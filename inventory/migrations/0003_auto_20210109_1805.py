# Generated by Django 3.1.4 on 2021-01-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20210102_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='TimesRented',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
