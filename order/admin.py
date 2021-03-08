from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderTool)
admin.site.register(ExtraFeeSchedule)
admin.site.register(TaxCode)
admin.site.register(OrderDelivery)
admin.site.register(DeliveryStatus)
admin.site.register(OrderPickup)
admin.site.register(PickupStatus)
admin.site.register(Cost)
admin.site.register(OrderStatus)
admin.site.register(ToolRetreival)