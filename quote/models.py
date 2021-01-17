from django.db import models
from datetime import timedelta, datetime
from inventory.models import Inventory
from customer.models import BusinessClient, Customer

def two_business_days():
    '''sets the quote expiry date to be in the next 2 business days'''
    today = datetime.now()
    expiry_date = today + timedelta(days = 2)
    if expiry_date.weekday() == 5:
        expiry_date = expiry_date + timedelta(days = 2)
    elif expiry_date.weekday() == 6:
        expiry_date = expiry_date + timedelta(days = 2)
    return expiry_date

yn = (
        ('Y', 'YES'),
        ('N', 'NO'),
    )

# Create your models here.
class CustomerQuote(models.Model):
    CustomerQuoteID = models.AutoField(primary_key = True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    DateCreated = models.DateField(auto_now_add=True)
    Expired = models.CharField(max_length = 10, choices = yn, default = 'N')
    ExpiryDate = models.DateField(default = two_business_days, editable = False)
    CustomerFirstName = models.CharField(max_length = 100, blank = True)
    CustomerLastName = models.CharField(max_length = 100, blank = True)
    CustomerEmail = models.CharField(max_length = 100, blank = True)
    CustomerPhoneNumber = models.CharField(max_length = 100, blank = True)
    ProjectType = models.CharField(max_length = 100, blank = True)
    DesiredStartDate = models.DateField(auto_now=True)
    DesiredEndDate = models.DateField(auto_now=True)
    EstTotalCost = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    EstSubtotal = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    EstDeposit = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    EstTaxes = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    TandCAccepted = models.CharField(max_length = 10, choices = yn, default = 'N')

    def __str__(self):
        return self.CustomerFirstName + " " + self.CustomerLastName + " exp. " + str(self.ExpiryDate.strftime("%b %d %y"))


class CustomerQuoteTools(models.Model):
    CustomerQuoteID = models.ForeignKey(CustomerQuote, on_delete=models.CASCADE)
    ToolID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    QuantityRequested = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.CustomerQuoteID.CustomerQuoteID) + " - " + str(self.ToolID)


class BusinessQuote(models.Model):
    BusinessQuoteID = models.AutoField(primary_key = True)
    BusinessClientID = models.ForeignKey(BusinessClient, on_delete=models.CASCADE)
    DateCreated = models.DateField(auto_now_add=True)
    Expired = models.CharField(max_length = 10, choices = yn, default = 'N')
    ExpiryDate = models.DateField(default = two_business_days, editable = False)
    ProjectType = models.CharField(max_length = 100)
    ProjectAddress = models.CharField(max_length = 100)
    ProjectCity = models.CharField(max_length = 100)
    ProjectProvince = models.CharField(max_length = 100)
    ProjectPostalCode = models.CharField(max_length = 100)
    ProjectManager = models.CharField(max_length = 100)
    ProjectManagerContact = models.CharField(max_length = 100)
    ProjectEndDate = models.DateField(blank = True)
    RentalStartDate = models.DateField(blank = True)
    RentalEndDate = models.DateField(blank = True)
    EstTotalCost = models.DecimalField(max_digits=10, decimal_places=2)
    EstSubtotal = models.DecimalField(max_digits=10, decimal_places=2)
    EstDeposit = models.DecimalField(max_digits=10, decimal_places=2)
    EstTaxes = models.DecimalField(max_digits=10, decimal_places=2)
    EstShippingCost = models.DecimalField(max_digits=10, decimal_places=2)
    TandCAccepted = models.CharField(max_length = 10, choices = yn, default = 'N')

    def __str__(self):
        return self.BusinessClientID.BusinessName + " exp. " + str(self.ExpiryDate.strftime("%b %d %y"))

class BusinessQuoteTools(models.Model):
    BusinessQuoteID = models.ForeignKey(BusinessQuote, on_delete=models.CASCADE)
    ToolID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    QuantityRequested = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.BusinessQuoteID.BusinessQuoteID) + " - " + str(self.ToolID)