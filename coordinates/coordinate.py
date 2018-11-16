class Coordinates_little(object):
    """
    Creates coordinates for little houses (one family homes)
    """

    def __init__(self, y, x):
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
    Creates coordinates for medium houses (bungalow)
    """

    def __init__(self, y, x):
        self.y = y
        self.x = x

    def coordinates(self):
        coordinates_medium = []
        medium_coordinates_y = [self.y, self.y, self.y + 7.5, self.y + 7.5]
        medium_coordinates_x = [self.x, self.x + 10, self.x, self.x + 10]
<<<<<<< HEAD
        coordinates_medium.append(medium_coordinates_y)
=======
        Coordinates_medium.append(medium_coordinates_y)
>>>>>>> 87c1142790a1960d66cf08a1337f8f50b1d68abe
        coordinates_medium.append(medium_coordinates_x)

        return coordinates_medium

class Coordinates_large(object):
    """
    Creates coordinates for large houses (mansion)
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

if __name__ == "__main__":

    coordinates_1 = Coordinates_little(0, 0)
    coordinates_2 = Coordinates_little(0, 10)
    coordinates_3 = Coordinates_little(0, 20)
    coordinates_4 = Coordinates_little(0, 30)
    coordinates_5 = Coordinates_little(0, 40)
    coordinates_6 = Coordinates_little(0, 50)
    coordinates_7 = Coordinates_little(0, 60)
    coordinates_8 = Coordinates_little(0, 70)
    coordinates_9 = Coordinates_little(0, 80)
    coordinates_10 = Coordinates_little(0, 90)
    coordinates_11 = Coordinates_little(0, 100)
    coordinates_12 = Coordinates_little(0, 110)

    coordinates_13 = Coordinates_medium(10, 0)
    coordinates_14 = Coordinates_medium(10, 15)
    coordinates_15 = Coordinates_medium(10, 30)
    coordinates_16 = Coordinates_medium(10, 45)
    coordinates_17 = Coordinates_medium(10, 60)

    coordinates_18 = Coordinates_large(30, 0)
    coordinates_19 = Coordinates_large(30, 15)
    coordinates_20 = Coordinates_large(30, 30)
