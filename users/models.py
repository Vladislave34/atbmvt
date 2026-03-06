from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.


class CustomUser(AbstractUser):
    # Поле для зберігання маленького аватара користувача
    # upload_to="avatars/" означає, що файл буде зберігатись у папці media/avatars
    # null=True дозволяє зберігати NULL у базі даних
    # blank=True дозволяє залишати поле порожнім у формах
    image_small = models.ImageField(upload_to="avatars/", null=True, blank=True)

    # Поле для зберігання аватара середнього розміру
    # Використовується, наприклад, у профілі користувача
    image_medium = models.ImageField(upload_to="avatars/", null=True, blank=True)

    # Поле для зберігання великого аватара
    # Може використовуватись для сторінки профілю або детального перегляду
    image_big = models.ImageField(upload_to="avatars/", null=True, blank=True)

    def __str__(self):
        # Метод, який визначає як об'єкт користувача буде відображатися у Django Admin
        # Тут буде показуватись email користувача
        return self.email