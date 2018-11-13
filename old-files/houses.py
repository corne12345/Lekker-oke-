from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d
from Opzet import SingleHome
from Opzet import Bungalow
from Opzet import Maison
from grid_houses import Grid

class House(object):
    def __init__(self, grid):
        self.grid = grid

    def create_single_home(self, file):
        house = file

        # import the grid and put the houses in the right spaces
        for place, row in enumerate(self.grid): # to do iterate over the grid to put the houses on the right places
            print(place, row) # print the place
        for row in range(house.length):
            for place in range(house.width):
                if grid[row][place] != 2:
                    grid[row][place] = 2
        surface = house.length * house.width
        return surface

    def create_bungalow(self, file):
        house = file
        for row in range(int(house.length)):
            for place in range(int(house.width)):
                if grid[row][place] is 0:
                    grid[row][place] = 3
                else:
                    pass
        surface = house.length * house.width
        return surface

    def create_maison(self, file):
        house = file
        for row in range(int(house.length)):
            for place in range(int(house.width)):
                if grid[row][place] != 4:
                    grid[row][place] = 4
        surface = house.length * house.width
        return surface


class Visualator(object):

    def __init__(self, grid, single_home, bungalow, maison):
        self.grid = grid
        self.single_home = single_home
        self.bungalow = bungalow
        self.maison = maison

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

        # makes the graph and changes the aesthetics if the graph
        graph.x_range = Range1d(last_x, first_x)
        graph.y_range = Range1d(last_y, first_y)

        graph = figure(title = "Amstelhaege")
        print(self.grid)
        # makes houses and datapoints
        single_home_first_x = 0
        single_home_first_y = 0
        single_home_last_x = single_home_first_x + self.single_home.width
        single_home_last_y = single_home_first_y + self.single_home.length

        bungalow_first_x = 0
        bungalow_first_y = 0
        bungalow_last_x = single_home_first_x + self.bungalow.width
        bungalowe_last_y = single_home_first_y + self.bungalow.length

        maison_first_x = 0
        maison_first_y = 0
        maison_last_x = maison_first_x + self.maison.width
        maison_last_y = maison_first_y + self.maison.length


        for y, list in enumerate(self.grid):
            if 2 in list and single_home_first_x == 0:
                single_home_first_x = list[::1].index(2) + 1
                single_home_first_y = y + 1

            elif 2 in list:
                single_home_last_x = len(list) - list[::-1].index(2)
                single_home_last_y = y + 1

            elif 3 in list and bungalow_first_x == 0:
                bungalow_first_x = list[::1].index(3) + 1
                bungalow_first_y = y + 1

            elif 3 in list:
                bungalow_last_x = len(list) - list[::-1].index(3)
                bungalow_last_y = y + 1

            elif 4 in list and maison_first_x == 0:
                maison_first_x = list[::1].index(4) + 1
                maison_first_y = y + 1

            elif 4 in list:
                maison_last_x = len(list) - list[::-1].index(4)
                maison_last_y = y + 1

        # checks if a home exist and print the ground
        if single_home_first_x != 0:
            graph.multi_polygons(xs=[[[ [first_x, first_x, last_x, last_x], [single_home_first_x, single_home_first_x, single_home_last_x, single_home_last_x] ]]],
                                 ys=[[[ [first_y, last_y, last_y, first_y], [single_home_first_y, single_home_last_y, single_home_last_y, single_home_first_y] ]]],
                                 color="grey")
            graph.patch(x=[single_home_first_x, single_home_first_x, single_home_last_x, single_home_last_x], y=[single_home_first_y, single_home_last_y, single_home_last_y, single_home_first_y], color="red")

        elif bungalow_first_x != 0:
            graph.multi_polygons(xs=[[[ [first_x, first_x, last_x, last_x], [bungalow_first_x, bungalow_first_x, bungalow_last_x, bungalow_last_x] ]]],
                                 ys=[[[ [first_y, last_y, last_y, first_y], [bungalow_first_y, bungalow_last_y, bungalow_last_y, bungalow_first_y] ]]],
                                 color="grey")
            graph.patch(x=[bungalow_first_x, bungalow_first_x, bungalow_last_x, bungalow_last_x], y=[bungalow_first_y, bungalow_last_y, bungalow_last_y, bungalow_first_y], color="yellow")

        elif maison_first_x != 0:
            graph.multi_polygons(xs=[[[ [first_x, first_x, last_x, last_x], [maison_first_x, maison_first_x, maison_last_x, maison_last_x] ]]],
                                 ys=[[[ [first_y, last_y, last_y, first_y], [maison_first_y, maison_last_y, maison_last_y, maison_first_y] ]]],
                                 color="grey")
            graph.patch(x=[maison_first_x, maison_first_x, maison_last_x, maison_last_x], y=[maison_first_y, maison_last_y, maison_last_y, maison_first_y], color="green")

        # prints only the ground
        else:
            graph.multi_polygons(xs=[[[[first_x, first_x, last_x, last_x]]]],
                                 ys=[[[[first_y, last_y, last_y, first_y]]]],
                                 color="grey")

        return graph

if __name__ == "__main__":

    # define houses
    total_homes = 20
    grid = Grid(160, 180).grid
    house = House(grid)
    y = house.create_single_home(SingleHome(total_homes, 8, 8, 285000))
    x = Visualator(grid, SingleHome(total_homes, 8, 8, 285000), Bungalow(total_homes, 10, 7.5, 399000), Maison(total_homes, 11, 10.5, 610000))
    y = house.create_bungalow(Bungalow(total_homes, 10, 7.5, 399000))
    y = house.create_maison(Maison(total_homes, 11, 10.5, 610000))
    show(x.bokeh())
