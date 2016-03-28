from random import randint
year = {}


class Day(object):
    def __init__(self, pressure, temperature, wind, month, number):
        self.pressure = pressure
        self.temperature = temperature
        self.wind = wind
        self.month = month
        self.number = number


def add_day(pressure, temperature, wind, month, number):
    year[month].append(Day(pressure, temperature, wind, month, number))


def del_day(month, number):
    for i in year[month]:
        if i.number == number:
            year[month].remove(i)


def add_month(name):
    year[name] = []


def del_month(name):
    del year[name]


#
# def creation_blog():  # Ф-ція для створення місяців в словнику season
#     for k in season.keys():
#         for i in range(5):
#             season[k].append(creation_day())
#     return season
#
#
# def creation_day():  # Ф-ція для створення днів
#     x = randint(684, 809)
#     y = randint(-5, 20)
#     z = randint(1, 30)
#     day = {"pressure": x, "temperature": y, "wind": z}
#     return day
























