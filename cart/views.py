from django.shortcuts import render
from inventory.models import Inventory, ToolPrice
from cart.cart import get_start_date, get_start_time, get_end_date, get_end_time

# Create your views here.
def cart(request):
    items = []
    stores = []
    context = {}
    
    context['inventory'] = Inventory.objects.all()
    context['prices'] = ToolPrice.objects.all()
    # del request.session['cart']

    if request.method == 'POST':
        # split the store name and the inventory id string from POST
        for x in request.POST.getlist('item'):
            items.append(x.split("&&~~")[0])
            stores.append(x.split("&&~~")[1])
        rate = request.POST.getlist('rate') * len(request.POST.getlist('item'))
        start = request.POST.getlist('start') * len(request.POST.getlist('item'))
        startdate = get_start_date(start)
        starttime = get_start_time(start, rate)
        rentallength = request.POST.getlist('rlength') * len(request.POST.getlist('item'))
        enddate = get_end_date(start, rate, rentallength)
        endtime = get_end_time(start, rate, rentallength)
        
        
        for x in range(len(items)):
            d = {
            'item': items[x],
            'store': stores[x],
            'rate' : rate[x],
            'startdate' : startdate[x],
            'starttime' : starttime[x],
            'enddate' : enddate[x],
            'endtime' : endtime[x],
            'rentallength': rentallength[x],
            }
            
            if 'cart' in request.session:
                # if cart session exists

                # dont add tools more than once
                request.session['cart'][str(items[x])] = d
                request.session.save()
            else:
                # if cart session doesn't exist
                request.session['cart'] = {}
                request.session['cart'][str(items[x])] = d
                request.session.save()
    
    return render(request, "cart/cart.html", context)
