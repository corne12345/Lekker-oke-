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

    # def grid(self):
    #     self.length = 180
    #     self.width = 160

    def create_coordinates(self):
        list_coordinates = []
        # y_x_coordinates = {}

        x_list = []
        y_list = []

        for i in range(20, self.width, 20):
            x_list.append(i)

        for i in range(20, self.length, 20):
            y_list.append(i)

        print(x_list)
        print(y_list)

        number = 8
        y_x_coordinates = []

        # check if water is on the place
        for y_value in y_list:
            for x_value in x_list:
                y_x_coordinates.append({"y" : y_value,
                                        "x" : x_value})


        # print(y_x_coordinates)

        # y_x_coordinate = ({"y" : random.choice(y_list),
        #                     "x" : random.choice(x_list)})
        #
        # print(y_x_coordinate)

        end_coordinates = []
        coordinates = []

        for i, coord in enumerate(y_x_coordinates):
            if i < number:
                coordinates.append(coord)

        end_coordinates.append(coordinates)
        #
        print(end_coordinates)

        # # for i, coord in enumerate(all_coordinates):
        # for i, coord in enumerate(y_x_coordinates):
        #     # for i, coord in enumerate(y_x_coordinates):
        #     coordinates.remove(coordinates[-1])
        #     coordinates.append(coord)
        #     end_coordinates.append(coordinates)
        #     print(coordinates)
        #
        # print(end_coordinates)


        for i in range(len(coordinates)):
            for j, coord in enumerate(y_x_coordinates):
                coordinates[i] = coord
                end_coordinates.append(coordinates)
                print(coordinates)
        # print(end_coordinates)

        for i in range(len(coordinates)):
            for j in range(len(coordinates)):
                for k, coord in enumerate(y_x_coordinates):
                        coordinates[i] = coord
                        end_coordinates.append(coordinates)
                        print(coordinates)
        # print(end_coordinates)



        # for i in range(number):
        #     for j in range(len(coordinates)):
        #         if y_x_coordinates[i]["x"] == 160:
        #             coordinates.remove(y_x_coordinates[i])


                # if (i == j and y_x_coordinates[i]["x"] == y_x_coordinates[j]["x"] \
                # and y_x_coordinates[i]["y"] == y_x_coordinates[j]["y"]):
                #     # Hier nog dat die niet in water mag aan toevoegen
                #     coordinates.remove(y_x_coordinates[i])

        # print(coordinates)

        return y_x_coordinates, coordinates

if __name__ == "__main__":
    grid = Grid(180, 160)
    test = Depthfirst(8, 180, 160, grid)
    test.create_coordinates()
