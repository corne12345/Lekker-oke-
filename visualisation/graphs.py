import csv
from bokeh.io import export_png
from bokeh.plotting import figure, output_file, show

class Graph(object):
    def __init__(self):
        self.bokeh(self.load_csv("visualisation_hill.csv"))

    def load_csv(self, data):
        itteration = []
        value = []
        with open(data, "r") as data:
            reader = csv.reader(data)
            for line in reader:
                line = line[0].split(";")
                try:
                    value.append(int(line[0]))
                    itteration.append(int(line[1]))
                except:
                    print("No number")

        return itteration, value

    def bokeh(self, data):
        itteration, value = data
        graph = figure(plot_width=1600, plot_height=1600)

        graph.line(value, itteration, line_width=2)

        export_png(graph, filename="hillclimber.png")



if __name__ == "__main__":
    Graph()
