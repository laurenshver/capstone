# Generated by Django 3.1.4 on 2021-03-09 00:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_auto_20210309_0002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='DueDate',
            field=models.DateField(default=datetime.datetime(2021, 4, 8, 0, 25, 26, 464287), editable=False),
        ),
    ]
