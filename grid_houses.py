from bokeh.plotting import figure, output_file, show
from bokeh.models import Range1d

class Grid(object):
    def __init__(self, total_length, total_width):
        self.width = total_width
        self.length = total_length
        self.grid = self.grid_command()

    def grid_command(self):
        grid = []
        grid_row = []
        for length in range(self.length):
            for pixel in range(self.width):
                grid_row.append(0)
            grid.append(grid_row)
            grid_row = []
        return grid

    def create_water(self, width, length):
        for row in range(length):
            for place in range(width):
                if self.grid[row][place] != 1:
                    self.grid[row][place] = 1


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
        graph.multi_polygons(xs=[[[[first_x, first_x, last_x, last_x]]]],
                             ys=[[[[first_y, last_y, last_y, first_y]]]],
                             color="green")

        # makes a waterbody
        for y, value in enumerate(self.grid):
            print(y, values)
            for x, value in enumerate(self.grid[y]):
                if value == 1:
                    #print(x, value, end="/")
                    print("", end='')


        return graph
if __name__ == "__main__":

    grid = Grid(160, 180)
    grid.create_water(15, 20)
    grid = grid.grid
    x = Visualator(grid)
    x.bokeh()
    # show(x.bokeh())
