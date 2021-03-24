from django.shortcuts import render
from django.http import HttpResponse
from order.models import *
from customer.models import Patron, Business
from inventory.models import Tool
from django.views.generic.detail import DetailView
# Create your views here.

def index(request):
    context = {}
    orders = Order.objects.all()
    context['orders'] = orders
    context['patron'] = Patron.objects.all()
    context['business'] = Business.objects.all()
    return render(request, 'order/order_summary.html', context)

class OrderDetailView(DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['ordertool'] = OrderTool.objects.filter(OrderID_id = self.kwargs['pk'])
        return context
