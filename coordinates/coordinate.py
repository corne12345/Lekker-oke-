class Coordinates_little(object):
    """
    Creates coordinates for little houses (one-family homes).
    """

    def __init__(self, y, x,):
        self.y = y
        self.x = x

    def coordinates(self):
        coordinates_little = []
        little_coordinates_y = [self.y, self.y, self.y + 8, self.y + 8]
        little_coordinates_x = [self.x, self.x + 8, self.x, self.x + 8]
        coordinates_little.append(little_coordinates_y)
        coordinates_little.append(little_coordinates_x)

        return coordinates_little

class Coordinates_medium(object):
    """
    Creates coordinates for medium houses (bungalow).
    """

    def __init__(self, y, x):
        self.y = y
        self.x = x

    def coordinates(self):
        coordinates_medium = []
        medium_coordinates_y = [self.y, self.y, self.y + 7.5, self.y + 7.5]
        medium_coordinates_x = [self.x, self.x + 10, self.x, self.x + 10]
        coordinates_medium.append(medium_coordinates_y)
        coordinates_medium.append(medium_coordinates_x)

        return coordinates_medium

class Coordinates_large(list):
    """
    Creates coordinates for large houses (maison).
    """

    def __init__(self, y, x):
        self.y = y
        self.x = x

    def coordinates(self):
        coordinates_large = []
        large_coordinates_y = [self.y, self.y, self.y + 10.5, self.y + 10.5]
        large_coordinates_x = [self.x, self.x + 11, self.x, self.x + 11]
        coordinates_large.append(large_coordinates_y)
        coordinates_large.append(large_coordinates_x)

        return coordinates_large
