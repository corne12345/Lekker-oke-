import random

class Coordinates(object):
    def __init__(self, number, length, width):
        self.length = length
        self.width = width
        self.coordinates = self.create_coordinates(number)

    # random generator
    def create_coordinates(self, number):
        list_coordinates = []
        y_x_coordinates = {}
        for _ in range(number):

            # creates a library with the y and x coordinates
            y_x_coordinates.update({"y" : random.randint(0, self.length),
                                    "x" : random.randint(0, self.width)})
            list_coordinates.append(y_x_coordinates)
            y_x_coordinates = {}
        return list_coordinates

    def single_coordinate(self):
        y_x_coordinates = ({"y" : random.randint(0, self.length),
                            "x" : random.randint(0, self.width)})
        return y_x_coordinates


if __name__ == "__main__":
    test = Coordinates(20,180,160).coordinates
    print(test)
