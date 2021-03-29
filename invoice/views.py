from django.shortcuts import render, redirect
from django.http import HttpResponse
from order.models import Order, Cost
from invoice.models import Invoice, InvoiceOrder, InvoiceStatus, Payment
from invoice.invoice import invoice_expiry
from customer.models import Customer, Patron, Business
# Create your views here.

def index(request):
    invoices = Invoice.objects.all()
    context = {'invoices' : invoices}
    return render(request, 'invoice/index.html', context)

def select_order(request):
    context = {}
    invoiced = list(InvoiceOrder.objects.values_list('OrderID_id', flat = True))
    # if orders session variable exists
    if 'orders' in request.session:
        k = request.session['orders'].keys()
        # filter orders by first selected customer
        customer = request.session['orders'][list(k)[0]].get('cust')
        # exclude orders already selected
        exclude = list(request.session['orders'].keys())
        context['orders'] = Order.objects.filter(CustomerID_id = customer).exclude(OrderID__in = exclude + invoiced)
    else:
        context['orders'] = Order.objects.all().order_by('CustomerID_id').exclude(OrderID__in = invoiced)
    return render(request, 'invoice/select_order.html', context)

def add_to_invoice(request, oid, cid):
    d = {
        'order' : int(oid),
        'cust' : int(cid),
    }

    # if orders session variable exists
    if 'orders' in request.session:
        request.session['orders'][int(oid)] = d
    else:
        # create orders session variable as blank dict
        request.session['orders'] = {}
        # add d at key of order id
        request.session['orders'][int(oid)] = d

    request.session.save()

    return redirect(select_order)

def remove_from_invoice(request, oid):
    del request.session['orders'][oid]
    
    # delete orders variable if empty
    if not request.session['orders']:
        del request.session['orders']
        
    request.session.save()
    return redirect(select_order)

def generate_invoice(request):
    if request.method == 'POST':
        if request.POST.get('discount'):
            # if the business discount is sent via POST
            cost = Cost.objects.create(
                Total = request.POST.get('total'),
                Subtotal = request.POST.get('subtotal'),
                Taxes = request.POST.get('taxes'),
                BusinessDiscount = request.POST.get('discount'),
                Deposit = request.POST.get('deposit'),
            )
        else:
            cost = Cost.objects.create(
                Total = request.POST.get('total'),
                Subtotal = request.POST.get('subtotal'),
                Taxes = request.POST.get('taxes'),
                Deposit = request.POST.get('deposit'),
            )
        
        status = InvoiceStatus.objects.get(InvoiceStatus = 'Sent')
        cust = request.session['orders'][list(request.session['orders'].keys())[0]].get('cust')
        customer = Customer.objects.get(CustomerID = cust)

        # create invoice record
        invoice = Invoice.objects.create(
            CostID = cost,
            InvoiceStatusID = status,
            CustomerID = customer,
            DueDate = invoice_expiry(),
            DepositPaid = 'N',
            DepositRefunded =  'N',
            OverdueCharges = 'N'
        )

        # cretae invoice orders records
        for order in request.session['orders'].keys():
            InvoiceOrder.objects.create(
                InvoiceID = invoice,
                OrderID = Order.objects.get(OrderID = order),
            )

    del request.session['orders']
    request.session.save()
    # add new invoice pk
    return redirect(new_invoice, pk=invoice.pk)

def new_invoice(request, pk):
    context = {}
    context['invoice'] = Invoice.objects.get(InvoiceID = pk)
    context['invoiceorders'] = InvoiceOrder.objects.filter(InvoiceID_id = pk)
    context['payments'] = Payment.objects.filter(InvoiceID_id = pk)
    cid = Invoice.objects.get(InvoiceID = pk).CustomerID_id
    q = Customer.objects.get(CustomerID = int(cid)).CustomerType_id
    # if customer type is patron
    if q == 1:
        context['address'] = Patron.objects.get(CustomerID_id = cid).AddressID
    else:
        context['address'] = Business.objects.get(CustomerID_id = cid).AddressID
    return render(request, 'invoice/invoice_details.html', context)