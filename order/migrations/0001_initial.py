# Generated by Django 3.1.4 on 2021-03-07 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
        ('customer', '0001_initial'),
        ('retail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('CostID', models.AutoField(primary_key=True, serialize=False)),
                ('Total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Subtotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Taxes', models.DecimalField(decimal_places=2, max_digits=10)),
                ('BusinessDiscount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Deposit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('OverdueCharges', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeliveryStatus', models.CharField(max_length=100)),
                ('ModifiedDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraFeeSchedule',
            fields=[
                ('ExtraFeeID', models.AutoField(primary_key=True, serialize=False)),
                ('DamageName', models.CharField(max_length=100)),
                ('DamageDescription', models.CharField(max_length=150)),
                ('FeeCost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ModifiedDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderID', models.AutoField(primary_key=True, serialize=False)),
                ('OrderStatus', models.CharField(choices=[('O', 'OPEN'), ('C', 'CLOSED')], default='O', max_length=100)),
                ('ToolRetreival', models.CharField(blank=True, choices=[('D', 'Delivery'), ('P', 'Patron Pickup')], max_length=10, null=True)),
                ('StartDate', models.DateTimeField(auto_now_add=True)),
                ('EstimatedEndDate', models.DateTimeField()),
                ('EndDate', models.DateTimeField()),
                ('TandCAccepted', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], default='N', max_length=10)),
                ('OrderStatusAfterRefund', models.CharField(choices=[('G', 'GOOD'), ('O', 'OK'), ('P', 'POOR')], default='G', max_length=20)),
                ('OrderNotes', models.TextField(blank=True)),
                ('ModifiedDate', models.DateField(auto_now=True)),
                ('AddressID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.address')),
                ('CostID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.cost')),
                ('CustomerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
        migrations.CreateModel(
            name='PickupStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PickupStatus', models.CharField(max_length=100)),
                ('ModifiedDate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaxCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HSTCharge', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=2)),
                ('HSTPercentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('GSTCharge', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=2)),
                ('GSTPercentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('MARCharge', models.CharField(choices=[('Y', 'YES'), ('N', 'NO')], max_length=2)),
                ('MARPercentage', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ModifiedDate', models.DateField(auto_now=True)),
                ('ProvinceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.province')),
            ],
        ),
        migrations.CreateModel(
            name='OrderTool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('StartDate', models.DateTimeField()),
                ('EndDate', models.DateTimeField()),
                ('RentalLength', models.PositiveSmallIntegerField()),
                ('InventoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('OrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('ToolPriceID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.toolprice')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPickup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PickupDate', models.DateTimeField(blank=True, null=True)),
                ('EmployeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.employee')),
                ('OrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('PickupStatusID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.pickupstatus')),
            ],
        ),
        migrations.CreateModel(
            name='OrderDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DeliveryDate', models.DateTimeField(blank=True, null=True)),
                ('DeliveryStatusID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.deliverystatus')),
                ('EmployeeID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retail.employee')),
                ('InventoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.inventory')),
                ('OrderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
        ),
    ]
