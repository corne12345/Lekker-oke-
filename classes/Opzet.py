# the measurements are decimeters (not in foot, filthy emperials)



# Single Home defined
class SingleHome(object):
    def __init__(self, nr_of_houses, length, width, standard_price, detachement):
        self.detachement = detachement
        self.nr_of_houses = nr_of_houses
        self.length = length
        self.width = width
        self.surface = length * width
        self.number = 0.6 * nr_of_houses # TODO: misschien hier nog percentage ook als variabele invullen
        self.price = standard_price

    def surface_house(self, length, width):
        surface = length * width
        return surface


# Bungalow defined
class Bungalow(object):
    def __init__(self, nr_of_houses, length, width, standard_price):
        self.nr_of_houses = nr_of_houses, standard_price
        self.length = length
        self.width = width
        self.surface = length * width
        self.number = 0.25 * nr_of_houses
        self.price = standard_price

# Maison defined
class Maison(object):
    def __init__(self, nr_of_houses, length, width, standard_price):
        self.nr_of_houses = nr_of_houses
        self.length = length
        self.width = width
        self.surface = length * width
        self.number = 0.15 * nr_of_houses
        self.price = standard_price

class Water(object):
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.surface = width * length

if __name__ == "__main__":
    total_homes = 20

    # defines the houses
    single_home = SingleHome(total_homes, 8, 8, 285000, 2)
    bungalow = Bungalow(total_homes, 10, 7.5, 399000, 4)
    maison = Maison(total_homes, 11, 10.5, 610000, 6)
