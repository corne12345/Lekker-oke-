import pathlib as pathlib
import sys
from bokeh.plotting import show
# # get the path to the classes
path = pathlib.Path.cwd()
path = pathlib.Path(path).iterdir()
for submap in path:
    sys.path.append(str(submap))

from grid_houses import Grid, Visualator
from Opzet import LittleHouse, MediumHouse, LargeHouse, Water
from greedy import Greed
from score_function_new import random_to_vis
from hillclimber_corne import hillclimber

def Main(algorithm):
        total_houses = 20
        grid = Grid(180, 160)
        grid.create_water(Water(60, 100))
        # grid.make_csv()

        if algorithm == "greedy":
            coordinates = Greed(grid, LittleHouse(total_houses, 8, 8, 285000, 2, 0.03),
                          MediumHouse(total_houses, 10, 7.5, 399000, 3, 0.04),
                          LargeHouse(total_houses, 11, 10.5, 610000, 6, 0.06)).coordinates

        elif algorithm == "hillclimber":
            coordinates = hillclimber(1000, 3, 100, True)

        # elif algorithm == "random":
        #     coordinates = None
        #     grid.create_house(grid, LittleHouse(total_houses, 8, 8, 285000, 2, 0.03),
        #                              MediumHouse(total_houses, 10, 7.5, 399000, 3, 0.04),
        #                              LargeHouse(total_houses, 11, 10.5, 610000, 6, 0.06))


        model = Visualator(grid, LittleHouse(total_houses, 8, 8, 285000, 2, 0.03),
                                 MediumHouse(total_houses, 10, 7.5, 399000, 3, 0.04),
                                 LargeHouse(total_houses, 11, 10.5, 610000, 6, 0.06),
                                 Water(60, 100), coordinates)
        show(model.bokeh())

if __name__ == "__main__":
    Main("hillclimber")
