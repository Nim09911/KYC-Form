import re
import datetime


def pan_validation(pan):
    if re.match('\d{10}', pan):
        return True
    return False


def aadhar_validation(aadhar):
    if re.match('\d{12}', aadhar):
        return True
    return False


def name_validation(name):
    if re.match('[a-zA-Z]+', name):
        if len(name) > 48:
            return False
        else:
            return True
    return False


def phone_validation(phno):
    if re.match('\d{10}', phno):
        return True
    return False


def dob_validation(day, month, year):
    try:
        newDate = datetime.datetime(year, month, day)
    except ValueError:
        return False
    return True


def pin_validation(pin):
    if re.match('\d{6}', pin):
        return True
    return False
