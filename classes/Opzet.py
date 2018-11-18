# the measurements are decimeters (not in foot, filthy emperials)



# Single Home defined
class LittleHouse(object):
    def __init__(self, nr_of_houses, length, width, standard_price, detachement):
        self.detachement = detachement
        self.nr_of_houses = nr_of_houses
        self.length = length
        self.width = width
        self.surface = length * width
        self.number = 0.6 * nr_of_houses
        self.price = standard_price

    def surface_house(self, length, width):
        surface = length * width
        return surface


# Bungalow defined
class MediumHouse(object):
    def __init__(self, nr_of_houses, length, width, standard_price):
        self.nr_of_houses = nr_of_houses, standard_price
        self.length = length
        self.width = width
        self.surface = length * width
        self.number = 0.25 * nr_of_houses
        self.price = standard_price

# Maison defined
class LargeHouse(object):
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
    total_houses = 20

    # defines the houses
    single_home = LittleHouse(total_houses, 8, 8, 285000, 2)
    bungalow = MediumHouse(total_houses, 10, 7.5, 399000, 4)
    maison = LargeHouse(total_houses, 11, 10.5, 610000, 6)
