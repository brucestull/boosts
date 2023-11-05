from celery import shared_task
from django.core.mail import send_mail


@shared_task()
def send_boost_email_task(
    current_site_domain,
    user_username,
    user_email,
    user_beastie_email,
    user_beastie_username,
    message,
):
    """
    Sends an email.
    """
    # Send the inspirational quote to the user's beastie:
    send_mail(
        f"Inspirational Quote from your Beastie: {user_username}",
        message,
        user_email,
        [user_beastie_email],
        fail_silently=False,
    )
    # Send a copy of the inspirational quote to the user:
    send_mail(
        f"You Sent an Inspirational Quote to your Beastie: {user_beastie_username}",
        message,
        user_email,
        [user_email],
        fail_silently=False,
    )
