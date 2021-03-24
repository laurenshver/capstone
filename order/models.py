from django.db import models
import quote.models
from customer.models import Customer, Address, Province
from retail.models import Store, Employee
from inventory.models import Inventory, ToolPrice

# Create your models here.
YN = (
    ('Y', 'YES'),
    ('N', 'NO'),
)

class OrderStatus(models.Model):
    OrderStatus = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.OrderStatus

class ToolRetreival(models.Model):
    ToolRetreival = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.ToolRetreival

class ExtraFeeSchedule(models.Model):
    ExtraFeeID = models.AutoField(primary_key = True)
    DamageName = models.CharField(max_length = 100)
    DamageDescription = models.CharField(max_length = 150)
    FeeCost = models.DecimalField(max_digits=10, decimal_places=2)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.DamageName + " $" + str(self.FeeCost)

class TaxCode(models.Model):
    ProvinceID = models.ForeignKey(Province, on_delete=models.CASCADE)
    HSTCharge = models.CharField(max_length = 2, choices = YN)
    HSTPercentage = models.DecimalField(max_digits=10, decimal_places=2)
    GSTCharge = models.CharField(max_length = 2, choices = YN)
    GSTPercentage = models.DecimalField(max_digits=10, decimal_places=2)
    MARCharge = models.CharField(max_length = 2, choices = YN)
    MARPercentage = models.DecimalField(max_digits=10, decimal_places=2)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.ProvinceID.ProvinceShortName + str(self.GSTPercentage) + str(self.HSTPercentage) + str(self.MARPercentage)

class Cost(models.Model):
    CostID = models.AutoField(primary_key = True)
    TaxCodeID = models.ForeignKey(TaxCode, on_delete=models.CASCADE, blank = True, null = True)
    Total = models.DecimalField(max_digits=10, decimal_places=2)
    Subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    Taxes = models.DecimalField(max_digits=10, decimal_places=2)
    BusinessDiscount = models.DecimalField(max_digits=10, decimal_places=2, blank = True, null = True)
    Deposit = models.DecimalField(max_digits=10, decimal_places=2, blank = True, null = True)
    OverdueCharges = models.DecimalField(max_digits=10, decimal_places=2, blank = True, null = True)

    def __str__(self):
        return str(self.Total)

class Order(models.Model):
    OrderID = models.AutoField(primary_key = True)
    # fk from customer quote
    CustomerQuoteID = models.ForeignKey("quote.Quote", on_delete=models.CASCADE, blank = True, null=True)
    # fk from customer
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    # fk from employee
    EmployeeID = models.ForeignKey(Employee, on_delete= models.CASCADE)
    # fk from address
    AddressID = models.ForeignKey(Address, on_delete=models.CASCADE, blank = True, null = True)
    CostID = models.ForeignKey(Cost, on_delete=models.CASCADE, blank = True, null = True)
    OrderStatusID = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, blank = True, null = True)
    ToolRetreival = models.ForeignKey(ToolRetreival, on_delete=models.CASCADE, blank = True, null = True)
    StartDate = models.DateTimeField()
    EstimatedEndDate = models.DateTimeField()
    EndDate = models.DateTimeField(blank = True, null = True)
    TandCAccepted = models.CharField(max_length = 10, choices = YN, default = 'N')
    OrderNotes = models.TextField(blank=True, null=True)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.CustomerID) + " " + str(self.OrderStatusID.OrderStatus)


class OrderTool(models.Model):
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    InventoryID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    ToolPriceID = models.ForeignKey(ToolPrice, on_delete=models.CASCADE)
    StartDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    RentalLength = models.PositiveSmallIntegerField()
    

    def __str__(self):
        return str(self.OrderID) + str(self.InventoryID)

class DeliveryStatus(models.Model):
    DeliveryStatus = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.DeliveryStatus

class OrderDelivery(models.Model):
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    DeliveryStatusID = models.ForeignKey(DeliveryStatus, on_delete=models.CASCADE)
    InventoryID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    DeliveryDate = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return str(self.DeliveryDate) + self.DeliveryStatusID.DeliveryStatus

class PickupStatus(models.Model):
    PickupStatus = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.PickupStatus

class OrderPickup(models.Model):
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    PickupStatusID = models.ForeignKey(PickupStatus, on_delete=models.CASCADE)
    PickupDate = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return str(self.PickupDate) + self.PickupStatusID.PickupStatus