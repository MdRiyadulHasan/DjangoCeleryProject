from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from CeleryProject import settings

@shared_task(bind=True)
def send_mail_func(self):
    #operations
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Testing Celery Project"
        message = "Dhaka is the capital of Bangladesh. Hello World ! Welcome to Programming"
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message = message,
            from_email = settings.EMAIL_HOST_USER,
            recipient_list =[to_email],
            fail_silently = True

        )
    return "Done Riyad Vai"
