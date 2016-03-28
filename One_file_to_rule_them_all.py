
from model import *


def add_day(pressure, temperature, wind, month, number):
    year[month].append(Day(pressure, temperature, wind, number))


def del_day(month, number):
    for i in year[month]:
        if i.number == number:
            year[month].remove(i)


def add_month(name):
    year[name] = []


def del_month(name):
    del year[name]