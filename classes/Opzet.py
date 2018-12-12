# the measurements are in decimeters (not in foot, filthy emperials)

class LittleHouse(object):
    """
    Defines a little house (one-family home).
    """
    
    def __init__(self, nr_of_houses, length, width, standard_price, detachement, price_improvement):
        self.detachement = detachement
        self.nr_of_houses = nr_of_houses
        self.length = length
        self.width = width
        self.surface = length * width
        self.price = standard_price
        self.number = 0.6 * nr_of_houses
        self.price_improvement = price_improvement

    def surface_house(self, length, width):
        surface = length * width
        return surface

class MediumHouse(object):
    """
    Defines a medium house (bungalow).
    """
    
    def __init__(self, nr_of_houses, length, width, standard_price, detachement, price_improvement):
        self.nr_of_houses = nr_of_houses
        self.length = length
        self.width = width
        self.surface = length * width
        self.number = 0.25 * nr_of_houses
        self.price = standard_price
        self.detachement = detachement
        self.price_improvement = price_improvement

class LargeHouse(object):
    """
    Defines a large house (maison).
    """
    
    def __init__(self, nr_of_houses, length, width, standard_price, detachement, price_improvement):
        self.nr_of_houses = nr_of_houses
        self.length = length
        self.width = width
        self.surface = length * width
        self.number = 0.15 * nr_of_houses
        self.price = standard_price
        self.detachement = detachement
        self.price_improvement = price_improvement

class Water(object):
    """
    Defines the water.
    """
        
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.surface = width * length
