from django.db import models

# Create your models here.
class Address(models.Model):
    ADDRESS_TYPE = (
        ('C', 'Customer'),
        ('B', 'Business'),
        ('Bi', 'Billing'),
        ('D', 'Delivery'),
        ('S', 'Store'),
    )
    AddressID = models.AutoField(primary_key = True)
    AddressType = models.CharField(max_length = 2, choices = ADDRESS_TYPE)
    Address = models.CharField(max_length = 100)
    City = models.CharField(max_length = 100)
    Province = models.CharField(max_length = 100)
    PostalCode = models.CharField(max_length = 100)
    PhoneNumber = models.CharField(max_length = 30)

    def __str__(self):
        return self.Address + "(" + self.AddressType + ")"

class BusinessDiscountSchedule(models.Model):
    BusinessDiscountID = models.AutoField(primary_key = True)
    BusinessTier = models.CharField(max_length = 100)
    BusinessDiscountPercentage = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.BusinessTier + "  (" + str(self.BusinessDiscountPercentage) + "%)"


class Customer(models.Model):
    # table name customer_customer
    CUSTOMER_RATINGS = (
        ('G', 'GOOD'),
        ('K', 'OK'),
        ('P', 'POOR'),
    )

    CUSTOMER_TYPE = (
        ('C', 'Customer'),
        ('B', 'Business'),
    )
    CustomerID = models.AutoField(primary_key=True)
    BusinessDiscountID = models.ForeignKey(BusinessDiscountSchedule, on_delete=models.CASCADE, blank = True, null = True)
    AddressID = models.ForeignKey(Address, on_delete=models.CASCADE, blank = True, null = True)
    DateCreated = models.DateField(auto_now_add=True)
    FirstName = models.CharField(max_length = 100)
    LastName = models.CharField(max_length = 100, blank = True, null = True)
    CustomerType = models.CharField(max_length = 2, choices = CUSTOMER_TYPE, default = 'C', blank = True, null = True)
    HomeNumber = models.CharField(max_length = 20, blank=True, default=None)
    CellNumber = models.CharField(max_length = 20, blank = True)
    BusinessNumber = models.CharField(max_length = 20, blank = True)
    EmailAddress = models.CharField(max_length = 100, blank = True, null = True)
    BusinessPrimaryContact = models.CharField(max_length = 100, blank = True)
    BusinessPrimaryContactPhoneNumber = models.CharField(max_length = 100, blank = True)
    BusinessPrimaryContactEmail = models.CharField(max_length = 100, blank = True)
    CustomerRating = models.CharField(max_length = 2, blank=True, default=None, choices=CUSTOMER_RATINGS)
    CustomerNotes = models.TextField(default=None,blank=True)


    def __str__(self):
        return self.FirstName + " " + self.LastName