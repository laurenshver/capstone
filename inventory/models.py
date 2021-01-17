from django.db import models
from retail.models import Store
from django.forms import ModelForm

# Create your models here.
class Inventory(models.Model):
    TOOL_CONDITIONS = (
        ('G', 'GOOD'),
        ('DR', 'DAMAGE/REPAIR'),
        ('D', 'DAMAGED'),
    )
    DECOMISSIONED = (
        ('Y', 'YES'),
        ('N', 'NO'),
    )
    TOOL_CATEGORIES = (
        ('1', 'Shovels, Picks, Long Handled Tools'),
        ('2', 'HVAC Equipment'),
        ('3', 'Concrete and Masonry Equipment'),
        ('4', 'Drilling and Drilling Accessories'),
        ('5', 'Floor Care and Sanding'),
        ('6', 'Scaffolding'),
        ('7', 'Other')
    )

    TOOL_SUB_CATEGORIES = (
        ('1.1', 'Rental Bars'),
        ('1.2', 'Forks and Rakes'),
        ('1.3', 'Picks and Handles'),
        ('2.1', 'Dehumidifiers'),
        ('2.2', 'Heaters'),
        ('3.1', 'Concrete Grinders and Surface Prep'),
        ('3.2', 'Sawing and Drilling Equipment'),
        ('4.1', 'Drill Bit Sets'),
        ('4.2', 'Annular Cutting Sets'),
        ('5.1', 'Sanders & Edgers'),
        ('5.2', 'Polishers'),
        ('5.3', 'Grinders'),
        ('6.1', 'Scafolding Towers'),
        ('7.1', 'Other'),
    )
    ToolID = models.AutoField(primary_key=True)
    # store ID FK
    StoreID = models.ForeignKey(Store, on_delete=models.CASCADE)
    ToolName = models.CharField(max_length = 100)
    ToolBrand = models.CharField(max_length = 100)
    ToolCategory = models.CharField(max_length = 100, choices = TOOL_CATEGORIES)
    ToolSubCategory = models.CharField(max_length = 100, choices = TOOL_SUB_CATEGORIES)
    ToolDescription = models.TextField(blank = True, default= "")
    HourlyPrice = models.DecimalField(max_digits=10, decimal_places=2)
    DailyPrice = models.DecimalField(max_digits=10, decimal_places=2)
    WeeklyPrice = models.DecimalField(max_digits=10, decimal_places=2)
    MonthlyPrice = models.DecimalField(max_digits=10, decimal_places=2)
    HourlyOverduePrice = models.DecimalField(max_digits=10, decimal_places=2)
    DailyOverduePrice = models.DecimalField(max_digits=10, decimal_places=2)
    WeeklyOverduePrice = models.DecimalField(max_digits=10, decimal_places=2)
    MonthlyOverduePrice = models.DecimalField(max_digits=10, decimal_places=2)
    PictureURL = models.CharField(max_length = 100, blank=True)
    NumToolInInventory = models.PositiveSmallIntegerField()
    NumToolAvailable = models.PositiveSmallIntegerField()
    TimesRented = models.PositiveSmallIntegerField(default=0)
    ConditionRating = models.CharField(max_length = 100, default='G', choices = TOOL_CONDITIONS)
    Decomissioned = models.CharField(max_length = 100, default='N', choices = DECOMISSIONED)

    def __str__(self):
        return self.ToolName + " (" + self.ToolBrand + ")"

class InventoryForm(ModelForm):
    class Meta:
        model = Inventory
        exclude = ['PictureURL']
        labels = {
            'StoreID' : 'Store Name',
            'ToolName' : 'Tool Name',
        }

