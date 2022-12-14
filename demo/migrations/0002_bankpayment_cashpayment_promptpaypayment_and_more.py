# Generated by Django 4.1 on 2022-10-14 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("demo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BankPayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PAID", "Paid"),
                            ("UNPAID", "Unpaid"),
                            ("PENDING", "Pending"),
                        ],
                        default="UNPAID",
                        max_length=10,
                    ),
                ),
                ("image", models.ImageField(blank=True, upload_to="images/")),
                ("bank", models.CharField(max_length=100)),
                ("bank_account", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                (
                    "bill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="demo.bills"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="CashPayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PAID", "Paid"),
                            ("UNPAID", "Unpaid"),
                            ("PENDING", "Pending"),
                        ],
                        default="UNPAID",
                        max_length=10,
                    ),
                ),
                (
                    "bill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="demo.bills"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PromptPayPayment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PAID", "Paid"),
                            ("UNPAID", "Unpaid"),
                            ("PENDING", "Pending"),
                        ],
                        default="UNPAID",
                        max_length=10,
                    ),
                ),
                ("image", models.ImageField(blank=True, upload_to="images/")),
                ("phone_number", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=100)),
                (
                    "bill",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="demo.bills"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.DeleteModel(
            name="Payment",
        ),
    ]
