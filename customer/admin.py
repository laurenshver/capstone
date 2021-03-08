from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(CustomerType)
admin.site.register(BusinessDiscountSchedule)
admin.site.register(Address)
admin.site.register(IdentifierType)
admin.site.register(PhoneNumber)
admin.site.register(PhoneNumberType)
admin.site.register(Province)
admin.site.register(Patron)
admin.site.register(PatronPhoneNumbers)
admin.site.register(Business)
admin.site.register(BusinessContact)
admin.site.register(BusinessContactRole)