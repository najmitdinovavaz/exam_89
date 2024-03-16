from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_verification_email(email: str, _uuid: str):
    link = f'http://localhost:8000/api/v1/users/confirm-email/{_uuid}'

    context = {
        'link': link
    }

    html_message = render_to_string('', context)
    plain_message = strip_tags(html_message)

    message = EmailMultiAlternatives(
        subject='NewCommerce account activation',
        body=plain_message,
        to=[email]
    )
    message.attach_alternative(html_message, 'text/html')
    message.send()
