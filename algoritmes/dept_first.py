import math
import pathlib as pathlib
import sys
from bokeh.plotting import show
import random
import copy
import csv

path = pathlib.Path.cwd()
path = path.absolute()
path = path.parent
path = pathlib.Path(path).iterdir()

for submap in path:
    sys.path.append(str(submap))
from grid_houses import Grid


from Opzet import LittleHouse, MediumHouse, LargeHouse, Water

class Depthfirst(object):
    def __init__(self, number, length, width, grid):
        self.number = number
        self.grid = grid
        self.length = 180
        self.width = 160
        # self.coordinates = self.create_coordinates(number)
        self.points = {}
        self.number_point = 1

    def grid(self):
        self.length = 180
        self.width = 160

    def create_coordinates(self):
        list_coordinates = []
        y_x_coordinates = {}

        x_list = []
        y_list = []

        for i in range(0, self.width + 1, 10):
            x_list.append(i)

        for i in range(0, self.length + 1, 10):
            y_list.append(i)

        print(x_list)
        print(y_list)

        number = 20
        y_x_coordinates = []

        # check if water is on the place
        for y_value in y_list:
            for x_value in x_list:
                y_x_coordinates.append({"y" : y_value,
                                        "x" : x_value})


        print(y_x_coordinates)

        y_x_coordinate = []

        # while len(y_x_coordinates) <= number:
        #     y_x_coordinates.append({"y" : random.choice(y_list),
        #                             "x" : random.choice(x_list)})
        #
        #     for i in range(len(y_x_coordinates)):
        #         for j in range(len(y_x_coordinates)):
        #             if (i != j and y_x_coordinates[i]["x"] == y_x_coordinates[j]["x"] \
        #             and y_x_coordinates[i]["y"] == y_x_coordinates[j]["y"]):
        #                 # Hier nog dat die niet in water mag aan toevoegen
        #                 y_x_coordinates.remove(y_x_coordinates[i])
        print(y_x_coordinate)

        return y_x_coordinates , y_x_coordinate

if __name__ == "__main__":
    grid = Grid(180, 160)
    test = Depthfirst(20, 180, 160, grid)
    test.create_coordinates()
