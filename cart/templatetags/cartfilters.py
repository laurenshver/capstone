from django.template import Library
from decimal import Decimal

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
