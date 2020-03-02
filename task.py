import math


def firstrun():
    return "success"


def circlerun(rad):
    return math.pi * (rad**2)


def listrun(deck):
    newlist = [0, 0]
    newlist[0] = deck[0]
    newlist[1] = deck[len(deck)-1]
    return newlist


def daterun(date1, date2):
    yearday1 = date1.day + monthcalc(date1)
    yearday2 = date2.day + monthcalc(date2)
    leapdays = 0
    for n in range(date1.year, date2.year):
        if n % 400 == 0:
            leapdays += 1
        elif n % 4 == 0 and n % 100 != 0:
            leapdays += 1
    totaldays = yearday2 - yearday1 + (date2.year - date1.year)*365 + leapdays
    return abs(totaldays)


def monthcalc(date1):
    mon_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthdays1 = 0
    if date1.year % 4 != 0:
        c1 = 0
    elif date1.year % 100 != 0:
        c1 = 1
    elif date1.year % 400 != 0:
        c1 = 0
    else:
        c1 = 1
    for n in range(date1.month - 1):
        if c1 == 0:
            monthdays1 += mon_list[n]
        if c1 == 1:
            monthdays1 += leap_list[n]
    return monthdays1
