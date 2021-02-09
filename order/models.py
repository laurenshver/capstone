from django.db import models
from datetime import timedelta, datetime
from quote.models import Quote
from customer.models import Customer, Address
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

TOOL_RETREIVAL = (
    ('D', 'Delivery'),
    ('P', 'Pickup'),
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

TOOL_CONDITIONS = (
    ('G', 'GOOD'),
    ('DR', 'DAMAGE/REPAIR'),
    ('D', 'DAMAGED'),
)

CC_TYPE = (
    ('V', 'VISA'),
    ('M', 'MASTERCARD'),
    ('A', 'AMERICAN EXPRESS'),
)

PAYMENT_TYPE = (
    ('CC', 'CREDIT CARD'),
    ('CA', 'CASH'),
)

def invoice_expiry():
    '''calculate the invoice expiry date, which is 30 days from the incoice creation'''
    today = datetime.now()
    expiry_date = today + timedelta(days = 30)
    return expiry_date

class ExtraFeeSchedule(models.Model):
    ExtraFeeID = models.AutoField(primary_key = True)
    DamageName = models.CharField(max_length = 100)
    DamageDescription = models.CharField(max_length = 150)
    FeeCost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.DamageName + " $" + str(self.FeeCost)

class PaymentInformation(models.Model):
    PaymentInformationID = models.AutoField(primary_key = True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    AddressID = models.ForeignKey(Address, on_delete=models.CASCADE)
    CreditCardNum = models.CharField(max_length = 30)
    CreditCardType = models.CharField(max_length = 3, choices = CC_TYPE)
    CreditCardCustomerName = models.CharField(max_length = 100)

    def __str__(self):
        return self.CreditCardType + " " + self.CreditCardCustomerName

class Order(models.Model):
    OrderID = models.AutoField(primary_key = True)
    # fk from customer quote
    CustomerQuoteID = models.ForeignKey(Quote, on_delete=models.CASCADE, blank = True)
    # fk from customer
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    # fk from store
    StoreID = models.ForeignKey(Store, on_delete=models.CASCADE)
    # fk from employee
    EmployeeID = models.ForeignKey(Employee, on_delete= models.CASCADE)
    # fk from address
    AddressID = models.ForeignKey(Address, on_delete=models.CASCADE, blank = True, null = True)
    OrderStatus = models.CharField(max_length=100, choices=STATUS, default='O')
    ToolRetreival = models.CharField(max_length = 10, choices = TOOL_RETREIVAL, blank = True, null = True)
    StartDate = models.DateTimeField(auto_now_add=True)
    EstimatedEndDate = models.DateTimeField()
    EndDate = models.DateTimeField()
    TandCAccepted = models.CharField(max_length = 10, choices = YN, default = 'N')
    OrderStatusAfterRefund = models.CharField(max_length = 20, choices = REFUND_STATUS, default = 'G')
    OrderNotes = models.TextField(blank=True)

    def __str__(self):
        return str(self.CustomerID) + " " + str(self.OrderStatus)


class OrderTool(models.Model):
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    ToolID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    ToolNum = models.PositiveSmallIntegerField(blank = True, null = True)
    RentalRate = models.CharField(max_length = 10, choices = RENTAL_RATE)
    QuantityRented = models.PositiveSmallIntegerField()
    RentalLength = models.PositiveSmallIntegerField()
    ToolConditionAtRental = models.CharField(max_length = 10, choices = TOOL_CONDITIONS, blank = True)
    ToolConditionAtRefund = models.CharField(max_length = 10, choices = TOOL_CONDITIONS, blank = True)

    def __str__(self):
        return str(self.ToolID)

class Invoice(models.Model):
    InvoiceID = models.AutoField(primary_key = True)
    # fk from order
    OrderID = models.ForeignKey(Order, on_delete=models.CASCADE)
    # fk from extra fee schedule
    ExtraFeeID = models.ForeignKey(ExtraFeeSchedule, on_delete=models.CASCADE, blank = True, null = True)
    ExpiryDate = models.DateField(default = invoice_expiry, editable = False)
    TotalOrderCost = models.DecimalField(max_digits=10, decimal_places=2)
    Subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    TaxesAmount = models.DecimalField(max_digits=10, decimal_places=2)
    DiscountAmount = models.DecimalField(max_digits=10, decimal_places=2, blank = True)
    DepositPaid = models.CharField(max_length = 10, choices = YN, default = 'N')
    DepositAmount = models.DecimalField(max_digits=10, decimal_places=2, blank = True)
    DepositRefunded = models.CharField(max_length = 10, choices = YN)
    OverdueCharges = models.CharField(max_length = 10, choices = YN)
    OverdueCost = models.DecimalField(max_digits=10, decimal_places=2, blank = True, null = True)

    def __str__(self):
        return self.OrderID + str(self.TotalOrderCost)

class Payment(models.Model):
    PaymentID = models.AutoField(primary_key = True)
    InvoiceID = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    PaymentInformationID = models.ForeignKey(PaymentInformation, on_delete=models.CASCADE)
    DatePaid = models.DateField()
    PaymentMethod = models.CharField(max_length = 5, choices = PAYMENT_TYPE)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.PaymentID.CreditCardCustomerName) + " " + str(self.Amount)