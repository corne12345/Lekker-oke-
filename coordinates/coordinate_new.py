class CoordinatesHouse(object):
    """
    Creates coordinates for little houses (one-family homes)
    """

    def __init__(self, y, x, house):
        self.y = y
        self.x = x
        self.house = house

    def coordinates(self):
        coordinates = []
        coordinates_y = [self.y, self.y, self.y + self.house.length,
                                self.y + self.house.length]
        coordinates_x = [self.x, self.x + self.house.width,
                                self.x, self.x + self.house.width]
        coordinates.append(coordinates_y)
        coordinates.append(coordinates_x)

        return coordinates
