from model import *


def show_month():  # Виведення на екран місяців
    for i in season.keys():
        print("- " + i)
    month = input("Enter month: ")
    if month in season.keys():
        for i in season[month]:
            print(i)
    else:
        print("Oops, try again ")
        show_month()


def add_day(month, pr, tm, wd):  # Додавання днів
    day = {"pressure": pr, "temperature": tm, "wind": wd}
    season[month].append(day)


def add_month(name):  # Додавання місяців
    season[name] = []


def param(name):  # Технічні параметри щоденника погоди
    pressure = input("Please, type the pressure(684, 809): ")
    temperature = input("Please, type the temperature in celsius: ")
    wind = input("Please, type the speed of the wind: ")
    add_day(name, pressure, temperature, wind)
