import sys

# get the path to the classes
sys.path.append(sys.path[0].replace('\\grid', '\\classes'))

from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d
from Opzet import *


# 1 = waterbody
# 2 = single home
# 3 = bungalow
# 4 = maison
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

        # creates the wwater and check if there is nothing there
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


    def create_single_home(self, file):
        """
        Creates small homes (single family homes)
        """

        single_home = file
        first_length_position = None
        first_width_position = None

        # import the grid and put the houses in the right spaces
        for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places
            if first_length_position == None: # nog nakijken of de huizen goed positioneerd
                first_length_position = row

            if single_home.length > (row - first_length_position) and \
            first_length_position != None:
                for place in range(len(self.grid[0])):
                    if self.grid[row][place] not in range(1, 5) and first_width_position == None:
                        first_width_position = place
                        self.grid[row][place] = 2

                    elif self.grid[row][place] not in range(1, 5) and \
                    single_home.width > (place - first_width_position):
                        self.grid[row][place] = 2

    def create_bungalow(self, file):
        """
        Creates medium homes (bungalows)
        """

        bungalow = file
        first_length_position = None
        first_width_position = None


        # import the grid and put the houses in the right spaces
        for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places
            if first_length_position == None: # nog nakijken of de huizen goed positioneerd
                first_length_position = row

            if bungalow.length > (row - first_length_position) and \
            first_length_position != None:
                for place in range(len(self.grid[0])):
                    if self.grid[row][place] not in range(1, 5) and first_width_position == None:
                        first_width_position = place
                        self.grid[row][place] = 3

                    elif self.grid[row][place] not in range(1, 5) and \
                    bungalow.width > (place - first_width_position):
                        self.grid[row][place] = 3

    def create_maison(self, file):
        """
        Creates large homes (maisons)
        """

        maison = file
        first_length_position = None
        first_width_position = None


        # import the grid and put the houses in the right spaces
        for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places
            if first_length_position == None: # nog nakijken of de huizen goed positioneerd
                first_length_position = row

            if maison.length > (row - first_length_position) and \
            first_length_position != None:
                for place in range(len(self.grid[0])):
                    if self.grid[row][place] not in range(1, 5) and first_width_position == None:
                        first_width_position = place
                        self.grid[row][place] = 4

                    elif self.grid[row][place] not in range(1, 5) and \
                    maison.width > (place - first_width_position):
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
        single_home_first_x = None
        single_home_first_y = None
        single_home_last_x = None
        single_home_last_y = None

        #  make variables for medium houses (bungalows)
        bungalow_first_x = None
        bungalow_first_y = None
        bungalow_last_x = None
        bungalow_last_y = None

        #  make variables for large houses (mansions)
        maison_first_x = None
        maison_first_y = None
        maison_last_x = None
        maison_last_y = None

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
            if 2 in list and single_home_first_x == None:
                single_home_first_x = list[::1].index(2)
                single_home_first_y = y + 1
            elif 2 in list:
                single_home_last_x = len(list) - list[::-1].index(2)
                single_home_last_y = y + 1

            # makes position of the medium houses (bungalow)
            if 3 in list and bungalow_first_x == None:
                bungalow_first_x = list[::1].index(3)
                bungalow_first_y = y + 1
            elif 3 in list:
                bungalow_last_x = len(list) - list[::-1].index(3)
                bungalow_last_y = y + 1

            # makes postion of the large houses (maison)
            if 4 in list and maison_first_x == None:
                maison_first_x = list[::1].index(4)
                maison_first_y = y + 1
            elif 4 in list:
                maison_last_x = len(list) - list[::-1].index(4)
                maison_last_y = y + 1

        # checks if water exist and print the ground
        if water_first_x != None and single_home_first_x != None \
        and bungalow_first_x != None and maison_first_x != None:

            # makes ground plan polygon
            graph.patch(x=[first_x, first_x, last_x, last_x],
                        y=[first_y, last_y, last_y, first_y],
                        color="grey")

            # makes water polygon
            graph.patch(x=[water_first_x, water_first_x, water_last_x, water_last_x],
                        y=[water_first_y, water_last_y, water_last_y, water_first_y],
                        color="blue" )

            # makes little house (single familt home) polygon
            graph.patch(x=[single_home_first_x, single_home_first_x, single_home_last_x, single_home_last_x],
                        y=[single_home_first_y, single_home_last_y, single_home_last_y, single_home_first_y],
                        color="red")

            # makes medium house (bungalow) polygon
            graph.patch(x=[bungalow_first_x, bungalow_first_x, bungalow_last_x, bungalow_last_x],
                        y=[bungalow_first_y, bungalow_last_y, bungalow_last_y, bungalow_first_y],
                        color="yellow")

            # makes large house (maison) polygon
            graph.patch(x=[maison_first_x, maison_first_x, maison_last_x, maison_last_x],
                        y=[maison_first_y, maison_last_y, maison_last_y, maison_first_y],
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
    grid.create_single_home(SingleHome(total_houses, 8, 8, 285000, 2))
    grid.create_bungalow(Bungalow(total_houses, 10, 7.5, 399000))
    grid.create_maison(Maison(total_houses, 11, 10.5, 610000))
    create_water = grid.create_water(water)

    check = Check(create_water, grid, water)
    if check.check_water is True:
        grid_end = grid.grid
        x = Visualator(grid_end)
        show(x.bokeh())
    else:
        print("ERROR JOE")
