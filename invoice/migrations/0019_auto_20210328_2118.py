# Generated by Django 3.1.4 on 2021-03-28 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0018_remove_paymentmethod_paymentissuer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creditcardpayment',
            name='AddressID',
        ),
        migrations.RemoveField(
            model_name='creditcardpayment',
            name='CustomerID',
        ),
        migrations.RemoveField(
            model_name='creditcardpayment',
            name='PaymentID',
        ),
        migrations.DeleteModel(
            name='ChequePayment',
        ),
        migrations.DeleteModel(
            name='CreditCardPayment',
        ),
    ]