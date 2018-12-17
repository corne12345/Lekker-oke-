import csv
from bokeh.io import export_png
from bokeh.plotting import figure, output_file, show

class Graph(object):
    """
    Gives the data of a csv.
    """

    def make_csv(self, score, name):
        name = name + str(max(score)) + ".csv"
        with open(name, "w") as infile:
            writer = csv.writer(infile, delimiter=",")
            for count in range(len(score)):
                writer.writerow([count + 1, score[count]])

        return name

    def load_csv(self, file):
        value = []
        iteration = []
        # Reads the values in the data.
        with open(file, "r") as data:
            reader = csv.reader(data)
            for line in reader:
                print(line)
                try:
                    value.append(float(line[1]))
                    iteration.append(int(line[0]))
                except:
                    print("No number")

        return iteration, value

    def bokeh(self, data, name):
        """
        Makes a bokeh plot from the data.
        """

        iteration, value = data
        graph = figure(plot_width=1600, plot_height=1600)

        for count in range(len(value)):
            graph.scatter(iteration[count], value[count], marker="circle", size=15,
                          line_color="navy", fill_color="orange", alpha=0.5)


        export_png(graph, name + str(max(value)) + ".png")

if __name__ == "__main__":
    Graph()
