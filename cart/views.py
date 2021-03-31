from django.shortcuts import render, redirect
from inventory.models import Inventory, ToolPrice, PriceRate, Tool, ToolStatus
from customer.models import *
from retail.models import Store, Employee
from order.models import *
from cart.cart import get_start_date, get_start_time, get_end_date, get_end_time, start_date_and_time, end_date_and_time
import datetime
from cart.templatetags.cartfilters import elstdate, latestdate

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

def remove_from_cart(request, key):
    del request.session['cart'][key]
    request.session.save()
    return redirect(cart)

def assign_customer_to_order(request):
    context = {}
    context['customers'] = Customer.objects.all()
    context['patrons'] = Patron.objects.all()
    context['businesses'] = Business.objects.all()
    context['businesscontact'] = BusinessContact.objects.all()
    context['patronnumbers'] = PatronPhoneNumbers.objects.all()

    if request.method == 'POST':
        request.session['subtotal'] = request.POST['hidden-subtotal']

    return render(request, "cart/select_customer.html", context)


def select_customer(request, custID, rating, type, name, contact, identifier):
    # if customer variable in session exists
    request.session['customer'] = {
        'id': custID,
        'rating': rating,
        'type' : type,
        'name' : name,
        'contact' : contact,
        'identifier' : identifier,
    }
    request.session.save()
    return redirect(assign_customer_to_order)

def delete_customer_session(request):
    del request.session['customer']
    request.session.save()
    return redirect(assign_customer_to_order)

def procurement(request):
    stores = []
    start_dates = []
    end_dates = []
    start_times = []
    end_times = []
    if request.session['customer']['type'] == 'Patron':
        patron_details = Patron.objects.get(CustomerID_id = int(request.session['customer']['id']))
        context = {'customer' : patron_details}
    else:
        business_details = Business.objects.get(CustomerID_id = int(request.session['customer']['id']))
        context = {'customer' : business_details}
    
    for item in request.session['cart']:
        stores.append(request.session['cart'][item]['store'])
        start_dates.append(request.session['cart'][item]['startdate'])
        start_times.append(request.session['cart'][item]['starttime'])
        end_dates.append(request.session['cart'][item]['enddate'])
        end_times.append(request.session['cart'][item]['endtime'])
        
    context['pickup'] = Store.objects.filter(StoreID__in = set(stores))
    context['sdate'] = start_dates
    context['edate'] = end_dates
    
    request.session['startdates'] = start_dates
    request.session['enddates'] = end_dates
    request.session.save()


    return render(request, 'cart/order_procurement.html', context)

def review_order(request):
    # print(request.POST)
    context = {}
    if request.method == 'POST':
        # save order costs to session
        z = {
            'subtotal' : request.POST.get('hidden-subtotal'),
            'taxes' : request.POST.get('hidden-taxes'),
            'deposit' : request.POST.get('hidden-deposit'),
            'total' : request.POST.get('hidden-total'),
        }
        if request.session['customer']['type'] == 'Business':
            z['discount'] = request.POST.get('hidden-businessdiscount')

        request.session['costs'] = z
        

        # save procurement to session
        if request.POST.get('tool-retrival') == 'pickup':
            p = {
                'type': request.POST.get('tool-retrival'),
                'pickup-location' : int(request.POST.get('pickup-location')),
            }
            request.session['procurement'] = p
        
        if (request.POST.get('tool-retrival') == 'delivery') and (request.POST.get('customer-address')):
            p = {
                'type': request.POST.get('tool-retrival'),
                'custaddress' : 'customer address',
            }
            request.session['procurement'] = p

        if (request.POST.get('tool-retrival') == 'delivery') and (request.POST.get('customer-address') == None):
            p = {
                'type': request.POST.get('tool-retrival'),
                'address' : request.POST.getlist('address'),
            }
            request.session['procurement'] = p
        request.session.save()

    # adding view context
    if request.session['customer']['type'] == 'Business':
        business_details = Business.objects.get(CustomerID_id = int(request.session['customer']['id']))
        context = {'customer' : business_details}
    else:
        patron_details = Patron.objects.get(CustomerID_id = int(request.session['customer']['id']))
        context = {'customer' : patron_details}
    
    if request.session['procurement']['type'] == 'pickup':
        store_address = Store.objects.get(StoreID = request.session['procurement']['pickup-location'])
        context['pickupaddress'] = store_address

    context['inventory'] = Inventory.objects.all()
    context['prices'] = ToolPrice.objects.all()
    
    return render(request, 'cart/complete_order.html', context)



