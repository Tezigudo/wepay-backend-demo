
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from typing import List


class Bills(models.Model):
    header = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pub_date = models.DateTimeField(default=timezone.localtime)


class Food(models.Model):
    """Topic model"""
    title = models.CharField(max_length=100)
    price = models.IntegerField("price")
    bill = models.ForeignKey(Bills, on_delete=models.CASCADE)
    user: List[User] = []


    def add_user(self, user):
        self.user.append(user)


class Payment(models.Model):
    """Entry model"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    bill = models.ForeignKey(Bills, on_delete=models.CASCADE)

    class Status_choice(models.TextChoices):
        PAID = 'PAID'
        UNPAID = 'UNPAID'
        PENDING = 'PENDING'

    status = models.CharField(
        choices=Status_choice.choices,
        default=Status_choice.UNPAID,
        max_length=10)

    image = models.ImageField(upload_to='images/', blank=True)
