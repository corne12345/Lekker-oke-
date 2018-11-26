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

def Main():
        total_houses = 20
        grid = Grid(180, 160)
        grid.create_water(Water(60, 100))
        grid.make_csv()
        grid.create_house(LittleHouse(total_houses, 8, 8, 285000, 2),
                          MediumHouse(total_houses, 10, 7.5, 399000),
                          LargeHouse(total_houses, 11, 10.5, 610000),
                          Water(60, 100))

        model = Visualator(grid, LittleHouse(total_houses, 8, 8, 285000, 2),
                             MediumHouse(total_houses, 10, 7.5, 399000),
                             LargeHouse(total_houses, 11, 10.5, 610000),
                             Water(60, 100))
        show(model.bokeh())

if __name__ == "__main__":
    Main()
