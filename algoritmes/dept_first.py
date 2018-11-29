import math
import pathlib as pathlib
import sys
from bokeh.plotting import show
import random
import copy
import csv

class Depthfirst(object):
    def __init__(self):
        self.grid = self.grid()
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

        y_x_coordinates = []

        # check if water is on the place
        while len(y_x_coordinates) <= 20:
            y_x_coordinates.append({"y" : random.choice(y_list),
                                    "x" : random.choice(x_list)})

        print(y_x_coordinates)

        return y_x_coordinates

if __name__ == "__main__":
    test = Depthfirst()
    test.create_coordinates()
