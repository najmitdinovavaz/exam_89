from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model, ForeignKey, CASCADE, ImageField, PositiveIntegerField, EmailField


class User(AbstractUser):
    username = CharField(unique=True, max_length=255)
    photo = ImageField(upload_to='users/images', default='users/default.jpg')
    email = EmailField(max_length=255, blank=True)
    password = CharField(max_length=255, blank=True)


class Category(Model):
    name = CharField(max_length=255)


class Product(Model):
    name = CharField(max_length=255, blank=True)
    user = ForeignKey('apps.User', CASCADE)
    category = ForeignKey('apps.Category', CASCADE)
    price = PositiveIntegerField(default=0)
    version = CharField(max_length=255, blank=True)
    color = CharField(max_length=255, blank=True)
    kg = PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class ProductImage(Model):
    product = ForeignKey('apps.Product' ,CASCADE)
    image = ImageField(upload_to='products/images')
