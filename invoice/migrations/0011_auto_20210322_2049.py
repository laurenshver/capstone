# Generated by Django 3.1.4 on 2021-03-23 00:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0010_auto_20210322_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='DueDate',
            field=models.DateField(default=datetime.datetime(2021, 4, 21, 20, 49, 8, 347088), editable=False),
        ),
    ]