from django.db import models
from datetime import timedelta, datetime
import order.models
import customer.models

# Create your models here.
YN = (
    ('Y', 'YES'),
    ('N', 'NO'),
)

def invoice_expiry():
    '''calculate the invoice expiry date, which is 30 days from the incoice creation'''
    today = datetime.now()
    expiry_date = today + timedelta(days = 30)
    return expiry_date


class InvoiceStatus(models.Model):
    InvoiceStatus = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.InvoiceStatus

class PaymentMethod(models.Model):
    PaymentMethod = models.CharField(max_length = 100)
    PaymentIssuer = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.PaymentMethod + " " + self.PaymentIssuer

class Invoice(models.Model):
    InvoiceID = models.AutoField(primary_key = True)
    CostID = models.ForeignKey("order.Cost", on_delete=models.CASCADE)
    InvoiceStatusID = models.ForeignKey(InvoiceStatus, on_delete=models.CASCADE)
    DueDate = models.DateField(default = invoice_expiry(), editable = False)
    DepositPaid = models.CharField(max_length = 5, choices = YN)
    DepositRefunded = models.CharField(max_length = 5, choices = YN)
    OverdueCharges = models.CharField(max_length = 5, choices = YN)

    def __str__(self):
        return str(self.InvoiceID) + str(self.DueDate)

class InvoiceOrder(models.Model):
    InvoiceID = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    OrderID = models.ForeignKey("order.Order", on_delete=models.CASCADE)

    def __str__(self):
        return self.InvoiceID + " " + self.OrderID

class Payment(models.Model):
    InvoiceID = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    PaymentMethodID = models.ForeignKey(PaymentMethod, on_delete=models.CASCADE)
    TransactionDate = models.DateField(auto_now_add=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.PaymentMethodID + str(self.Amount)

class CreditCardPayment(models.Model):
    PaymentID = models.ForeignKey(Payment, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey("customer.Customer", on_delete=models.CASCADE, blank = True, null = True)
    AddressID = models.ForeignKey("customer.Address", on_delete=models.CASCADE)
    CreditCardNumber = models.CharField(max_length = 30)
    CCV = models.CharField(max_length = 5)
    ExpiryDate = models.DateField()
    CreditCardType = models.CharField(max_length = 30)
    CreditCardName = models.CharField(max_length = 100)

    def __str__(self):
        return self.CreditCardName + " *" + self.CreditCardNumber[-4:]

class ChequePayment(models.Model):
    PaymentID = models.ForeignKey(Payment, on_delete=models.CASCADE)
    ChequeDate = models.DateField()
    PayTo = models.CharField(max_length = 100)
    ChequeTotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.PayTo + str(self.ChequeTotal)

