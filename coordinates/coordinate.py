class Coordinates_little(object):

    def __init__(self, y, x):
        self.y = y
        self.x = x

    def coordinates(self):
        coordinates = []
        little_coordinates_y = [y, y, y + 8, y + 8]
        little_coordinates_x = [x, x + 8, x, x + 8]
        coordinates.append(little_coordinates_y)
        coordinates.append(little_coordinates_x)

        return coordinates

if __name__ == "__main__":

    coordinates_1 = Coordinates_little(70, 70)
    coordinates_2 = Coordinates_little(50, 50)
