from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Customer

# Create your views here.
def all_customers(request):
    # sends customer list to index.html
    # objects.raw() can be used to write SQL queries :D
    customer_list = Customer.objects.all()
    context = {'customer_list' : customer_list }
    return render(request, 'customer/index.html', context)