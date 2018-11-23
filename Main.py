import pathlib
import sys


path = pathlib.Path.cwd()
path = pathlib.Path(path).iterdir()
for submap in path:
    sys.path.append(str(submap))

from grid_houses import *
from classes import *
# from grid_houses import Grid, Visualator

def Main():
        total_houses = 20
        grid = Grid(180, 160)
        # grid.load_csv()
        water = Water(60, 100)
        create_water = grid.create_water(water)
        grid.make_csv()
        grid.create_little_house(LittleHouse(total_houses, 8, 8, 285000, 2))
        grid.create_medium_house(MediumHouse(total_houses, 10, 7.5, 399000))
        grid.create_large_house(LargeHouse(total_houses, 11, 10.5, 610000))


        x = Visualator(grid, LittleHouse(total_houses, 8, 8, 285000, 2), MediumHouse(total_houses, 10, 7.5, 399000), LargeHouse(total_houses, 11, 10.5, 610000))
        show(x.bokeh())

if __name__ == "__main__":
    Main()
