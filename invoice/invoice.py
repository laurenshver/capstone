from datetime import timedelta, datetime

def invoice_expiry():
    '''calculate the invoice expiry date, which is 30 days from the incoice creation'''
    today = datetime.now()
    expiry_date = today + timedelta(days = 30)
    return expiry_date