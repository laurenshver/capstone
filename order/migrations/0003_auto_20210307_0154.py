# Generated by Django 3.1.4 on 2021-03-07 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20210307_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderStatus', models.CharField(max_length=100)),
                ('ModifiedDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ToolRetreival',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ToolRetreival', models.CharField(max_length=100)),
                ('ModifiedDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='OrderStatus',
        ),
        migrations.RemoveField(
            model_name='order',
            name='OrderStatusAfterRefund',
        ),
        migrations.AddField(
            model_name='order',
            name='OrderStatusID',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.orderstatus'),
        ),
        migrations.AlterField(
            model_name='order',
            name='ToolRetreival',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.toolretreival'),
        ),
    ]
