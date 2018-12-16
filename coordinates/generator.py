import random

class Coordinates(object):
    """
    Generates coordinates for houses.
    """

    def __init__(self, number, length, width, grid):
        self.length = length
        self.width = width
        self.grid = grid
        self.coordinates = self.create_coordinates(number)

    def create_coordinates(self, number):
        """
        Generates random coordinates.
        """

        list_coordinates = []
        y_x_coordinates = {}

        # Iterates trough the number.
        for _ in range(number):

            # Creates a library with the y and x coordinates.
            y_x_coordinates.update({"y" : random.randint(0, self.length),
                                    "x" : random.randint(0, self.width)})

            # Checks if water is on the place.
            while self.length <= y_x_coordinates["y"] \
            or self.width <= y_x_coordinates["x"] \
            or self.grid[y_x_coordinates["y"]][y_x_coordinates["x"]] == 1 :
                y_x_coordinates = ({"y" : random.randint(0, self.length),
                                    "x" : random.randint(0, self.width)})

            list_coordinates.append(y_x_coordinates)
            y_x_coordinates = {}

        return list_coordinates

    def single_coordinate(self):
        """
        Appends a random coordinate.
        """

        y_x_coordinates = ({"y" : random.randint(0, self.length),
                            "x" : random.randint(0, self.width)})

        return y_x_coordinates


if __name__ == "__main__":
    test = Coordinates(20,180,160).coordinates
    print(test)
