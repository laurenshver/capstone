# Generated by Django 3.1.4 on 2021-03-23 00:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_auto_20210322_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='DueDate',
            field=models.DateField(default=datetime.datetime(2021, 4, 21, 20, 45, 37, 367289), editable=False),
        ),
    ]