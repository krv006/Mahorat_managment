from celery import shared_task
from django.core.mail import send_mail

from root.settings import EMAIL_HOST_USER


@shared_task
def send_email(email: str | list[str], msg: str):
    subject = 'Confirmation'
    send_mail(subject, msg, EMAIL_HOST_USER, (email if type(email) is list else [email]))

    return f'send email to {email} successfully'
