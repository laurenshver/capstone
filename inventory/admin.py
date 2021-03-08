from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Inventory)
admin.site.register(Tool)
admin.site.register(ToolCondition)
admin.site.register(ToolCategory)
admin.site.register(ToolSubCategory)
admin.site.register(ToolPrice)
admin.site.register(ToolStatus)
admin.site.register(PriceRate)
admin.site.register(ToolPowerType)