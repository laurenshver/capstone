from django.template import Library
import datetime
from decimal import Decimal
from customer.models import Patron, Business
from retail.models import Store

register = Library()

@register.filter
def times(number):
    return range(number)

@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg2) + str(arg1)

@register.filter
def get_type(value):
    return type(value)

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def tool_filter(inventory, inventoryid):
    '''get tool inventory information'''
    return inventory.filter(InventoryID = int(inventoryid))

@register.filter
def price_filter(prices, toolid):
    '''get tool inventory information'''
    return prices.filter(ToolID_id = toolid)

@register.filter
def get_price(prices, rate):
    
    return prices.filter(PriceRateID__PriceRate = rate.title())

@register.filter
def calc_total(price,length):
    dollar_amount = str(price).split(" ")[0]
    cost = Decimal(dollar_amount.split("$")[1])
    return cost * int(length)

@register.filter
def get_patron_details(patrons, custID):
    return patrons.filter(CustomerID_id = int(custID))

@register.filter
def get_business_details(businesses, custID):
    return businesses.filter(CustomerID_id = int(custID))

@register.filter
def get_phone_number(phonenumbers, patID):
    # return customer cell phone
    return phonenumbers.filter(PatronID_id = int(patID)).filter(PhoneNumberID_id__PhoneNumberType_id = 2)

@register.filter
def primary_contact(buscontacts, busID):
    return buscontacts.filter(BusinessID_id = int(busID)).filter(PrimaryContact = "Y")

@register.filter
def store_name(storeid):
    return Store.objects.get(StoreID = int(storeid))

@register.filter
def elstdate(sdate):
    '''get earliest start date from array of start dates'''
    date = []
    for x in sdate:
        date.append(datetime.datetime.strptime(x, "%b. %d %Y").date())
    return min(date)

@register.filter
def latestdate(edate):
    '''get latest end date from array of end dates'''
    date = []
    for x in edate:
        date.append(datetime.datetime.strptime(x, "%b. %d %Y").date())
    return max(date)

@register.filter
def order_taxes(subtotal):
    return "{:.2f}".format(float(subtotal) * 0.13)

@register.filter
def order_deposit(subtotal):
    return "{:.2f}".format(float(subtotal) * 0.10)

@register.filter
def get_discount(subtotal, discount):
    return "{:.2f}".format(float(subtotal) * (float(discount)/100))

@register.filter
def get_order_total(subtotal, discount = "0.00"):
    subt = float(subtotal)
    tax = float(order_taxes(subtotal))
    deposit = float(order_deposit(subtotal))
    disc = float(get_discount(subtotal, discount))
    return "{:.2f}".format(subt + tax + deposit - disc)
