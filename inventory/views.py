from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse, request
from django.template import loader
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from .models import *
from cart.forms import AddCartForm

# Create your views here.
def toolcatalogue(request):
    inventory = Tool.objects.all()
    context = {'tool_list' : inventory }
    context['categories'] = ToolCategory.objects.distinct()
    context['subcategories'] = ToolSubCategory.objects.distinct()
    return render(request, 'inventory/toolcatalogue.html', context)

class ToolDetailView(DetailView):
    model = Tool

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['inventory'] = Inventory.objects.filter(ToolID = self.kwargs['pk']).prefetch_related('ToolConditionID', 'ToolStatusID')
        context['prices'] = ToolPrice.objects.filter(ToolID = self.kwargs['pk']).prefetch_related('ToolID', 'PriceRateID')
        return context


