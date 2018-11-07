# Single Home defined
class SingleHome(object):
    def __init__(self, nr_of_houses, length, width, standard_price):
        self.nr_of_houses = nr_of_houses
        self.surface = length * width
        self.number = 0.6 * nr_of_houses
        self.price = standard_price

    def surface_house(self, length, width):
        surface = length * width
        return surface

# Bungalow defined
class Bungalow(object):
    def __init__(self, nr_of_houses, length, width):
        self.nr_of_houses = nr_of_houses, standard_price
        self.surface = length * width
        self.number = 0.25 * nr_of_houses
        self.price = standard_price

# Maison defined
class Maison(object):
    def __init__(self, nr_of_houses, length, width, standard_price):
        self.nr_of_houses = nr_of_houses
        self.surface = length * width
        self.number = 0.15 * nr_of_houses
        self.price = standard_price

class Surface(object):
    def __init__(self, total_width, total_length):
        self.width = total_width
        self.length = total_length
        self.total_surface = total_width * total_length

class WaterSurface(object):
    def __init__(self):
        self.surface = Surface.total_surface * 0.2
if __name__ == "__main__":
    total_homes = 20

    # defines the houses
    single_home = SingleHome(total_homes, 8, 8, 285000)
    bungalow = Bungalow(total_homes, 10, 7.5, 399000)
    maison = Maison(total_homes, 11, 10.5, 610000)
