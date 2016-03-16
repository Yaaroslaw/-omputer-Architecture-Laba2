from random import randint
season = {'March': [], 'April': [], 'May': []}  # Словник для місяців

class weather_blog(object):
    def __init__(self, name, days_amount):
        self.name = name
        self.days_amount = days_amount



class day(object):
    def __init__(self, pressure, temperature, wind):
        self.pressure = pressure
        self.temperature = temperature
        self.wind = wind


def creation_blog():  # Ф-ція для створення місяців в словнику season
    for k in season.keys():
        for i in range(5):
            season[k].append(creation_day())
    return season


def creation_day():  # Ф-ція для створення днів
    x = randint(684, 809)
    y = randint(-5, 20)
    z = randint(1, 30)
    day = {"pressure": x, "temperature": y, "wind": z}
    return day
























