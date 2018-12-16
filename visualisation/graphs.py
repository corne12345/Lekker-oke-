import csv
from bokeh.io import export_png
from bokeh.plotting import figure, output_file, show

class Graph(object):
    """
    Gives the data of a csv.
    """

    def __init__(self):
        self.bokeh(self.load_csv("visualisation_hill.csv"))

    def load_csv(self, data):
        iteration = []
        value = []

        # Reads the values in the data.
        with open(data, "r") as data:
            reader = csv.reader(data)
            for line in reader:
                line = line[0].split(";")
                try:
                    value.append(int(line[0]))
                    iteration.append(int(line[1]))
                except:
                    print("No number")

        return iteration, value

    def bokeh(self, data):
        """
        Makes a bokeh plot from the data.
        """

        iteration, value = data
        graph = figure(plot_width=1600, plot_height=1600)

        graph.line(value, iteration, line_width=2)

        export_png(graph, filename="hillclimber.png")

if __name__ == "__main__":
    Graph()
