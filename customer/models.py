from django.db import models

# Create your models here.
class Customer(models.Model):
    # table name customer_customer
    CUSTOMER_RATINGS = (
        ('G', 'GOOD'),
        ('K', 'OK'),
        ('P', 'POOR'),
    )
    CustomerID = models.AutoField(primary_key=True)
    DateCreated = models.DateField(auto_now_add=True)
    FirstName = models.CharField(max_length = 100)
    LastName = models.CharField(max_length = 100)
    Address = models.CharField(max_length = 100)
    City = models.CharField(max_length = 100)
    Province = models.CharField(max_length = 100)
    PostalCode = models.CharField(max_length = 100)
    HomeNumber = models.CharField(max_length = 100, blank=True, default=None)
    CellNumber = models.CharField(max_length = 100)
    EmailAddress = models.CharField(max_length = 100)
    CreditCardNumber = models.CharField(max_length = 100)
    CreditCardType = models.CharField(max_length = 100)
    CreditCardName = models.CharField(max_length = 100)
    BillingAddress = models.CharField(max_length = 100)
    BillingCity = models.CharField(max_length = 100)
    BillingProvince = models.CharField(max_length = 100)
    BillingPostalCode = models.CharField(max_length = 100)
    CustomerRating = models.CharField(max_length = 100, blank=True, default=None, choices=CUSTOMER_RATINGS)
    CustomerNotes = models.TextField(default=None,blank=True)


    def __str__(self):
        return self.FirstName + " " + self.LastName

class BusinessDiscountSchedule(models.Model):
    BusinessDiscountID = models.AutoField(primary_key = True)
    BusinessTier = models.CharField(max_length = 100)
    BusinessDiscountPercentage = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.BusinessTier + "  (" + str(self.BusinessDiscountPercentage) + "%)"

class BusinessClient(models.Model):
    BusinessClientID = models.AutoField(primary_key = True)
    # fk business discount
    BusinessDiscountID = models.ForeignKey(BusinessDiscountSchedule, on_delete=models.CASCADE)
    DateCreated = models.DateField(auto_now_add=True)
    BusinessName = models.CharField(max_length = 100)
    BusinessArea = models.CharField(max_length = 100)
    BusinessAddress = models.CharField(max_length = 100)
    BusinessCity = models.CharField(max_length = 100)
    BusinessProvince = models.CharField(max_length = 100)
    BusinessPostalCode = models.CharField(max_length = 100)
    BusinessPhoneNumber = models.CharField(max_length = 100)
    BusinessNumberExtension = models.CharField(max_length = 100, blank = True)
    BusinessEmail = models.CharField(max_length = 100)
    PrimaryContactName = models.CharField(max_length = 100)
    PrimaryContactPhoneNumber = models.CharField(max_length = 100)
    PrimaryContactExtension = models.CharField(max_length = 100, blank = True)
    PrimaryContactEmail = models.CharField(max_length = 100)
    BusinessNotes = models.TextField(default=None,blank=True)

    def __str__(self):
        return self.BusinessName + " (" + self.BusinessDiscountID.BusinessTier + ")"