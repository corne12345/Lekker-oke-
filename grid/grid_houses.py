import sys

# get the path to the classes
sys.path.append(sys.path[0].replace('\\grid', '\\classes'))

from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d
from Opzet import *


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
        return surface


    def create_little_house(self, file):
        little_house = file
        first_length_position = None
        first_width_position = None
        h_check = []

        # import the grid and put the houses in the right spaces
        for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places
            for check in range(1, file.detachement + 1):
                try:
                    if row - check < 0:
                        h_check.append(None)
                    else:
                        h_check.append(self.grid[row - check][0])
                except:
                    h_check.append(None)

            if None not in h_check:
                if first_length_position == None: # nog nakijken of de huizen goed positioneerd
                    first_length_position = row

            if first_length_position != None and \
            little_house.length > (row - first_length_position):
                for place in range(len(self.grid[0])):
                    if self.grid[row][place] not in range(1, 5) and first_width_position == None:
                        first_width_position = place
                        self.grid[row][place] = 2
                    elif self.grid[row][place] not in range(1, 5) and \
                    little_house.width > (place - first_width_position):
                        self.grid[row][place] = 2
            h_check = []


        # import the grid and put the houses in the right spaces
        for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places
            if first_length_position == None: # nog nakijken of de huizen goed positioneerd
                first_length_position = row

            if little_house.length > (row - first_length_position) and \
            first_length_position != None:
                for place in range(len(self.grid[0])):
                    if self.grid[row][place] not in range(1, 5) and first_width_position == None:
                        first_width_position = place
                        self.grid[row][place] = 2

                    elif self.grid[row][place] not in range(1, 5) and \
                    little_house.width > (place - first_width_position):
                        self.grid[row][place] = 2

    def create_medium_house(self, file):
        """
        Creates medium homes (bungalows)
        """

        medium_house = file
        first_length_position = None
        first_width_position = None


        # import the grid and put the houses in the right spaces
        for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places
            if first_length_position == None: # nog nakijken of de huizen goed positioneerd
                first_length_position = row

            if medium_house.length > (row - first_length_position) and \
            first_length_position != None:
                for place in range(len(self.grid[0])):
                    if self.grid[row][place] not in range(1, 5) and first_width_position == None:
                        first_width_position = place
                        self.grid[row][place] = 3

                    elif self.grid[row][place] not in range(1, 5) and \
                    medium_house.width > (place - first_width_position):
                        self.grid[row][place] = 3

    def create_large_house(self, file):
        """
        Creates large homes (maisons)
        """

        large_house = file
        first_length_position = None
        first_width_position = None


        # import the grid and put the houses in the right spaces
        for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places
            if first_length_position == None: # nog nakijken of de huizen goed positioneerd
                first_length_position = row

            if large_house.length > (row - first_length_position) and \
            first_length_position != None:
                for place in range(len(self.grid[0])):
                    if self.grid[row][place] not in range(1, 5) and first_width_position == None:
                        first_width_position = place
                        self.grid[row][place] = 4

                    elif self.grid[row][place] not in range(1, 5) and \
                    large_house.width > (place - first_width_position):
                        self.grid[row][place] = 4

# Checks if the conditions are fine
class Check(object):
    def __init__(self, water_class, grid, file):
        self.surface = grid.width * grid.length
        self.properties = file
        self.check_water = self.check_water_surface(water_class, 0.2)

    # checks if the ratio is right and there is enough surface
    def check_water_surface(self, surface, percentage):

        # ratio of the surface
        ratio = self.properties.length / self.properties.width
        if surface >= self.surface * percentage and ratio <= 4:
            return True
        else:
            return False

