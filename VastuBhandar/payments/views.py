"""
Views for the all payment related operation.inheriting the WishlistCart's models,
Payment's models and Generic views also using the strip payment gateway for the
payment, and django's send_mail for sending emails
"""


from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, View
from WishlistCart.models import UserCart
from .models import PaymentCheckOut
import stripe
from django.conf import settings

from .tasks import send_email_payment_update

stripe.api_key = settings.STRIPE_SECRET_KEY


class CheckOutPage(TemplateView):
    """ module for creating a checkout page for selected product
     from cart and make payment for it
     """
    template_name = "checkout.html"

    def get_context_data(self, **kwargs):
        cart_id = self.kwargs['cart_id']
        cart_product = UserCart.objects.get(id=cart_id)
        context = super(CheckOutPage, self).get_context_data(**kwargs)
        context.update({
            "cart_product": cart_product,
            'secret_key': settings.STRIPE_PUBLISHABLE_KEY
        })
        return context


class CheckOutPayment(View):
    """
    creating a stripe payment intent with a product's details
    in this module using Stripe's API for creating intent
    """

    def post(self, request, *args, **kwargs):
        cart_id = self.kwargs['cart_id']
        cart = UserCart.objects.get(id=cart_id)
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=[
                'card',
            ],
            line_items=[
                {
                    "price_data": {
                        'currency': 'inr',
                        'unit_amount': int(cart.cart_price * 100),
                        'product_data': {
                            'name': cart.product_id.name
                        }
                    },
                    "quantity": cart.quantity,
                },
            ],
            metadata={"cart_id": cart.id},
            mode='payment',
            success_url='http://127.0.0.1:8000/payments/PaymentDone/',
            cancel_url='http://127.0.0.1:8000/payments/PaymentFailed/',
        )
        return JsonResponse({"id": checkout_session.id})



@csrf_exempt
def my_webhook_view(request):

    """
    this module is created for the making after payment's operations
    we are using here the Stripe's Webhook API for checking the session
    and sending the email to user about their purchase information
    """

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        cart = UserCart.objects.get(id=session['metadata']['cart_id'])
        payment = PaymentCheckOut.objects.create(
            cart=cart, amount=session['amount_total'],
            payment_id=session['payment_intent'], status=session['payment_status']
        )
        send_email_payment_update(payment, email=session['customer_details']['email'])
    return HttpResponse(status=200)

