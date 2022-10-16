# Generated by Django 4.1 on 2022-10-14 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("demo", "0002_bankpayment_cashpayment_promptpaypayment_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bankpayment",
            name="bank",
            field=models.CharField(
                choices=[
                    ("KTB", "Ktb"),
                    ("BBL", "Bbl"),
                    ("SCB", "Scb"),
                    ("KRUNGTHAI", "Krungthai"),
                    ("TTB", "Tmb"),
                    ("BAY", "Bay"),
                    ("CREDIT", "Redcit"),
                    ("other", "Other"),
                ],
                default="other",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="bankpayment",
            name="bank_account",
            field=models.CharField(max_length=10),
        ),
    ]