import sys

# get the path to the classes
sys.path.append(sys.path[0].replace('\\grid', '\\classes'))
sys.path.append(sys.path[0].replace('\\grid', '\\coordinates'))


from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d
from Opzet import *
from generator import *


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

    # makes the grid itself
    def grid_command(self):
        grid = []
        grid_row = []
        print(self.length)
        print(self.width)
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
        """
        Creates little homes (single family homes)
        """

        little_house = file
        self.little_coordinates = Coordinates(int(little_house.number), self.length, self.width).coordinates
        coordinates = self.little_coordinates

        for coordinate in coordinates:
            # coordinates, navragen of library beter is
            y_axis = coordinate["y"]
            x_axis = coordinate["x"]
            first_length_position = None
            first_width_position = None

            # import the grid and put the houses in the right spaces
            for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places
                if first_length_position == None and row == y_axis : # nog nakijken of de huizen goed positioneerd
                    first_length_position = row

                if first_length_position != None and \
                first_length_position + little_house.length > row :
                    for place in range(len(self.grid[0])):
                        if self.grid[row][place] not in range(1, 5) and first_width_position == None and place == x_axis:
                            first_width_position = place
                            self.grid[row][place] = 2
                        elif first_width_position != None and self.grid[row][place] not in range(1, 5) and \
                        first_width_position + little_house.width > place and place - first_width_position >= 0:
                            self.grid[row][place] = 2


    def create_medium_house(self, file):
        """
        Creates medium homes (bungalows)
        """

        medium_house = file
        self.medium_coordinates = Coordinates(int(medium_house.number), self.length, self.width).coordinates
        coordinates = self.medium_coordinates

        for coordinate in coordinates:
            # coordinates, navragen of library beter is
            y_axis = coordinate["y"]
            x_axis = coordinate["x"]
            first_length_position = None
            first_width_position = None

            # import the grid and put the houses in the right spaces
            for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places
                if first_length_position == None and row == y_axis : # nog nakijken of de huizen goed positioneerd
                    first_length_position = row

                if first_length_position != None and \
                first_length_position + medium_house.length > row :
                    for place in range(len(self.grid[0])):
                        if self.grid[row][place] not in range(1, 5) and first_width_position == None and place == x_axis:
                            first_width_position = place
                            self.grid[row][place] = 3
                        elif first_width_position != None and self.grid[row][place] not in range(1, 5) and \
                        first_width_position + medium_house.width > place and place - first_width_position >= 0:
                            self.grid[row][place] = 3


    def create_large_house(self, file):
        """
        Creates large homes (maisons)
        """

        large_house = file
        self.large_coordinates = Coordinates(int(large_house.number), self.length, self.width).coordinates
        coordinates = self.large_coordinates

        for coordinate in coordinates:
            # coordinates, navragen of library beter is
            y_axis = coordinate["y"]
            x_axis = coordinate["x"]
            first_length_position = None
            first_width_position = None

            # import the grid and put the houses in the right spaces
            for row in range(len(self.grid)): # to do iterate over the grid to put the houses on the right places
                if first_length_position == None and row == y_axis : # nog nakijken of de huizen goed positioneerd
                    first_length_position = row

                if first_length_position != None and \
                first_length_position + large_house.length > row :
                    for place in range(len(self.grid[0])):
                        if self.grid[row][place] not in range(1, 5) and first_width_position == None and place == x_axis:
                            first_width_position = place
                            self.grid[row][place] = 4
                        elif first_width_position != None and self.grid[row][place] not in range(1, 5) and \
                        first_width_position + large_house.width > place and place - first_width_position >= 0:
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
    def __init__(self, grid, little_house, medium_house, big_house):
        self.grid = grid
        self.little_house = little_house
        self.medium_house = medium_house
        self.big_house = big_house

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

        # makes a waterbody and datapoints
        water_first_x = None
        water_first_y = None
        water_last_x = None
        water_last_y = None

        #  get the coordinates for little houses (single family homes)
        little_coordinates = grid.little_coordinates

        #  get the coordinates for medium houses (bungalows)
        medium_coordinates = grid.medium_coordinates

        # get the coordinates for large houses (maisons)
        large_coordinates = grid.large_coordinates


        # makes postion of the little houses (single homes)
        for y, list in enumerate(self.grid):

            # misschien dubble loepen
            # make water body
            if 1 in list and water_first_x == None:
                water_first_x = list[::1].index(1)
                water_first_y = y
            elif 1 in list:
                water_last_x = len(list) - list[::-1].index(1)
                water_last_y = y

            # makes position of the medium houses (bungalow)
            if 3 in list and medium_house_first_x == None:
                medium_house_first_x = list[::1].index(3)
                medium_house_first_y = y
            elif 3 in list:
                medium_house_last_x = len(list) - list[::-1].index(3)
                medium_house_last_y = y

            # makes postion of the large houses (maison)
            if 4 in list and large_house_first_x == None:
                large_house_first_x = list[::1].index(4)
                large_housen_first_y = y
            elif 4 in list:
                large_house_last_x = len(list) - list[::-1].index(4)
                large_house_last_y = y

        # checks if water exist and print the ground
        if water_first_x != None or little_house_first_x != None \
        and medium_house_first_x != None or large_house_first_x != None:

            # makes ground plan polygon
            graph.patch(x=[first_x, first_x, last_x, last_x],
                        y=[first_y, last_y, last_y, first_y],
                        color="grey")

            # makes water polygon
            graph.patch(x=[water_first_x, water_first_x, water_last_x, water_last_x],
                        y=[water_first_y, water_last_y, water_last_y, water_first_y],
                        color="blue" )

            # makes little house (single family home) polygon
            for house in little_coordinates:
                graph.patch(x=[house["x"], house["x"], (house["x"] + self.little_house.width), (house["x"] + self.little_house.width)],
                            y=[house["y"], (house["y"] + self.little_house.length), (house["y"] + self.little_house.length), house["y"]],
                            color="red")

            # makes medium house (bungalow) polygon
            for house in medium_coordinates:
                graph.patch(x=[house["x"], house["x"], (house["x"] + self.medium_house.width), (house["x"] + self.medium_house.width)],
                            y=[house["y"], (house["y"] + self.medium_house.length), (house["y"] + self.medium_house.length), house["y"]],
                            color="yellow")

            # makes large house (maison) polygon
            for house in medium_coordinates:
                graph.patch(x=[house["x"], house["x"], (house["x"] + self.medium_house.width), (house["x"] + self.medium_house.width)],
                            y=[house["y"], (house["y"] + self.medium_house.length), (house["y"] + self.medium_house.length), house["y"]],
                            color="yellow")

        # prints only the ground
        else:
            graph.multi_polygons(xs=[[[[first_x, first_x, last_x, last_x]]]],
                                 ys=[[[[first_y, last_y, last_y, first_y]]]],
                                 color="grey")
        return graph


if __name__ == "__main__":
    total_houses = 20
    grid = Grid(180, 160)
    water = Water(60, 100)

    grid.create_little_house(LittleHouse(total_houses, 8, 8, 285000, 2))
    grid.create_medium_house(MediumHouse(total_houses, 10, 7.5, 399000, 4))
    grid.create_large_house(LargeHouse(total_houses, 11, 10.5, 610000, 6))
    create_water = grid.create_water(water)

    check = Check(create_water, grid, water)
    if check.check_water is True:
        grid_end = grid.grid
        x = Visualator(grid_end, LittleHouse(total_houses, 8, 8, 285000, 2), MediumHouse(total_houses, 10, 7.5, 399000, 4), LargeHouse(total_houses, 11, 10.5, 610000, 6))
        show(x.bokeh())
    else:
        print("ERROR JOE haha!!!")
