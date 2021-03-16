from django import forms 
from inventory.models import *

PRICE_RATE = [
    ('hourly', 'Hourly'),
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
]

class AddCartForm(forms.Form):
    PriceRate = forms.ChoiceField(widget = forms.RadioSelect, choices=PRICE_RATE)


