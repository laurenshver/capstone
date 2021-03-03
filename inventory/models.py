from django.db import models
from retail.models import Store
from django.utils.timezone import now

# Create your models here.
YN = (
        ('Y', 'YES'),
        ('N', 'NO'),
)

class ToolCategory(models.Model):
    ToolCategory = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.ToolCategory

class ToolSubCategory(models.Model):
    ToolCategoryID = models.ForeignKey(ToolCategory, on_delete=models.CASCADE)
    ToolSubCategory = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.ToolSubCategory

class ToolStatus(models.Model):
    ToolStatus = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.ToolStatus

class ToolCondition(models.Model):
    ToolCondition = models.CharField(max_length = 100)
    ToolConditionDescription = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)   

    def __str__(self):
        return self.ToolCondition

class PriceRate(models.Model):
    PriceRate = models.CharField(max_length = 100)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.PriceRate

class Tool(models.Model):
    ToolID = models.AutoField(primary_key=True)
    ToolCategoryID = models.ForeignKey(ToolCategory, on_delete=models.CASCADE)
    ToolSubCategoryID = models.ForeignKey(ToolSubCategory, on_delete=models.CASCADE)
    DateCreated = models.DateField(auto_now_add=True)
    ToolName = models.CharField(max_length = 100)
    ToolBrand = models.CharField(max_length = 100)
    ToolPicture = models.ImageField(null=True, blank=True)
    ItemDescription = models.TextField(blank = True, default= "")
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.ToolName + " (" + self.ToolBrand + ")"


class Inventory(models.Model):
    InventoryID = models.AutoField(primary_key = True)
    StoreID = models.ForeignKey(Store, on_delete=models.CASCADE)
    ToolID = models.ForeignKey(Tool, on_delete=models.CASCADE)
    ToolStatusID = models.ForeignKey(ToolStatus, on_delete=models.CASCADE)
    ToolConditionID = models.ForeignKey(ToolCondition, on_delete=models.CASCADE, null=True, blank=True)
    DateCreated = models.DateField(default = now, editable = False)
    TimesRented = models.SmallIntegerField(default=0)
    Decomissioned = models.CharField(max_length = 10, choices = YN, default = 'N', null=True, blank=True)
    DateDecomissioned = models.DateField(blank = True, null = True)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return self.ToolID.ToolName + " #" + self.InventoryID
    

class ToolPrice(models.Model):
    ToolID = models.ForeignKey(Tool, on_delete=models.CASCADE)
    PriceRateID = models.ForeignKey(PriceRate, on_delete=models.CASCADE)
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    StartDate = models.DateField(auto_now=True)
    EndDate = models.DateField(blank = True, null = True)
    ModifiedDate = models.DateField(auto_now=True)

    def __str__(self):
        return "$" + str(self.Price) + " " + self.PriceRateID.PriceRate


