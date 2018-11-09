from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d
from Opzet import Water

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
            for pixel in range(selb f.width):
                grid_row.append(0)
            grid.append(grid_row)
            grid_row = []
        return grid

    # creates different_water_bodies
    def create_water(self, file):
        water = file
        for row in range(water.length):
            for place in range(water.width):
                if self.grid[row][place] != 1:
                    self.grid[row][place] = 1
        surface = water.length * water.width
        return surface

class Check(object):
    def __init__(self, surface_water, grid):
        self.surface = grid.width * grid.length
        self.check_water = self.check_water_surface(surface_water, 0.2)

    def total_surface water(self):
        print("")

    def check_water_surface(self, surface, percentage):
        if surface >= self.surface * percentage:
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
            graph.multi_polygons(xs=[[[ [first_x, first_x, last_x, last_x], [water_first_x, water_first_x, water_last_x, water_last_x]  ]]],
                                 ys=[[[ [first_y, last_y, last_y, first_y], [water_first_y, water_last_y, water_last_y, water_first_y]  ]]],
                                color="green")
            graph.patch(x=[water_first_x, water_first_x, water_last_x, water_last_x], y=[water_first_y, water_last_y, water_last_y, water_first_y], color="blue" )

        # prints only the ground
        else:
            graph.multi_polygons(xs=[[[[first_x, first_x, last_x, last_x]]]],
                                 ys=[[[[first_y, last_y, last_y, first_y]]]],
                                 color="green")



        return graph
if __name__ == "__main__":

    grid = Grid(160, 180)
    x = grid.create_water(Water(6, 100))
    check = Check(x, grid)
    if check.check_water is True:
        grid_end = grid.grid
        x = Visualator(grid_end)
        show(x.bokeh())
    else:
        print("ERROR JOE")
