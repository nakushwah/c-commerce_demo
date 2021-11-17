from django.urls import path
from django.views.generic import TemplateView
from .views import CheckOutPage, CheckOutPayment, my_webhook_view

urlpatterns = [
    path("CheckOutPayment/<cart_id>",
         CheckOutPayment.as_view(),
         name="CheckOutPayment"
         ),
    path("CreatePayment/<cart_id>",
         CheckOutPage.as_view(),
         name="CheckOutPage"
         ),
    path("PaymentDone/",
         TemplateView.as_view(template_name="PaymentSuccess.html"),
         name="PaymentDone"
         ),
    path("PaymentFailed/",
         TemplateView.as_view(template_name="PaymentFailed.html"),
         name="PaymentFailed"
         ),
    path("my_webhook_view/",
         my_webhook_view,
         name="my_webhook_view"
         ),
]
