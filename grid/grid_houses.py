import sys
import pathlib

# # get the path to the classes
path = pathlib.Path.cwd()
path = pathlib.Path(path).iterdir()
for submap in path:
    sys.path.append(str(submap))

import csv
from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d
from Opzet import *
from generator import *
from calc_money import *


# 1 = waterbody
# 2 = little house (single family home)
# 3 = medium house (bungalow)
# 4 = large house (maison)
# 5 = detachement
class Grid(object):
    def __init__(self, total_length, total_width):
        self.width = total_width
        self.length = total_length
        self.grid = self.grid_command()
        self.little_coordinates = None
        self.coordinates = Check().check()
        self.waterbody = None

    def make_csv(self):
        with open("coordinates.csv", "w") as csv_file:
            csv_reader = csv.writer(csv_file, delimiter=" ")
            for row in self.coordinates.items():
                csv_reader.writerow(row)

    def load_csv(self):
        list = []

        with open("data-for-check.txt", "r") as infile, open("data-for-check.csv", "w"):
            for text in infile:
                list.append(text)
        print(list)


    # makes the grid itself
    def grid_command(self):
        grid = []
        grid_row = []
        for length in range(self.length):
            for pixel in range(self.width):
                grid_row.append(0)
            grid.append(grid_row)
            grid_row = []
        return grid

    # creates different waterbodies
    def create_water(self, file):
        """
        Creates different waterbodies
        """
        water = file
        first_length_position = None
        first_width_position = None
        last_width_position = None

        # creates the water and checks if there is nothing there
        for row in range(len(self.grid)): # length

            # get the first position of the length
            if first_length_position == None:
                first_length_position = row

            if water.length > (row - first_length_position) \
            and first_length_position != None:
                for place, item in enumerate(self.grid[0]): # width
                    if item == 0 and first_width_position == None:
                        first_width_position = place
                        self.grid[row][place] = 1

                    elif first_width_position != None and place >= first_width_position \
                    and water.width > (place - first_width_position):
                        self.grid[row][place] = 1

        # calculates the surface
        surface = water.length * water.width
        self.waterbody = {"y": first_width_position, "x": first_width_position}


    def create_house(self, little, middle, large, water):
        """
        Creates little homes (single family homes)
        """

        houses ={"little": little, "medium": middle, "large": large}
        coordinates = self.coordinates
        first_length_position = None
        first_width_position = None


        for house in coordinates.keys():
            for number in range(len(coordinates[house])):

                # coordinates, navragen of library beter is
                coordinate = coordinates[house][number]


                # import the grid and put the houses in the right spaces
                for row in range(len(self.grid)): # to do iterate  over the grid to put the houses on the right places
                    if first_length_position == None and row == round(coordinate["y"]): # nog nakijken of de huizen goed positioneerd
                        first_length_position = row

                    # get first x position
                    if first_length_position != None and \
                    first_length_position + houses[house].length > row :
                        for place in range(len(self.grid[0])):

                            # fill the first the x position
                            if self.grid[row][place] not in range(1, 5) and first_width_position == None and place == round(coordinate["x"]):
                                first_width_position = place
                                if house == "little":
                                    self.grid[row][place] = 2
                                elif house == "medium":
                                    self.grid[row][place] = 3
                                else:
                                    self.grid[row][place] = 4

                            # fill the grid in
                            elif first_width_position != None and self.grid[row][place] not in range(1, 5) and \
                            first_width_position + houses[house].width > place and place - first_width_position >= 0:
                                if house == "little":
                                    self.grid[row][place] = 2
                                elif house == "medium":
                                    self.grid[row][place] = 3
                                else:
                                    self.grid[row][place] = 4


# Visualizes the graph
class Visualator(object):
    def __init__(self, grid, little_house, medium_house, large_house, water):
        self.grid = grid.grid
        self.coordinates = grid.coordinates
        self.houses = {"little": little_house, "medium": medium_house, "large": large_house}
        self.water, self.waterbody = water, grid.waterbody

    def bokeh(self):
        graph = figure(title = "Amstelhaege")

        # get x values for the bokeh figure
        x_axis = self.grid[-1]
        first_x = x_axis.index(x_axis[0])
        last_x = None
        for count, values in enumerate(x_axis):
            last_x = count + 1

        # get y values for graph
        y_axis = self.grid
        first_y = y_axis.index(y_axis[0])
        last_y = None
        for count, values in enumerate(y_axis):
            last_y = count + 1

        # makes the  graph and changes the aesthetics if the graph
        graph.x_range = Range1d(last_x, first_x)
        graph.y_range = Range1d(last_y, first_y)

        # makes ground plan polygon
        graph.patch(x=[first_x, first_x, last_x, last_x],
                    y=[first_y, last_y, last_y, first_y],
                    color="grey")

        # make waterbody
        graph.patch(x=[self.waterbody["x"], self.waterbody["x"],
                       self.waterbody["x"] + self.water.width,
                       self.waterbody["x"] + self.water.width],
                    y=[self.waterbody["y"],
                       self.waterbody["y"] + self.water.length,
                       self.waterbody["y"] + self.water.length,
                       self.waterbody["y"]],
                    color="blue", line_color="black")

        # makes the houses into the graph
        for sort in self.coordinates.keys():
            colour = None

            for house in self.coordinates[sort]:
                try:
                    if sort in "little":
                        colour = "red"
                    elif sort in "medium":
                        colour = "yellow"
                    else:
                        colour = "green"
                    graph.patch(x=[house["x"], house["x"], (house["x"] + self.houses[sort].width), (house["x"] + self.houses[sort].width)],
                                y=[house["y"], (house["y"] + self.houses[sort].length), (house["y"] + self.houses[sort].length), house["y"]],
                                color=colour, line_color="black")
                except:
                    print("No valid coordinates")

        return graph
