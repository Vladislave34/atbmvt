


import uuid

from django.core.mail import send_mail
from django.conf import settings

def upload_avatar(size):
    def wrapper(instance, filename):
        return f"avatars/{size}/{uuid.uuid4()}.webp"
    return wrapper





