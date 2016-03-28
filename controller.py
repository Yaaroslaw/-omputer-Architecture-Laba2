
from One_file_to_rule_them_all import *
from view import menu

def add_day_param():
    month = input("Enter the month ")
    # check month
    number = input("Enter the number ")
    pressure = input("Enter the pressure ")
    temperature = input("Enter the temperature ")
    wind = input("Enter the wind ")
    add_day(pressure, temperature, wind, month, number)


def add_del_month_param(n):
    name = input("Enter the month ")
    # check
    if n == 1:
        add_month(name)
    elif n == 2:
        del_month(name)


def del_day_param():
    month = input("Enter the month ")
    number = input("Enter the number ")
    # check
    del_day(month, number)


def want_cont():
    print("If you want to continue enter 1, else enter any key ")
    choice2 = input("Your choice: ")
    if choice2 == "1":
        menu()
    else:
        exit()


def show_month():
    for key in year:
        print(key)
    month = input("Enter the month ")
    # check
    for i in year[month]:
        print("Number: {}, Pressure: {}, Wind: {}, Temperature: {}".format(i.number, i.pressure, i.wind, i. temperature))
