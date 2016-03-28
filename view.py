

from model import *


def menu():  # Взаємодія з користувачем
    print(" 1.Show ")
    print(" 2.Add day ")
    print(" 3.Add month")
    print(" 4.Delete day")
    print(" 5.Delete month")
    print(" 6.Exit ")
    choose()
    want_cont()


def choose():
    n = input("Your choice: ")
    if n == "1":
        pass
        #show_month()
    elif n == "2":
        add_day_param()
    elif n == "3":
        add_del_month_param(1)
    elif n == "4":
        del_day_param()
    elif n == "5":
        add_del_month_param(2)
    elif n == "6":
        exit()


def add_day_param():
    month = input("Enter the month")
    # check month
    number = input("Enter the number")
    pressure = input("Enter the pressure")
    temperature = input("Enter the temperature")
    wind = input("Enter the wind")
    add_day(pressure, temperature, wind, month, number)


def add_del_month_param(n):
    name = input("Enter the month")
    # check
    if n == 1:
        add_month(name)
    else:
        del_month(name)


def del_day_param():
    month = input("Enter the month")
    number = input("Enter the number")
    # check
    del_day(month, number)


def want_cont():
    print("If you want to continue enter 1, else enter any key ")
    choice2 = input("Your choice: ")
    if choice2 == "1":
        menu()
    else:
        exit()


menu()