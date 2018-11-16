import random

class Coordinates(object):
    def __init__(self, number, length, width):
        self.coordinates = self.create_coordinates(number, length, width)

    def create_coordinates(self, number, length, width):
        list_coordinates = []
        y_x_coordinates = []
        for _ in range(number):
            y_x_coordinates.append(random.randint(0, length))
            y_x_coordinates.append(random.randint(0, width))
            list_coordinates.append(y_x_coordinates)
            y_x_coordinates = []
        print(list_coordinates)

        return list_coordinates

if __name__ == "__main__":
    test = Coordinates(20, 160, 180)
    print(test)
