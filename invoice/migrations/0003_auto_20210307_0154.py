# Generated by Django 3.1.4 on 2021-03-07 01:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0002_auto_20210307_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='DueDate',
            field=models.DateField(default=datetime.datetime(2021, 4, 6, 1, 54, 24, 192382), editable=False),
        ),
    ]
