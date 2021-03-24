from django.template import Library

register = Library()

@register.filter
def status_filter(inventory, status):
    return inventory.filter(ToolStatusID__ToolStatus = status).filter(StoreID_id = 1).count()

@register.filter()
def store_filter_count(inventory):
    return inventory.filter(StoreID_id = 1).count()

@register.filter
def store_filter(inventory, store1):
    if store1 == 'Y':
        return inventory.filter(StoreID_id = 1)
    else:
        return inventory.exclude(StoreID_id = 1)

@register.filter
def get_price(prices, rate):
    return prices.filter(PriceRateID__PriceRate = rate)

@register.filter
def return_string(inventoryid):
    return str(inventoryid)