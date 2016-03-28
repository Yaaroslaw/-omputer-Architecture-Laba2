from random import randint
year = {}


class Day(object):
    def __init__(self, pressure, temperature, wind, number):
        self.pressure = pressure
        self.temperature = temperature
        self.wind = wind
        self.number = number


def initial_values():
    year["February"] = []
    for i in range(25, 29):
        x = randint(684, 809)
        y = randint(-9, 10)
        z = randint(1, 30)
        year["February"].append(Day(x, y, z, i))



























