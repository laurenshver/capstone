from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from customer.models import *
from django.views.generic.detail import DetailView

# Create your views here.

# get all patrons and the necessary information (NAme, Postal Code, Rating)
def patrons(request):
    patron_list = Patron.objects.raw("SELECT PatronID, FirstName, LastName, PostalCode, CustomerRating, PhoneNumber, PhoneNumberType FROM customer_patron JOIN customer_address ON customer_address.AddressID = customer_patron.AddressID_id JOIN customer_customer ON customer_customer.CustomerID = customer_patron.CustomerID_id JOIN customer_patronphonenumbers ON customer_patronphonenumbers.PatronID_id = customer_patron.PatronID JOIN customer_phonenumber ON customer_phonenumber.PhoneNumberID = customer_patronphonenumbers.PhoneNumberID_id JOIN customer_phonenumbertype ON customer_phonenumbertype.id = customer_phonenumber.PhoneNumberType_id WHERE PhoneNumberType = 'Cell Phone'")
    # Patron.objects.prefetch_related('CustomerID', 'AddressID')
    # print(patron_list)
    context = {'patrons' : patron_list}
    return render(request, 'customer/patron.html', context)

# get all details about patron at kwarg pk
class PatronDetailView(DetailView):
    model = Patron
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['phone_numbers'] = PatronPhoneNumbers.objects.all().filter(PatronID=self.kwargs['pk'])
        return context


def businesses(request):
    business_list = Business.objects.raw("SELECT BusinessID, BusinessName, FirstName, LastName, BusinessContactRole, PhoneNumber, Extension, CustomerRating FROM customer_business LEFT JOIN customer_businesscontact ON customer_business.BusinessID = customer_businesscontact.BusinessID_id Join customer_customer ON customer_business.CustomerID_id = customer_customer.CustomerID LEFT JOIN customer_businesscontactrole ON customer_businesscontact.BusinessContactRoleID_id = customer_businesscontactrole.BusinessContactRoleID JOIN customer_phonenumber ON customer_phonenumber.PhoneNumberID = customer_businesscontact.PhoneNumberID_id WHERE PrimaryContact = 'Y' GROUP BY BusinessID")
    context = {'businesses' : business_list}
    return render(request, 'customer/business.html', context)


class BusinessDetailView(DetailView):
    model = Business
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['contacts'] = BusinessContact.objects.all().filter(BusinessID=self.kwargs['pk'])
        return context