from django.db import models

# Create your models here.
class HQ(models.Model):
    HQname = models.CharField(max_length = 100)
    Address = models.CharField(max_length = 100)
    City = models.CharField(max_length = 100)
    Province = models.CharField(max_length = 100)
    PostalCode = models.CharField(max_length = 100)
    PhoneNumber = models.CharField(max_length = 100)
    EmailAddress = models.CharField(max_length = 100)
    # foreign key to employee id for CEO
    CEOID = models.ForeignKey('Employee', on_delete=models.CASCADE)

    def __str__(self):
        return self.HQname


class Store(models.Model):
    StoreID = models.AutoField(primary_key=True)
    StoreName = models.CharField(max_length = 100)
    Address = models.CharField(max_length = 100)
    City = models.CharField(max_length = 100)
    Province = models.CharField(max_length = 100)
    PostalCode = models.CharField(max_length = 100)
    PhoneNumber = models.CharField(max_length = 100)
    NumberExt = models.CharField(max_length = 100)
    # fk manager
    ManagerID = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='manager')
    # fk ass man
    AssistantManagerID = models.ForeignKey('Employee', on_delete=models.CASCADE, blank=True, default=None, null=True, related_name='assmanager')

    def __str__(self):
        return self.StoreName + " (#" + str(self.StoreID) + ")"

class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key = True)
    StoreID = models.ForeignKey('Store', on_delete=models.CASCADE, blank=True, default=None, null=True)
    PositionID = models.ForeignKey('EmployeeRole', on_delete=models.CASCADE)
    FirstName = models.CharField(max_length = 100)
    LastName = models.CharField(max_length = 100)
    EmployeeEmail = models.CharField(max_length = 100, blank=True, default=None)
    EmployeePhoneNum = models.CharField(max_length = 100, blank=True, default=None)

    def __str__(self):
        return self.FirstName + " " + self.LastName + " (" + self.PositionID.PositionName + ")"


class EmployeeRole(models.Model):
    PositionID = models.AutoField(primary_key=True)
    PositionName = models.CharField(max_length = 100)

    def __str__(self):
        return "(" + str(self.PositionID) + ") " + self.PositionName