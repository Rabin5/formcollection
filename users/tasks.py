from celery import shared_task

from django.core.mail.message import EmailMultiAlternatives

@shared_task
def send_email(subject, body, from_email, to_email):
    try:
        email = EmailMultiAlternatives(subject, body, from_email, to_email)
        email.content_subtype = 'html'
        email.send()
    except:
        raise