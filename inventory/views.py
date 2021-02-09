from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    inventory = Inventory.objects.all()
    context = {'tool_list' : inventory }
    return render(request, 'inventory/index.html', context)



