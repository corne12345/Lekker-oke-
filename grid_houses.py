from bokeh.plotting import figure, output_file, show

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


        graph.multi_polygons(xs=[[[[first_x, first_x, last_x, last_x]]]],
                             ys=[[[[first_y, last_y, last_y, first_y]]]],
                             color="green")
        return graph
if __name__ == "__main__":
    grid = Grid(160, 180).grid
    x = Visualator(grid)
    show(x.bokeh())
