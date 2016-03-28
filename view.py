
from controller import *
from model import initial_values


def menu():  # Взаємодія з користувачем
    print(" 1.Show")
    print(" 2.Add day")
    print(" 3.Add month")
    print(" 4.Delete day")
    print(" 5.Delete month")
    print(" 6.Exit")
    initial_values()
    choose()
    want_cont()


def choose():
    n = input("Your choice: ")
    if n == "1":
        show_month()
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


menu()