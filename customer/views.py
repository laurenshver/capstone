from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from customer.models import *
from order.models import Order
from django.views.generic.detail import DetailView

# Create your views here.

# get all patrons and the necessary information (NAme, Postal Code, Rating)
def patrons(request):
    patron_list = Patron.objects.all()
    context = {'patrons' : patron_list}
    return render(request, 'customer/patron.html', context)

# get all details about patron at kwarg pk
class PatronDetailView(DetailView):
    model = Patron
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['phone_numbers'] = PatronPhoneNumbers.objects.all().filter(PatronID=self.kwargs['pk'])
        p = Patron.objects.get(PatronID=self.kwargs['pk'])
        context['orders'] = Order.objects.all().filter(CustomerID_id = p.CustomerID_id)
        return context


def businesses(request):
    business_list = Business.objects.all()
    context = {'businesses' : business_list}
    return render(request, 'customer/business.html', context)


class BusinessDetailView(DetailView):
    model = Business
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['contacts'] = BusinessContact.objects.all().filter(BusinessID=self.kwargs['pk'])
        b = Business.objects.get(BusinessID = self.kwargs['pk'])
        context['orders'] = Order.objects.all().filter(CustomerID_id = b.CustomerID_id)
        return context