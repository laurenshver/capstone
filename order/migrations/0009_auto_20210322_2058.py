# Generated by Django 3.1.4 on 2021-03-23 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0001_initial'),
        ('order', '0008_auto_20210322_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='CustomerQuoteID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='quote.quote'),
        ),
    ]
