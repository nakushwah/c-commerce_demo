from celery import shared_task
from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import send_mail

logger = get_task_logger(__name__)


@shared_task(name='mail_task')
def send_mail_for_verification_link(email, username, token):
    logger.info(f'mail is sending.....to :{email}')
    send_mail(
        subject='Email Verification by Vastu Bhandar',
        message=f'''Hi {username} Please click on the link to verify you email id
                            http://localhost:8000/accounts/VerifyEmail/{token}''',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email])