def create_new_order(request):

    # create a cost object
    if 'discount' in request.session['costs']:
        order_costs = Cost.objects.create(
            Total= float(request.session['costs']['total']),
            Subtotal = float(request.session['costs']['subtotal']),
            Taxes = float(request.session['costs']['taxes']),
            BusinessDiscount = float(request.session['costs']['discount']),
        )
    else:
        order_costs = Cost.objects.create(
            Total= float(request.session['costs']['total']),
            Subtotal = float(request.session['costs']['subtotal']),
            Taxes = float(request.session['costs']['taxes']),
            Deposit = float(request.session['costs']['deposit']),
        )

    # if delivery to new address, create new address, otherwise, use address already on file
    if (request.session['procurement']['type'] == 'delivery') and ('address' in request.session['procurement']):
        # print(request.session['procurement']['address'])
        address = Address.objects.create(
            IdentifierTypeID = IdentifierType.objects.get(IdentifierType = 'Shipping'),
            AptSuite = request.session['procurement']['address'][0],
            Address = request.session['procurement']['address'][1],
            City = request.session['procurement']['address'][2],
            Country = 'Canada',
            ProvinceID = Province.objects.get(ProvinceShortName = request.session['procurement']['address'][3]),
            PostalCode = request.session['procurement']['address'][4]
        )

    # if delivering to customer address, get the customer address object
    if (request.session['procurement']['type'] == 'delivery') and ('custaddress' in request.session['procurement']):
        if request.session['customer']['type'] == 'Business':
            addressid = Business.objects.filter(CustomerID = request.session['customer']['id']).values('AddressID_id')
            address = Address.objects.get(AddressID = addressid[0]['AddressID_id'])
        else:
            addressid = Patron.objects.filter(CustomerID = request.session['customer']['id']).values('AddressID_id')
            address = Address.objects.get(AddressID = addressid[0]['AddressID_id'])

    
    if request.session['procurement']['type'] == 'pickup':
        addressid = Store.objects.filter(StoreID = request.session['procurement']['pickup-location']).values('AddressID_id')
        address = Address.objects.get(AddressID = addressid[0]['AddressID_id'])

    # get customer object
    customer = Customer.objects.get(CustomerID = request.session['customer']['id'])
    # get employee object
    employee = Employee.objects.get(EmployeeID = 2)

    # create new order
    order = Order.objects.create(
        CustomerID = customer,
        EmployeeID = employee,
        AddressID = address,
        CostID = order_costs,
        OrderStatusID = OrderStatus.objects.get(OrderStatus = 'Accepted'),
        ToolRetreival = ToolRetreival.objects.get(ToolRetreival = request.session['procurement']['type'].title()),
        StartDate = start_date_and_time(elstdate(request.session['startdates'])),
        EstimatedEndDate = end_date_and_time(latestdate(request.session['enddates'])),
        TandCAccepted = 'Y',
        OrderNotes = request.POST.get('ordernotes'),
    )

    for item in request.session['cart'].keys():
        tool = Inventory.objects.filter(InventoryID = request.session['cart'][item]['item']).values('ToolID_id')
        price = ToolPrice.objects.get(ToolID = tool[0]['ToolID_id'], PriceRateID__PriceRate = request.session['cart'][item]['rate'].title())

        # create an order tool record for all tools in the order
        OrderTool.objects.create(
            OrderID = order,
            InventoryID = Inventory.objects.get(InventoryID = item),
            ToolPriceID = price,
            StartDate = start_date_and_time(datetime.datetime.strptime(request.session['cart'][item]['startdate'], "%b. %d %Y")),
            EndDate = end_date_and_time( datetime.datetime.strptime(request.session['cart'][item]['enddate'], "%b. %d %Y")),
            RentalLength = request.session['cart'][item]['rentallength'],
        )

        # set inventory status to 'Rented'
        i = Inventory.objects.get(InventoryID = request.session['cart'][item]['item'])
        i.ToolStatusID = ToolStatus.objects.get(ToolStatus = 'Rented')
        i.save()

    # create order delivery/pickup object
    if request.session['procurement']['type'] == 'delivery':
        OrderDelivery.objects.create(
            OrderID = order,
            EmployeeID = employee,
            DeliveryStatusID = DeliveryStatus.objects.get(id = 2)
        )

    if request.session['procurement']['type'] == 'pickup':
        OrderPickup.objects.create(
            OrderID = order,
            EmployeeID = employee,
            PickupStatusID = PickupStatus.objects.get(id = 2)
        )


    del request.session['costs']
    del request.session['cart']
    del request.session['procurement']
    del request.session['customer']
    del request.session['subtotal']
    del request.session['startdates']
    del request.session['enddates']

    request.session.save()

    return redirect(order_placed, pk=order.pk)


def order_placed(request, pk):
    order = Order.objects.get(OrderID = pk)
    context = {'order' : order }
    custid = order.CustomerID_id
    cust = Customer.objects.get(CustomerID = custid)
    if cust.CustomerType.CustomerType == 'Patron':
        customer = Patron.objects.get(CustomerID_id = custid)
        context['customer'] = customer
    else:
        customer = Business.objects.get(CustomerID_id = custid)
        context['customer'] = customer


    
    
    return render(request, 'cart/order_placed.html', context)