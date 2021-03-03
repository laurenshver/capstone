from django.template import Library

register = Library()

@register.filter
def multiply(string, times):
    times = int(times)
    return string * times

@register.filter
def unchecked(string, times):
    times = int(times)
    return string  * (5-times)