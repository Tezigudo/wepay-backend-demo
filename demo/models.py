
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Food(models.Model):
    """Topic model"""
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField("price")

class Bills(models.Model):
    pass

class Payment(models.Model):
    """Entry model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    bill = models.ForeignKey(Bills, on_del)

    class Status_choice(models.TextChoices):
        PAID = 'PAID', 'PAID'
        UNPAID = 'UNPAID'

    image = models.ImageField(

# field_name = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
# ImageField.upload_to

    )



