from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from customer.models import *

# Create your views here.
def all_customers(request):
    # sends customer list to index.html
    # objects.raw() can be used to write SQL queries :D
    customer_list = Customer.objects.all()
    context = {'customer_list' : customer_list }
    return render(request, 'customer/index.html', context)

def patrons(request):
    patron_list = Patron.objects.raw("SELECT PatronID, FirstName, LastName, PhoneNumber, PhoneNumbreType, PostalCode, CustomerRating FROM customer_patron JOIN customer_patronphonenumbers on customer_patron.PatronID = customer_patronphonenumbers.PatronID_id JOIN customer_phonenumber on customer_patronphonenumbers.PhoneNumberID_id = customer_phonenumber.PhoneNumberID JOIN customer_address on customer_address.AddressID = customer_patron.AddressID_id JOIN customer_customer ON customer_customer.CustomerID = customer_patron.CustomerID_id WHERE customer_phonenumber.PhoneNumbreType = 'C'")
    # Patron.objects.prefetch_related('CustomerID', 'AddressID')
    # print(patron_list)
    context = {'patrons' : patron_list}
    return render(request, 'customer/patron.html', context)