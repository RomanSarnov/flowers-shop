from flowers_shop.celery import celery_app
from django.core.mail import send_mail
from django.conf import settings
from .models import Newsletter


@celery_app.task
def send_email_task(subject, text, sender, recipient):
    send_mail(subject, text, sender, recipient)


@celery_app.task
def send_newsletter():
    subject = 'Вы получили рассылку'
    text = 'Тут текст расслылки'
    sender = settings.EMAIL_HOST_USER
    recipients = [recipient.email for recipient in Newsletter.objects.all()]
    send_mail(subject, text, sender, recipients)