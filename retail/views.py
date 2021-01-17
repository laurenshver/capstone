from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def index(request):
    employee_list = Employee.objects.all()
    context = {'employee_list' : employee_list }
    return render(request, 'retail/index.html', context)