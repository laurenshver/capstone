from django.db import models
from datetime import timedelta, datetime
from inventory.models import Inventory, PriceRate
from customer.models import Customer, Address, BusinessContact
from retail.models import Store
import order.models

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
class QuoteStatus(models.Model):
    QuoteStatus = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.QuoteStatus

class Quote(models.Model):
    QuoteID = models.AutoField(primary_key = True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    StoreID = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True)
    AddressID = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null = True)
    CostID = models.ForeignKey("order.Cost", on_delete=models.CASCADE, blank=True, null = True)
    QuoteStatus = models.ForeignKey(QuoteStatus, on_delete=models.CASCADE, blank=True, null = True)
    BusinessContactID = models.ForeignKey(BusinessContact, on_delete=models.CASCADE, blank=True, null = True)
    DateCreated = models.DateField(auto_now_add=True)
    ExpiryDate = models.DateField(default = two_business_days, editable = False)
    ProjectType = models.CharField(max_length = 100, blank = True)
    DesiredStartDate = models.DateField(auto_now=True)
    DesiredEndDate = models.DateField(auto_now=True)
    QuoteAccepted = models.CharField(max_length = 10, choices = yn, default = 'Y')

    def __str__(self):
        return self.CustomerFirstName + " " + self.CustomerLastName + " exp. " + str(self.ExpiryDate.strftime("%b %d %y"))


class QuoteTool(models.Model):
    QuoteID = models.ForeignKey(Quote, on_delete=models.CASCADE)
    ToolID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    RateRequested = models.ForeignKey(PriceRate, on_delete=models.CASCADE)
    QuantityRequested = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.QuoteID) + " - " + str(self.ToolID)