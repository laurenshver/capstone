from django.db import models
from customer.models import Address, PhoneNumber

# Create your models here.
class HQ(models.Model):
    AddressID = models.ForeignKey(Address, on_delete=models.CASCADE, blank = True, null = True)
    HQname = models.CharField(max_length = 100)
    PhoneNumberID = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, blank = True, null = True)
    EmailAddress = models.CharField(max_length = 100)
    # foreign key to employee id for CEO
    CEOID = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.HQname


class Store(models.Model):
    StoreID = models.AutoField(primary_key=True)
    AddressID = models.ForeignKey(Address, on_delete=models.CASCADE, blank = True, null = True)
    StoreName = models.CharField(max_length = 100)
    PhoneNumberID = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.StoreName + " (#" + str(self.StoreID) + ")"

class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key = True)
    StoreID = models.ForeignKey('Store', on_delete=models.CASCADE, blank=True, default=None, null=True)
    PositionID = models.ForeignKey('EmployeeRole', on_delete=models.CASCADE)
    FirstName = models.CharField(max_length = 100)
    LastName = models.CharField(max_length = 100)
    EmployeeEmail = models.CharField(max_length = 100, blank=True)
    PhoneNumberID = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, blank = True, null = True)

    def __str__(self):
        return self.FirstName + " " + self.LastName + " (" + self.PositionID.PositionName + ")"  

class EmployeeRole(models.Model):
    PositionID = models.AutoField(primary_key=True)
    PositionName = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True, blank = True, null = True)

    def __str__(self):
        return "(" + str(self.PositionID) + ") " + self.PositionName