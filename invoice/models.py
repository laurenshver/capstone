from django.db import models
import order.models
from customer.models import Customer

# Create your models here.
YN = (
    ('Y', 'YES'),
    ('N', 'NO'),
)


class InvoiceStatus(models.Model):
    InvoiceStatus = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.InvoiceStatus

class PaymentMethod(models.Model):
    PaymentMethod = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.PaymentMethod

class Invoice(models.Model):
    InvoiceID = models.AutoField(primary_key = True)
    CostID = models.ForeignKey("order.Cost", on_delete=models.CASCADE)
    InvoiceStatusID = models.ForeignKey(InvoiceStatus, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE, blank = True, null = True)
    DueDate = models.DateField()
    DepositPaid = models.CharField(max_length = 5, choices = YN)
    DepositRefunded = models.CharField(max_length = 5, choices = YN)
    OverdueCharges = models.CharField(max_length = 5, choices = YN)

    def __str__(self):
        return str(self.InvoiceID)

class InvoiceOrder(models.Model):
    InvoiceID = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    OrderID = models.ForeignKey("order.Order", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.InvoiceID) + " " + str(self.OrderID)

class Payment(models.Model):
    InvoiceID = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    PaymentMethodID = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    TransactionDate = models.DateField(auto_now_add=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.InvoiceID) + " " + str(self.PaymentMethodID) + " " + str(self.Amount)

