import random

class Coordinates(object):
    def __init__(self, number, length, width, grid):
        self.length = length
        self.width = width
        self.grid = grid
        self.coordinates = self.create_coordinates(number)

    # random generator
    def create_coordinates(self, number):
        list_coordinates = []
        y_x_coordinates = {}
        for _ in range(number):

            # creates a library with the y and x coordinates
            y_x_coordinates.update({"y" : random.randint(0, self.length),
                                    "x" : random.randint(0, self.width)})

            # check if water is on the place 
            while self.length <= y_x_coordinates["y"] \
            or self.width <= y_x_coordinates["x"] \
            or self.grid[y_x_coordinates["y"]][y_x_coordinates["x"]] == 1 :
                y_x_coordinates = ({"y" : random.randint(0, self.length),
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
