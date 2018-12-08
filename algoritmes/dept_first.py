import math
import pathlib as pathlib
import sys
from bokeh.plotting import show
import random
import copy
import csv

# Imports different paths, has to be changed and to be put in main.
path = pathlib.Path.cwd()
path = path.absolute()
path = path.parent
path = pathlib.Path(path).iterdir()

for submap in path:
    sys.path.append(str(submap))
from grid_houses import Grid


from Opzet import LittleHouse, MediumHouse, LargeHouse, Water

class Depthfirst(object):
    """
    This function calculates all the possible coordinates for the houses
    in steps of ten.
    """

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

    # Creates the coordinates.
    def create_coordinates(self):
        list_coordinates = []
        # y_x_coordinates = {}

        # Makes lists for all the x and y coordinates.
        x_list = []
        y_list = []


        # Appends all the x and y coordinates.
        for i in range(2, self.width, 1):
            x_list.append(i)

        for i in range(2, self.length, 1):
            y_list.append(i)

        number = 20
        y_x_coordinates = []


        # To do: check if water is on the place!!!!!
        # Appends all the possible coordinates to a list.
        for y_value in y_list:
            for x_value in x_list:
                y_x_coordinates.append({"y" : y_value,
                                        "x" : x_value})


        # print(y_x_coordinates)
        print(len(y_x_coordinates))

        end_coordinates = []
        coordinates = []
        # print(y_x_coordinates)

        for i, coord in enumerate(y_x_coordinates):
            if len(coordinates) < 20:
                coordinates.append(coord)

                if len(coordinates) > 1:
                    pause = 0
                    for j in range(10):
                        if (coordinates[-1]["y"] == coordinates[-2]["y"] \
                        and (coordinates[-1]["x"] - j) == coordinates[-2]["x"]):
                            coordinates.remove(coord)
                            pause = 1
                            break



                    if pause == 0:

                        for j in range(len(coordinates) - 1):
                            for k in range(10):
                                for l in range(10):
                                    if ((coordinates[-1]["y"] - l) == coordinates[j]["y"] \
                                    and (coordinates[-1]["x"] - k) == coordinates[j]["x"]):
                                    # print(coord)
                                        coordinates.remove(coord)
                                    # print("blabla")

                        if len(coordinates) >= 12:
                            if coordinates[-1]["y"] == coordinates[-2]["y"] \
                            and (coordinates[-1]["x"] - 10) == coordinates[-2]["x"]:
                                 coordinates.remove(coord)

                            for j in range(len(coordinates) - 1):
                                    if ((coordinates[-1]["y"] - 1) == coordinates[j]["y"] \
                                    and (coordinates[-1]["x"] - 10) == coordinates[j]["x"]):
                                        # print("tweede")
                                        # print(coord)
                                        coordinates.remove(coord)

                        if len(coordinates) >= 17:
                            if coordinates[-1]["y"] == coordinates[-2]["y"] \
                            and (coordinates[-1]["x"] - 11) == coordinates[-2]["x"]:
                                 coordinates.remove(coord)

                            for j in range(len(coordinates) - 1):
                                    if ((coordinates[-1]["y"] - 1) == coordinates[j]["y"] \
                                    and (coordinates[-1]["x"] - 11) == coordinates[j]["x"]):
                                        # print("tweede")
                                        # print(coord)
                                        coordinates.remove(coord)



        # end_coordinates.append(coordinates)

        print(coordinates)
        print(len(coordinates))

        # # hier geeft die alleen deel van de coorinaten
        # for i in range(len(coordinates)):
        #     for j, coord in enumerate(y_x_coordinates):
        #         coordinates[i] = coord
        #         end_coordinates.append(coordinates)
        # #         print(coordinates)
        # # print(end_coordinates)

        # # changes all the coordinates, until you have all combinations and adds
        # # them to the list with all final coordinates
        # for i in range(len(coordinates)):
        #     for j in range(len(coordinates)):
        #         for k, coord in enumerate(y_x_coordinates):
        #             for l, coord_2 in enumerate(y_x_coordinates):
        #                 coordinates[i] = coord
        #                 coordinates[j] = coord_2
        #                 end_coordinates.append(coordinates)
        #                 print(coordinates)

                        # print(len(end_coordinates))

                        # # checks if same coordinates are used --> dit werkt zeg maar niet, dan krijg je een memory error
                        # # maar als je dit weghaalt en regel erboven met append uitcommit, werkt het wel en krijg je meer dan 200.000 uitkomsten.
                        # while coordinates[i]["y"] != coordinates[j]["y"] \
                        # or  coordinates[i]["x"] != coordinates[j]["x"]:
                        #     end_coordinates.append(coordinates)


        # print(len(end_coordinates))

        # # dit hieronder zou ook kunnen, maar ik weet niet wat in de remove(????) moet. Want coordinates erin kan niet.
        # for i in range(len(coordinates)):
        #     for j in range(len(coordinates)):
        #         while coordinates[i]["y"] == coordinates[j]["y"] \
        #         and  coordinates[i]["x"] == coordinates[j]["x"]:
        #             end_coordinates.remove(?????)
        #             # end_coordinates.remove(coordinates[i]["x"])

        # print(len(end_coordinates))

        # print(coordinates)
        return coordinates, y_x_coordinates

    def create_coordinates_2(self, all_coordinates):
        """
        This function calculates all the possible coordinates.
        """

        coordinates = all_coordinates[0]
        y_x_coordinates = all_coordinates[1]


        print(coordinates)
        # print(y_x_coordinates)
        coordinates.remove(coordinates[-1])

        for i, coord in enumerate(y_x_coordinates):
            # if len(coordinates) < 20:
            #     coordinates.append(coord)
            # for j in range(len(coordinates) - 1):

            # coordinates.append(coord)
            # print(coordinates)


            if len(coordinates) < 20:
                coordinates.append(coord)

                if len(coordinates) > 1:
                    pause = 0
                    for j in range(len(coordinates) - 1):
                        for k in range(10):
                            # print(coordinates)
                            if (coordinates[-1]["y"] == coordinates[j]["y"] \
                            and (coordinates[-1]["x"] - k) == coordinates[j]["x"]):
                                coordinates.remove(coord)
                                pause = 1
                                break

                    for j in range(len(coordinates) - 1):
                        for k in range(10):
                            if ((coordinates[-1]["y"] - 1) == coordinates[j]["y"] \
                            and (coordinates[-1]["x"] - k) == coordinates[j]["x"]):
                                # print(coord)
                                coordinates.remove(coord)
                                # print("blabla")

                    if pause == 0:
                        if len(coordinates) >= 12:
                            if coordinates[-1]["y"] == coordinates[-2]["y"] \
                            and (coordinates[-1]["x"] - 10) == coordinates[-2]["x"]:
                                 coordinates.remove(coord)

                            for j in range(len(coordinates) - 1):
                                    if ((coordinates[-1]["y"] - 1) == coordinates[j]["y"] \
                                    and (coordinates[-1]["x"] - 10) == coordinates[j]["x"]):
                                        # print("tweede")
                                        # print(coord)
                                        coordinates.remove(coord)

                        if len(coordinates) >= 17:
                            if coordinates[-1]["y"] == coordinates[-2]["y"] \
                            and (coordinates[-1]["x"] - 11) == coordinates[-2]["x"]:
                                 coordinates.remove(coord)

                            for j in range(len(coordinates) - 1):
                                    if ((coordinates[-1]["y"] - 1) == coordinates[j]["y"] \
                                    and (coordinates[-1]["x"] - 11) == coordinates[j]["x"]):
                                        # print("tweede")
                                        # print(coord)
                                        coordinates.remove(coord)


                # if ((coordinates[-1]["y"] - 1) == coordinates[i]["y"] \
                # and (coordinates[-1]["x"] - 11) == coordinates[i]["x"]):
        print("tweede")
        print(coordinates)
                #     coordinates.remove(coord)



if __name__ == "__main__":
    grid = Grid(180, 160)
    test = Depthfirst(8, 180, 160, grid)
    first = test.create_coordinates()
    coordinates = test.create_coordinates_2(first)
