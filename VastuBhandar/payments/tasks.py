from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import send_mail

logger = get_task_logger(__name__)


@shared_task(name='payment_update')
def send_email_payment_update(payment, email):
    logger.info(f'mail is sending.....to :{email}')
    send_mail(
        subject='Email Verification by Vastu Bhandar',
        message=f'''Hi {payment.cart.user_id.username}  you order has successfully purchased by you .
         and your payment_id is {payment.id}
''',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email])
