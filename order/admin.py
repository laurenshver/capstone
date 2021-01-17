from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CustomerOrder)
admin.site.register(CustomerOrderTool)
admin.site.register(BusinessOrder)
admin.site.register(BusinessOrderTool)
admin.site.register(ExtraFeeSchedule)