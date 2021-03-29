from django.template import Library
from django.db.models import Sum
from customer.models import Patron, Business, Customer, PatronPhoneNumbers, PhoneNumber, BusinessContact
from order.models import Order
from datetime import timedelta, datetime

register = Library()

@register.filter
def customer_name(custid, custtype):
    if custtype == 'Patron':
        return Patron.objects.get(CustomerID_id = int(custid))
    else:
        return Business.objects.get(CustomerID_id = int(custid))


@register.filter
def selected_customer_name(custid):
    q = Customer.objects.get(CustomerID = int(custid)).CustomerType_id
    if q == 1:
        return Patron.objects.get(CustomerID_id = int(custid))
    else:
        return Business.objects.get(CustomerID_id = int(custid))

@register.filter
def selected_order_object(key):
    return Order.objects.filter(OrderID = key)

@register.simple_tag
def expiry():
    '''calculate the invoice expiry date, which is 30 days from the incoice creation'''
    today = datetime.now()
    expiry_date = today + timedelta(days = 30)
    return expiry_date
    
@register.filter
def subtotal(session):
    k = session['orders'].keys()
    # filter orders by first selected customer
    customer = session['orders'][list(k)[0]].get('cust')
    # exclude orders already selected
    o = list(session['orders'].keys())
    orders = Order.objects.filter(CustomerID_id = customer).filter(OrderID__in = o).aggregate(Sum('CostID_id__Subtotal'))
    # return orders[1].CostID.Subtotal
    return '{:0.2f}'.format(orders['CostID_id__Subtotal__sum'])

@register.filter
def taxes(session):
    k = session['orders'].keys()
    # filter orders by first selected customer
    customer = session['orders'][list(k)[0]].get('cust')
    # exclude orders already selected
    o = list(session['orders'].keys())
    orders = Order.objects.filter(CustomerID_id = customer).filter(OrderID__in = o).aggregate(Sum('CostID_id__Taxes'))
    # return orders[1].CostID.taxes
    return '{:0.2f}'.format(orders['CostID_id__Taxes__sum'])

@register.filter
def deposit(session):
    k = session['orders'].keys()
    # filter orders by first selected customer
    customer = session['orders'][list(k)[0]].get('cust')
    # exclude orders already selected
    o = list(session['orders'].keys())
    orders = Order.objects.filter(CustomerID_id = customer).filter(OrderID__in = o).aggregate(Sum('CostID_id__Deposit'))
    # return orders[1].CostID.deposit
    return '{:0.2f}'.format(orders['CostID_id__Deposit__sum'])

@register.filter
def discount(session):
    k = session['orders'].keys()
    # filter orders by first selected customer
    customer = session['orders'][list(k)[0]].get('cust')
    # exclude orders already selected
    o = list(session['orders'].keys())
    orders = Order.objects.filter(CustomerID_id = customer).filter(OrderID__in = o).aggregate(Sum('CostID_id__BusinessDiscount'))
    # return orders[1].CostID.deposit
    return '{:0.2f}'.format(orders['CostID_id__BusinessDiscount__sum'])

@register.filter
def total(session):
    k = session['orders'].keys()
    # filter orders by first selected customer
    customer = session['orders'][list(k)[0]].get('cust')
    # exclude orders already selected
    o = list(session['orders'].keys())
    orders = Order.objects.filter(CustomerID_id = customer).filter(OrderID__in = o).aggregate(Sum('CostID_id__Total'))
    # return orders[1].CostID.deposit
    return '{:0.2f}'.format(orders['CostID_id__Total__sum'])

@register.filter
def cust_type(session):
    k = session['orders'].keys()
    customer = session['orders'][list(k)[0]].get('cust')
    c = Customer.objects.filter(CustomerID = customer)
    return c[0].CustomerType.CustomerType

@register.filter
def days_till_due(duedate):
    today = datetime.now().date()
    duedate = datetime.strptime(duedate, "%B %d, %Y").date()
    return (duedate - today).days

@register.filter
def customer_phonenumber(custid):
    q = Customer.objects.get(CustomerID = int(custid)).CustomerType_id
    if q == 1:
        id =  Patron.objects.get(CustomerID_id = int(custid)).PatronID
        qs = PatronPhoneNumbers.objects.filter(PatronID_id = id, PhoneNumberID_id__PhoneNumberType = 2)
        x = qs[0].PhoneNumberID_id
        return PhoneNumber.objects.get(PhoneNumberID = x).PhoneNumber
    else:
        bid = Business.objects.get(CustomerID_id = int(custid)).BusinessID
        x = BusinessContact.objects.get(BusinessID_id = bid, PrimaryContact = 'Y')
        pid = x.PhoneNumberID_id
        return PhoneNumber.objects.get(PhoneNumberID = pid).PhoneNumber
