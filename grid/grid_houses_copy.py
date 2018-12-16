import sys

# # get the path to the classes
sys.path.append(("../classes"))
sys.path.append(sys.path[0].replace('\\grid', '\\coordinates'))
sys.path.append(sys.path[0].replace('\\grid', '\\score_functions'))

import csv
from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d
from Opzet import *
from generator import *
from calc_money import *


# 1 = waterbody
# 2 = little house (single-family home)
# 3 = medium house (bungalow)
# 4 = large house (maison)
# 5 = detachement
class Grid(object):
    """
    Defines the grid.
    """

    def __init__(self, total_length, total_width):
        self.width = total_width
        self.length = total_length
        self.grid = self.grid_command()
        self.little_coordinates = None
        self.coordinates = Check().check()

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

    def grid_command(self):
        """
        Creates the grid itself.
        """

        grid = []
        grid_row = []

        for length in range(self.length):
            for pixel in range(self.width):
                grid_row.append(0)
            grid.append(grid_row)
            grid_row = []

        return grid

    def create_water(self, file):
        """
        Creates different waterbodies.
        """

        water = file
        first_length_position = None
        first_width_position = None
        last_width_position = None

        waterlist = []
        rows = []
        places = []

        # Creates the water and checks if there is nothing there.
        for row in range(len(self.grid)):

            # Get the first position of the length to check.
            if first_length_position == None:
                first_length_position = row

            if water.length > (row - first_length_position) \
            and first_length_position != None:

                # Checks the width.
                for place, item in enumerate(self.grid[0]):
                    if item == 0 and first_width_position == None:
                        first_width_position = place
                        self.grid[row][place] = 1
                        rows.append(row)
                        places.append(place)

                    elif first_width_position != None and place >= first_width_position \
                    and water.width > (place - first_width_position):
                        self.grid[row][place] = 1
                        self.grid[row][place] = 1
                        rows.append(row)
                        places.append(place)

        # Makes a list with the x and y coordinates of the water.
        waterlist.append(rows)
        waterlist.append(places)

        # Calculates the surface.
        surface = water.length * water.width
        return surface, waterlist


    def create_little_house(self, file):
        """
        Creates little homes (single-family homes).
        """

        little_house = file
        coordinates = self.coordinates["little"]

        # Defines the coordinates for the houses.
        for number in range(len(coordinates)):

            # coordinates, navragen of library beter is !!!!!!!!!!
            coordinate = coordinates[number]
            y_axis = round(coordinate["y"])
            x_axis = round(coordinate["x"])
            first_length_position = None
            first_width_position = None

            # Import the grid and put the houses in the right spaces.
            for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places !!!!!!
                if first_length_position == None and row == y_axis : # nog nakijken of de huizen goed positioneerd !!!!!!!!!!!
                    first_length_position = row

                # Get first x position.
                if first_length_position != None and \
                first_length_position + little_house.length > row :
                    for place in range(len(self.grid[0])):

                        # Fill the first x position.
                        if self.grid[row][place] not in range(1, 5) and first_width_position == None and place == x_axis:
                            first_width_position = place
                            self.grid[row][place] = 2

                        # Fill the grid in with houses.
                        elif first_width_position != None and self.grid[row][place] not in range(1, 5) and \
                        first_width_position + little_house.width > place and place - first_width_position >= 0:
                            self.grid[row][place] = 2

    def create_medium_house(self, file):
        """
        Creates medium homes (bungalows).
        """

        medium_house = file
        coordinates = self.coordinates["medium"]
        print(coordinates)

        # Defines the coordinates for the houses.
        for number in range(len(coordinates)):

            coordinate = coordinates[number]
            y_axis = round(coordinate["y"])
            x_axis = round(coordinate["x"])
            first_length_position = None
            first_width_position = None

            # Imports the grid and puts the houses in the right spaces.
            for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places !!!!!!
                if first_length_position == None and row == y_axis : # nog nakijken of de huizen goed positioneerd !!!!!!!!
                    first_length_position = row

                # Get first x position.
                if first_length_position != None and \
                first_length_position + medium_house.length > row :
                    for place in range(len(self.grid[0])):

                        # Fill the first x position.
                        if self.grid[row][place] not in range(1, 5) and first_width_position == None and place == x_axis:
                            first_width_position = place
                            self.grid[row][place] = 3

                        # Fill the grid in with houses.
                        elif first_width_position != None and self.grid[row][place] not in range(1, 5) and \
                        first_width_position + medium_house.width > place and place - first_width_position >= 0:
                            self.grid[row][place] = 3


    def create_large_house(self, file):
        """
        Creates large homes (maisons).
        """

        large_house = file
        coordinates = self.coordinates["large"]

        # Defines the coordinates for the houses.
        for number in range(len(coordinates)):

            # coordinates, navragen of library beter is !!!!!!!!
            coordinate = coordinates[number]
            y_axis = round(coordinate["y"])
            x_axis = round(coordinate["x"])
            first_length_position = None
            first_width_position = None

            # Import the grid and put the houses in the right spaces.
            for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places !!!!!!!!
                if first_length_position == None and row == y_axis : # nog nakijken of de huizen goed positioneerd !!!!!!!!!
                    first_length_position = row

                # Get first x position.
                if first_length_position != None and \
                first_length_position + large_house.length > row :
                    for place in range(len(self.grid[0])):

                        # Fill the first x position.
                        if self.grid[row][place] not in range(1, 5) and first_width_position == None and place == x_axis:
                            first_width_position = place
                            self.grid[row][place] = 4

                        # Fill the grid in with houses.
                        elif first_width_position != None and self.grid[row][place] not in range(1, 5) and \
                        first_width_position + large_house.width > place and place - first_width_position >= 0:
                            self.grid[row][place] = 4

