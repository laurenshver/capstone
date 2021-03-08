from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

YN = (
    ('Y', 'YES'),
    ('N', 'NO'),
)

class IdentifierType(models.Model):
    IdentifierTypeID = models.AutoField(primary_key = True)
    IdentifierType = models.CharField(max_length = 30)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.IdentifierType

class Province(models.Model):
    ProvinceID = models.AutoField(primary_key = True)
    ProvinceShortName = models.CharField(max_length = 20)
    ProvinceLongName = models.CharField(max_length = 50)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.ProvinceLongName + "(" + self.ProvinceShortName + ")"

class PhoneNumberType(models.Model):
    PhoneNumberType = models.CharField(max_length = 20)
    ModifiedDate = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.PhoneNumberType

class PhoneNumber(models.Model):
    
    PhoneNumberID = models.AutoField(primary_key = True)
    IdentifierType = models.ForeignKey(IdentifierType, on_delete=models.CASCADE, blank = True, null = True)
    PhoneNumberType = models.ForeignKey(PhoneNumberType, on_delete=models.CASCADE, blank = True, null = True)
    PhoneNumber = models.CharField(max_length = 30)
    Extension = models.CharField(max_length = 10, blank = True, null = True)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        if self.Extension:
            return str(self.IdentifierType.IdentifierType) + " " + str(self.PhoneNumberType.PhoneNumberType) + " " + self.PhoneNumber + " ext. " + self.Extension
        else:
            return str(self.IdentifierType.IdentifierType) + " " + str(self.PhoneNumberType.PhoneNumberType) + " " + self.PhoneNumber

class Address(models.Model):
    
    AddressID = models.AutoField(primary_key = True)
    IdentifierTypeID = models.ForeignKey(IdentifierType, on_delete=models.CASCADE, blank = True, null = True)
    AptSuite = models.CharField(max_length = 100, blank = True, null = True)
    Address = models.CharField(max_length = 100)
    City = models.CharField(max_length = 100)
    Country = models.CharField(max_length = 100, default = 'Canada')
    ProvinceID = models.ForeignKey(Province, on_delete=models.CASCADE, blank = True, null = True)
    PostalCode = models.CharField(max_length = 100)
    PhoneNumberID = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):
        if self.AptSuite:
            return self.AptSuite + " " + self.Address + "(" + self.IdentifierTypeID.IdentifierType + ")"
        else:
            return self.Address + "(" + self.IdentifierTypeID.IdentifierType + ")"

class BusinessDiscountSchedule(models.Model):
    BusinessDiscountID = models.AutoField(primary_key = True)
    BusinessTier = models.CharField(max_length = 100)
    BusinessDiscountPercentage = models.DecimalField(max_digits=10, decimal_places=2)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.BusinessTier + "  (" + str(self.BusinessDiscountPercentage) + "%)"

class CustomerType(models.Model):
    CustomerType = models.CharField(max_length = 40)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.CustomerType

class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    DateCreated = models.DateField(auto_now_add=True)
    ModifedDate = models.DateField(auto_now=True)
    CustomerType = models.ForeignKey(CustomerType, on_delete=models.CASCADE, blank = True, null = True)
    CustomerRating = models.SmallIntegerField(blank=True, default = 3, validators=[MaxValueValidator(5), MinValueValidator(1)])
    CustomerNotes = models.TextField(default=None,blank=True)


    def __str__(self):
        return str(self.CustomerType) + " Rating: " + str(self.CustomerRating)


class Patron(models.Model):
    PatronID = models.AutoField(primary_key = True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    AddressID = models.ForeignKey(Address, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length = 100)
    LastName = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 100)

    def __str__(self):
        return self.FirstName + " " + self.LastName

class PatronPhoneNumbers(models.Model):
    PatronID = models.ForeignKey(Patron, on_delete=models.CASCADE)
    PhoneNumberID = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE)
    ModifedDate = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.PatronID) + " " + str(self.PhoneNumberID.PhoneNumberType)

class Business(models.Model):
    BusinessID = models.AutoField(primary_key = True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    AddressID = models.ForeignKey(Address, on_delete=models.CASCADE)
    BusinessDiscountID = models.ForeignKey(BusinessDiscountSchedule, on_delete=models.CASCADE, blank = True, null = True)
    BusinessName = models.CharField(max_length = 100)
    BusinessArea = models.CharField(max_length = 100)
    BusinessEmail = models.CharField(max_length = 100, blank = True)

    def __str__(self):
        return self.BusinessName

class BusinessContactRole(models.Model):
    BusinessContactRoleID = models.AutoField(primary_key = True)
    BusinessContactRole = models.CharField(max_length = 100)
    ModifedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.BusinessContactRole

class BusinessContact(models.Model):
    BusinessContactID = models.AutoField(primary_key = True)
    BusinessID = models.ForeignKey(Business, on_delete=models.CASCADE)
    PhoneNumberID = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE)
    BusinessContactRoleID = models.ForeignKey(BusinessContactRole, on_delete=models.CASCADE)
    FirstName = models.CharField(max_length = 100)
    LastName = models.CharField(max_length = 100)
    Email = models.CharField(max_length = 100)
    PrimaryContact = models.CharField(max_length = 3, choices = YN, default= 'N')

    def __str__(self):
        return self.FirstName + " " + self.LastName