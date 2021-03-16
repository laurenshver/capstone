from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def retail_index(request):
    return render(request, 'retail/retail.html')
# homepage. do not change.
def index(request):
    return render(request, 'retail/index.html')