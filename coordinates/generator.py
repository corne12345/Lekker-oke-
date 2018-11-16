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
<<<<<<< HEAD
            y_x_coordinates = []
        print(list_coordinates)
=======
            y_x_coordinates = {}
>>>>>>> b78a838564ec0e0d878a34797b07fcafdd92c623

        return list_coordinates

if __name__ == "__main__":
    test = Coordinates(20, 160, 180).coordinates
    print(test)
