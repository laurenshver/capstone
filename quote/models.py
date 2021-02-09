from django.db import models
from datetime import timedelta, datetime
from inventory.models import Inventory
from customer.models import Customer, Address
from retail.models import Store

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

RENTAL_RATE = (
    ('H', 'HOURLY'),
    ('D', 'DAILY'),
    ('W', 'WEEKLY'),
    ('M', 'MONTHLY'),
)

# Create your models here.
class Quote(models.Model):
    QuoteID = models.AutoField(primary_key = True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=True)
    StoreID = models.ForeignKey(Store, on_delete=models.CASCADE, blank=True)
    AddressID = models.ForeignKey(Address, on_delete=models.CASCADE, blank=True, null = True)
    DateCreated = models.DateField(auto_now_add=True)
    Expired = models.CharField(max_length = 10, choices = yn, default = 'N')
    ExpiryDate = models.DateField(default = two_business_days, editable = False)
    CustomerFirstName = models.CharField(max_length = 100, blank = True)
    CustomerLastName = models.CharField(max_length = 100, blank = True)
    CustomerEmail = models.CharField(max_length = 100, blank = True)
    CustomerPhoneNumber = models.CharField(max_length = 100, blank = True)
    ProjectType = models.CharField(max_length = 100, blank = True)
    BusinessProjectManager = models.CharField(max_length = 100, blank = True)
    BusinessProjectManagerContact = models.CharField(max_length = 100, blank = True)
    DesiredStartDate = models.DateField(auto_now=True)
    DesiredEndDate = models.DateField(auto_now=True)
    EstTotalCost = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    EstSubtotal = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    EstDeposit = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    EstTaxes = models.DecimalField(max_digits=10, decimal_places=2, default = 0.00)
    TandCAccepted = models.CharField(max_length = 10, choices = yn, default = 'N')

    def __str__(self):
        return self.CustomerFirstName + " " + self.CustomerLastName + " exp. " + str(self.ExpiryDate.strftime("%b %d %y"))


class QuoteTool(models.Model):
    QuoteID = models.ForeignKey(Quote, on_delete=models.CASCADE)
    ToolID = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    RateRequested = models.CharField(max_length = 2, choices = RENTAL_RATE, blank = True)
    QuantityRequested = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.QuoteID.CustomerQuoteID) + " - " + str(self.ToolID)