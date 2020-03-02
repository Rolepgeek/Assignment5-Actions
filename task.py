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
