import random
from django.core.mail import EmailMessage, get_connection
from .models import User,OneTimePassword
from django.contrib.sites.shortcuts import get_current_site
from eccomerce.settings import base as settings
import os

def generateOtp():
    otp=""
    for i in range(6):
        otp+=str(random.randint(0,9))
    return otp

def send_code_to_user(email):
    Subject="passcod for email verification"
    otp_code=generateOtp()
    user=User.objects.get(email=email)
    current_site="mysite.com"
    email_body=f"Hi {user.first_name},\n\nYour OTP is {otp_code}\n\nRegards,\nTeam"
    from_email=settings.DEFAULT_FROM_EMAIL
    OneTimePassword.objects.create(user=user,code=otp_code)
    with get_connection(
        host=settings.RESEND_SMTP_HOST,
        port=settings.RESEND_SMTP_PORT,
        username=settings.RESEND_SMTP_USERNAME,
        password=os.environ["RESEND_API_KEY"],
        use_tls=True,
        ) as connection:
            d_email=EmailMessage(
                subject=Subject,
                body=email_body,
                from_email=from_email,
                to=[email],
                connection=connection,
            )
            d_email.send(fail_silently=True)
            
def send_normal_email(data):
    email_body=data['email_body']
    email_subject=data['email_subject']
    to_email=data['to_email']
    from_email=settings.DEFAULT_FROM_EMAIL
    with get_connection(
        host=settings.RESEND_SMTP_HOST,
        port=settings.RESEND_SMTP_PORT,
        username=settings.RESEND_SMTP_USERNAME,
        password=os.environ["RESEND_API_KEY"],
        use_tls=True,
        ) as connection:
            d_email=EmailMessage(
                subject=email_subject,
                body=email_body,
                from_email=from_email,
                to=[to_email],
                connection=connection,
            )
            d_email.send(fail_silently=True)