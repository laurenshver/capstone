from django.db import models
from quote.models import CustomerQuote, BusinessQuote
from customer.models import Customer, BusinessClient
from retail.models import Store, Employee
from inventory.models import Inventory

# Create your models here.
YN = (
    ('Y', 'YES'),
    ('N', 'NO'),
)

STATUS = (
    ('O', 'OPEN'),
    ('C', 'CLOSED'),
)

REFUND_STATUS = (
    ('G', 'GOOD'),
    ('K', 'OK'),
    ('P', 'POOR'),
)

RENTAL_RATE = (
    ('H', 'HOURLY'),
    ('D', 'DAILY'),
    ('W', 'WEEKLY'),
    ('M', 'MONTHLY'),
)

class ExtraFeeSchedule(models.Model):
    ExtraFeeID = models.AutoField(primary_key = True)
    DamageName = models.CharField(max_length = 100)
    DamageDescription = models.CharField(max_length = 150)
    FeeCost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.DamageName + " $" + str(self.FeeCost)


class CustomerOrder(models.Model):
    OrderID = models.AutoField(primary_key = True)
    # fk from customer quote
    CustomerQuoteID = models.ForeignKey(CustomerQuote, on_delete=models.CASCADE, blank = True)
    # fk from customer
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # fk from extra fee schedule
    ExtraFeeID = models.ForeignKey(ExtraFeeSchedule, on_delete=models.CASCADE, blank = True, null = True)
    # fk from store
    StoreID = models.ForeignKey(Store, on_delete=models.CASCADE)
    # fk from employee
    EmployeeID = models.ForeignKey(Employee, on_delete= models.CASCADE)
    OrderStatus = models.CharField(max_length=100, choices=STATUS, default='O')
    StartDate = models.DateTimeField(auto_now_add=True)
    EstimatedEndDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    TandCAccepted = models.CharField(max_length = 10, choices = YN, default = 'N')
    TotalOrderCost = models.DecimalField(max_digits=10, decimal_places=2)
    Subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    TaxesAmount = models.DecimalField(max_digits=10, decimal_places=2)
    DepositPaid = models.CharField(max_length = 10, choices = YN, default = 'N')
    DepositAmount = models.DecimalField(max_digits=10, decimal_places=2, blank = True)
    DepositRefunded = models.CharField(max_length = 10, choices = YN)
    OverdueCharges = models.CharField(max_length = 10, choices = YN)
    OverdueCost = models.DecimalField(max_digits=10, decimal_places=2, blank = True, null = True)
    OrderStatusAfterRefund = models.CharField(max_length = 20, choices = REFUND_STATUS, default = 'G')
    OrderNotes = models.TextField(blank=True)

    def __str__(self):
        return str(self.CustomerID) + " " + str(self.OrderStatus)


class CustomerOrderTool(models.Model):
    OrderID = models.ForeignKey(CustomerOrder, on_delete=models.CASCADE)
    ToolID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    RentalRate = models.CharField(max_length = 10, choices = RENTAL_RATE)
    QuantityRented = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.ToolID)


class BusinessOrder(models.Model):
    BusinessOrderID = models.AutoField(primary_key = True)
    # fk from business quote
    BusinessQuoteID = models.ForeignKey(BusinessQuote, on_delete=models.CASCADE, blank = True, null = True)
    # fk from business client
    BusinessClientID = models.ForeignKey(BusinessClient, on_delete=models.CASCADE)
    # fk extra fees
    ExtraFeeID = models.ForeignKey(ExtraFeeSchedule, on_delete=models.CASCADE, blank = True, null = True)
    # fk from store
    StoreID = models.ForeignKey(Store, on_delete=models.CASCADE)
    # fk from employee
    EmployeeID = models.ForeignKey(Employee, on_delete= models.CASCADE)
    OrderStatus = models.CharField(max_length=100, choices=STATUS, default='O')
    StartDate = models.DateTimeField(auto_now_add=True)
    EstimatedEndDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    TandCAccepted = models.CharField(max_length = 10, choices = YN, default = 'N')
    TotalOrderCost = models.DecimalField(max_digits=10, decimal_places=2)
    Subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    DiscountAmount = models.DecimalField(max_digits=10, decimal_places=2)
    TaxesAmount = models.DecimalField(max_digits=10, decimal_places=2)
    DepositPaid = models.CharField(max_length = 10, choices = YN, default = 'N')
    DepositAmount = models.DecimalField(max_digits=10, decimal_places=2, blank = True)
    DepositRefunded = models.CharField(max_length = 10, choices = YN)
    OverdueCharges = models.CharField(max_length = 10, choices = YN)
    OverdueCost = models.DecimalField(max_digits=10, decimal_places=2, blank = True, null = True)
    OrderStatusAfterRefund = models.CharField(max_length = 20, choices = REFUND_STATUS, default = 'G')
    OrderNotes = models.TextField(blank=True)

    def __str__(self):
        return str(self.BusinessClientID)


class BusinessOrderTool(models.Model):
    OrderID = models.ForeignKey(BusinessOrder, on_delete=models.CASCADE)
    ToolID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    RentalRate = models.CharField(max_length = 10, choices = RENTAL_RATE)
    QuantityRented = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.ToolID)