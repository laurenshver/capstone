# Generated by Django 3.1.4 on 2021-03-28 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0017_invoice_customerid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paymentmethod',
            name='PaymentIssuer',
        ),
    ]