# Visualizes the graph
class Visualator(object):
    def __init__(self, grid):
        self.grid = grid

    def bokeh(self):
        graph = figure(title = "Amstelhaege")

        # get x values for the bokeh figure
        x_axis = self.grid[-1]
        first_x = x_axis.index(x_axis[0]) + 1
        last_x = None
        for count, values in enumerate(x_axis):
            last_x = count + 1

        # get y values for graph
        y_axis = self.grid
        first_y = y_axis.index(y_axis[0]) + 1
        last_y = None
        for count, values in enumerate(y_axis):
            last_y = count + 1

        # makes the  graph and changes the aesthetics if the graph
        graph.x_range = Range1d(last_x, first_x)
        graph.y_range = Range1d(last_y, first_y)

        # makes a waterbody and datapoints
        water_first_x = None
        water_first_y = None
        water_last_x = None
        water_last_y = None

        #  makes variables for little houses (single family homes)
        little_house_first_x = None
        little_house_first_y = None
        little_house_last_x = None
        little_house_last_y = None

        #  make variables for medium houses (bungalows)
        medium_house_first_x = None
        medium_house_first_y = None
        medium_house_last_x = None
        medium_house_last_y = None

        #  make variables for large houses (maisons)
        large_house_first_x = None
        large_house_first_y = None
        large_house_last_x = None
        large_house_last_y = None

        # makes the datapoints
        for y, list in enumerate(self.grid):

            # misschien dubble loepen
            # make water body
            if 1 in list and water_first_x == None:
                water_first_x = list[::1].index(1)
                water_first_y = y + 1
            elif 1 in list:
                water_last_x = len(list) - list[::-1].index(1)
                water_last_y = y + 1

            # makes postion of the little houses (single homes)
            if 2 in list and little_house_first_x == None:
                little_house_first_x = list[::1].index(2)
                little_house_first_y = y + 1
            elif 2 in list:
                little_house_last_x = len(list) - list[::-1].index(2)
                little_house_last_y = y + 1

            # makes position of the medium houses (bungalow)
            if 3 in list and medium_house_first_x == None:
                medium_house_first_x = list[::1].index(3)
                medium_house_first_y = y + 1
            elif 3 in list:
                medium_house_last_x = len(list) - list[::-1].index(3)
                medium_house_last_y = y + 1

            # makes postion of the large houses (maison)
            if 4 in list and large_house_first_x == None:
                large_house_first_x = list[::1].index(4)
                large_housen_first_y = y + 1
            elif 4 in list:
                large_house_last_x = len(list) - list[::-1].index(4)
                large_house_last_y = y + 1

        # checks if water exist and print the ground
        if water_first_x != None and little_house_first_x != None \
        and medium_house_first_x != None and large_house_first_x != None:

            # makes ground plan polygon
            graph.patch(x=[first_x, first_x, last_x, last_x],
                        y=[first_y, last_y, last_y, first_y],
                        color="grey")

            # makes water polygon
            graph.patch(x=[water_first_x, water_first_x, water_last_x, water_last_x],
                        y=[water_first_y, water_last_y, water_last_y, water_first_y],
                        color="blue" )

            # makes little house (single family home) polygon
            graph.patch(x=[little_house_first_x, little_house_first_x, little_house_last_x, little_house_last_x],
                        y=[little_house_first_y, little_house_last_y, little_house_last_y, little_house_first_y],
                        color="red")

            # makes medium house (bungalow) polygon
            graph.patch(x=[medium_house_first_x, medium_house_first_x, medium_house_last_x, medium_house_last_x],
                        y=[medium_house_first_y, medium_house_last_y, medium_house_last_y, medium_house_first_y],
                        color="yellow")

            # makes large house (maison) polygon
            graph.patch(x=[large_house_first_x, large_house_first_x, large_house_last_x, large_house_last_x],
                        y=[large_house_first_y, large_house_last_y, large_house_last_y, large_house_first_y],
                        color="green")

        # prints only the ground
        else:
            graph.multi_polygons(xs=[[[[first_x, first_x, last_x, last_x]]]],
                                 ys=[[[[first_y, last_y, last_y, first_y]]]],
                                 color="grey")
        return graph


if __name__ == "__main__":
    total_houses = 20
    grid = Grid(160, 180)
    water = Water(60, 100)
    water2 = Water(50, 50)
    grid.create_little_house(SingleHome(total_houses, 8, 8, 285000, 2))
    grid.create_medium_house(Bungalow(total_houses, 10, 7.5, 399000))
    grid.create_large_house(Maison(total_houses, 11, 10.5, 610000))
    create_water = grid.create_water(water)

    check = Check(create_water, grid, water)
    if check.check_water is True:
        grid_end = grid.grid
        x = Visualator(grid_end)
        show(x.bokeh())
    else:
        print("ERROR JOE")
