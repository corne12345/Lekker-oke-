from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d
from Opzet import Water


# 1 = waterbody
# 2 = single home
# 3 = bungalow
# 4 = maison
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

    # creates different_water_bodies
    def create_water(self, file):
        water = file
        first_length_position = None
        first_width_position = None

        for row in range(len(self.grid)): # length
            if first_length_position == None:
                first_length_position = row
            elif water.length > (row - first_length_position):
                for place, item in enumerate(self.grid[0]): # width
                    if self.grid[row][place] == 0 and first_width_position == None:
                        self.grid[row][place] = 1
                        first_width_position = self.grid[row][place]

                    elif water.width > (place - first_width_position):
                        self.grid[row][place] = 1

        surface = water.length * water.width
        return surface


    def create_bungalow(self, file):
        bungalow = file
        print("")


class Check(object):
    def __init__(self, water_class, grid, file):
        self.surface = grid.width * grid.length
        self.properties = file
        self.check_water = self.check_water_surface(water_class, 0.2)


    def total_surface_water(self):
        print("")

    def check_water_surface(self, surface, percentage):
        # ratio of the surface
        ratio = self.properties.length / self.properties.width
        if surface >= self.surface * percentage and ratio <= 4:
            return True
        else:
            return False




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

        # makes the graph and changes the aesthetics if the graph
        graph.x_range = Range1d(last_x, first_x)
        graph.y_range = Range1d(last_y, first_y)

        # makes a waterbody and datapoints
        water_first_x = None
        water_first_y = None
        water_last_x = None
        water_last_y = None
        for y, list in enumerate(self.grid):
            if 1 in list and water_first_x == None:
                water_first_x = list[::1].index(1) + 1
                water_first_y = y + 1
            elif 1 in list:
                water_last_x = len(list) - list[::-1].index(1)
                water_last_y = y + 1

        # checks if water exist and print the ground
        if water_first_x != None:

            # makes ground plan polygon
            graph.multi_polygons(xs=[[[ [first_x, first_x, last_x, last_x],
                                    [water_first_x, water_first_x, water_last_x, water_last_x]  ]]],
                                 ys=[[[ [first_y, last_y, last_y, first_y],
                                    [water_first_y, water_last_y, water_last_y, water_first_y]  ]]],
                                color="grey")

            # makes water polygon
            graph.patch(x=[water_first_x, water_first_x, water_last_x, water_last_x],
                        y=[water_first_y, water_last_y, water_last_y, water_first_y],
                        color="blue" )

        # prints only the ground
        else:
            graph.multi_polygons(xs=[[[[first_x, first_x, last_x, last_x]]]],
                                 ys=[[[[first_y, last_y, last_y, first_y]]]],
                                 color="green")
        return graph


if __name__ == "__main__":

    grid = Grid(160, 180)
    water = Water(60, 100)
    x = grid.create_water(water)

    check = Check(x, grid, water)
    if check.check_water is True:
        grid_end = grid.grid
        x = Visualator(grid_end)
        show(x.bokeh())
    else:
        print("ERROR JOE")
