from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    inventory = Inventory.objects.all()
    context = {'inventory_list' : inventory }
    return render(request, 'inventory/index.html', context)

def create_tool(request):
    x = InventoryForm()
    return render(request, 'inventory/create_tool.html', {'form':x})

