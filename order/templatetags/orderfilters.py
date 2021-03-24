from django.template import Library
from customer.models import *
register = Library()

@register.filter
def get_patron_name(patron, custID):
    return Patron.objects.get(CustomerID_id = custID)

@register.filter
def get_business_name(business, custID):
    return Business.objects.get(CustomerID_id = custID)

@register.filter
def status_icon(status):
    statuses = {
        "Accepted" : "fas fa-user-check fa-2x",
        "Pending" : "fas fa-business-time fa-2x",
        "Shipped" : "fas fa-truck fa-2x",
        "Backorder" : "fas fa-exclamation-circle fa-2x",
        "Extended" : "fas fa-sort-amount-up fa-2x",
        "Invoiced" : "fas fa-file-invoice-dollar fa-2x",
        "Closed" : "fas fa-lock fa-2x",
    }

    return statuses.get(status)

@register.filter
def total_cost(price, length):
    return price*length