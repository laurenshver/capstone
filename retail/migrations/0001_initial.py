# Generated by Django 3.1.4 on 2020-12-31 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeRole',
            fields=[
                ('PositionID', models.AutoField(primary_key=True, serialize=False)),
                ('PositionName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('StoreID', models.AutoField(primary_key=True, serialize=False)),
                ('StoreName', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Province', models.CharField(max_length=100)),
                ('PostalCode', models.CharField(max_length=100)),
                ('PhoneNumber', models.CharField(max_length=100)),
                ('NumberExt', models.CharField(max_length=100)),
                ('AssistantManagerID', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='assmanager', to='retail.employeerole')),
                ('ManagerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager', to='retail.employeerole')),
            ],
        ),
        migrations.CreateModel(
            name='HQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HQname', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=100)),
                ('Province', models.CharField(max_length=100)),
                ('PostalCode', models.CharField(max_length=100)),
                ('PhoneNumber', models.CharField(max_length=100)),
                ('EmailAddress', models.CharField(max_length=100)),
                ('CEOID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.employeerole')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeID', models.AutoField(primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('EmployeeEmail', models.CharField(blank=True, max_length=100)),
                ('EmployeePhoneNum', models.CharField(blank=True, max_length=100)),
                ('PositionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.employeerole')),
                ('StoreID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.store')),
            ],
        ),
    ]
