import re
import datetime
from datetime import date


def pan_validation(pan):
    if re.match('^[A-Z]{5}\d{4}[A-Z]$', pan):
        return True
    return False


def aadhar_validation(aadhar):
    if re.match('^\d{12}$', aadhar):
        return True
    return False


def name_validation(name):
    if re.match("^[A-Za-z\s]{1,}[\.]{0,1}[A-Za-z\s]{0,}$", name):
        if len(name) > 48 or len(name) < 3:
            return False
        else:
            return True
    else:
        return False


def phone_validation(phno):
    if re.match('^\d{10}$', phno):
        return True
    return False


def dob_validation(day, month, year):
    today = date.today()
    x, y, z = today.strftime("%d %m %Y").split()
    x, y, z = int(x), int(y), int(z)
    if year < 1900 or z - year < 18:
        return False
    try:
        newDate = datetime.datetime(year, month, day)
    except ValueError:
        return False
    return True


def pin_validation(pin):
    if re.match('^\d{6}$', pin):
        return True
    return False
