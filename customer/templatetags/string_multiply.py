from django.template import Library
from customer.models import PatronPhoneNumbers, BusinessContact
register = Library()

@register.filter
def multiply(string, times):
    times = int(times)
    return string * times

@register.filter
def unchecked(string, times):
    times = int(times)
    return string  * (5-times)

@register.filter
def get_num(patron):
    x = PatronPhoneNumbers.objects.get(PatronID_id = patron, PhoneNumberID_id__PhoneNumberType = 2)
    return x.PhoneNumberID.PhoneNumber

@register.filter
def primarycontact(business):
    return BusinessContact.objects.get(BusinessID_id = business, PrimaryContact = "Y")

@register.filter
def primarycontact_number(business):
    x =  BusinessContact.objects.get(BusinessID_id = business, PrimaryContact = "Y")
    return x.PhoneNumberID.PhoneNumber

@register.filter
def primarycontact_role(business):
    x =  BusinessContact.objects.get(BusinessID_id = business, PrimaryContact = "Y")
    return x.BusinessContactRoleID.BusinessContactRole