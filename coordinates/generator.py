import random

class Coordinates(object):
    def __init__(self, number, length, width):
        self.coordinates = self.create_coordinates(number, length, width)

    # random generator
    def create_coordinates(self, number, length, width):
        list_coordinates = []
        y_x_coordinates = {}
        for _ in range(number):

            # creates a library with the y and x coordinates
            y_x_coordinates.update({"y" : random.randint(0, length),
                                    "x" : random.randint(0, width)})
            list_coordinates.append(y_x_coordinates)
            y_x_coordinates = {}
        return list_coordinates

if __name__ == "__main__":
    test = Coordinates(20,180,160).coordinates
    print(test)