class Visualator(object):
    """
    Visualizes the grid with houses and water.
    """

    def __init__(self, grid, little_house, medium_house, large_house):
        self.grid = grid
        self.little_house = little_house
        self.medium_house = medium_house
        self.large_house = large_house

    def bokeh(self):
        graph = figure(title = "Amstelhaege")

        # Get x values for the bokeh figure.
        x_axis = self.grid[-1]
        first_x = x_axis.index(x_axis[0])
        last_x = None
        for count, values in enumerate(x_axis):
            last_x = count + 1

        # Get y values for graph.
        y_axis = self.grid
        first_y = y_axis.index(y_axis[0])
        last_y = None
        for count, values in enumerate(y_axis):
            last_y = count + 1

        # Makes the graph and changes the aesthetics if the graph.
        graph.x_range = Range1d(last_x, first_x)
        graph.y_range = Range1d(last_y, first_y)

        # Makes a waterbody and datapoints.
        water_first_x = None
        water_first_y = None
        water_last_x = None
        water_last_y = None

        # Makes the datapoints.
        for y, list in enumerate(self.grid):

            # misschien dubble loepen !!!!!!!!!!!!!!!!
            # Makes a waterbody.
            if 1 in list and water_first_x == None:
                water_first_x = list[::1].index(1)
                water_first_y = y + 1
            elif 1 in list:
                water_last_x = len(list) - list[::-1].index(1)
                water_last_y = y + 1

        # Checks if water exist and prints the ground.
        if water_first_x != None:

            # Makes a ground plan polygon.
            graph.patch(x=[first_x, first_x, last_x, last_x],
                        y=[first_y, last_y, last_y, first_y],
                        color="grey")

            # Makes a water polygon.
            graph.patch(x=[water_first_x, water_first_x, water_last_x, water_last_x],
                        y=[water_first_y, water_last_y, water_last_y, water_first_y],
                        color="blue", line_color="black")

        # Puts the houses into the graph.
        for sort in grid.coordinates.keys():
            color = None

            for house in grid.coordinates[sort]:
                try:
                    if sort in "little":
                        color = "red"
                    elif sort in "medium":
                        color = "yellow"
                    else:
                        color = "green"
                    graph.patch(x=[house["x"], house["x"], (house["x"] + self.little_house.width), (house["x"] + self.little_house.width)],
                                y=[house["y"], (house["y"] + self.little_house.length), (house["y"] + self.little_house.length), house["y"]],
                                color=color, line_color="black")


                except:
                    print("No valid coordinates")

        return graph


if __name__ == "__main__":
    total_houses = 20
    grid = Grid(180, 160)
    # grid.load_csv()

    create_water = grid.create_water(Water(60, 100))
    grid.make_csv()
    grid.create_little_house(LittleHouse(total_houses, 8, 8, 285000, 2))
    grid.create_medium_house(MediumHouse(total_houses, 10, 7.5, 399000))
    grid.create_large_house(LargeHouse(total_houses, 11, 10.5, 610000))


    x = Visualator(grid.grid, LittleHouse(total_houses, 8, 8, 285000, 2), MediumHouse(total_houses, 10, 7.5, 399000), LargeHouse(total_houses, 11, 10.5, 610000))
    show(x.bokeh())
