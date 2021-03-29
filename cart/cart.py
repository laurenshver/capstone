from datetime import datetime, timedelta, time
import calendar

def get_start_date(startdate):
    '''format the start date. separate the string send in POST and get formatted date value'''
    array = []
    for x in startdate:
        date = datetime.strptime(x, "%Y-%m-%dT%H:%M")
        format_date = str(calendar.month_abbr[date.month]) + ". " + str(date.day) + " " + str(date.year)
        array.append(format_date)
    return array

def get_start_time(startdate, rate):
    '''set the start date to 7:00AM if not being rented on an hourly basis. otherwise, set start time to selected time'''
    array = []
    for x in range(len(startdate)):
        date = datetime.strptime(startdate[x], "%Y-%m-%dT%H:%M")
        if rate[x] == 'hourly':
            start_time_formatted = date.strftime("%H:%M %p")
            array.append(start_time_formatted)
        else:
            array.append("7:00 AM")
    return array

def get_end_date(startdate, rate, length):
    '''calculate end date of rentals'''
    array = []
    for x in range(len(startdate)):
        date = datetime.strptime(startdate[x], "%Y-%m-%dT%H:%M")
        if rate[x] == 'daily':
            end = date + timedelta(days = int(length[x]))
            format_date = str(calendar.month_abbr[end.month]) + ". " + str(end.day) + " " + str(end.year)
            array.append(format_date)
        elif rate[x] == 'weekly':
            end = date + timedelta(weeks = int(length[x]))
            format_date = str(calendar.month_abbr[end.month]) + ". " + str(end.day) + " " + str(end.year)
            array.append(format_date)
        elif rate[x] == 'monthly':
            end = date + timedelta(weeks = int(length[x]) * 4)
            format_date = str(calendar.month_abbr[end.month]) + ". " + str(end.day) + " " + str(end.year)
            array.append(format_date)
        else:
            format_date = str(calendar.month_abbr[date.month]) + ". " + str(date.day) + " " + str(date.year)
            array.append(format_date)
    return array

def get_end_time(startdate, rate, length): 
    '''calculate end time. return 5:00PM if not hourly'''
    array = []
    for x in range(len(startdate)):
        date = datetime.strptime(startdate[x], "%Y-%m-%dT%H:%M")
        if rate[x] == 'hourly':
            end = date + timedelta(hours = int(length[x]))
            end_time_formatted = end.strftime("%H:%M %p")
            array.append(end_time_formatted)
        else:
            array.append("5:00 PM")
    return array

def start_date_and_time(date):
    return datetime.combine(date, time(7, 00))

def end_date_and_time(date):
    return datetime.combine(date, time(17, 00))
