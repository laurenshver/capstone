from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(InvoiceOrder)
admin.site.register(Invoice)
admin.site.register(InvoiceStatus)
admin.site.register(PaymentMethod)
admin.site.register(Payment)