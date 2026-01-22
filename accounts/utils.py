#for sending verification email

import secrets
import smtplib
from django.conf import settings
from django.core.mail import send_mail

def generate_verification_token():
    return secrets.token_urlsafe(32)


def send_verification_email(user):
    token = generate_verification_token()
    user.email_verification_token = token
    user.save()

    verification_url = f"{settings.BACKEND_URL}/api/auth/verify-email/?token={token}"

    subject = "Verify your email address"

    #we can add beautiful HTML email later
    message = f"Hi, {user.first_name}, Please click the following link to verify your email address: {verification_url}"
    html_message = None

    try:
        send_mail(
            subject=subject,
            message= message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[user.email],
            html_message = html_message, # if you want to send HTML email (plain text fallback)
            fail_silently=False, #raise exception if email sending fails but silently=False
        )
        return True
    except smtplib.SMTPException as e:
        print(f"Error sending verification email: {e}")
        return False
    
