# Generated by Django 3.1.4 on 2021-01-10 20:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20210109_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='businessclient',
            name='DateCreated',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customer',
            name='DateCreated',
            field=models.DateField(auto_now_add=True),
        ),
    ]
