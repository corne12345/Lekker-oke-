import pathlib as pathlib
import sys
from bokeh.plotting import show

# get the path to the classes
path = pathlib.Path.cwd()
path = pathlib.Path(path).iterdir()
for submap in path:
    sys.path.append(str(submap))

from grid_houses import Grid, Visualator
from Opzet import LittleHouse, MediumHouse, LargeHouse, Water
from greedy_multi import Greed
from score_function_new import random_to_vis, best_of_random, vis_to_random, calc_score_greedy
from hillclimber_corne import hillclimber

def Main(algorithm, reps = 0, steps = 0, randoms = 0):
    """
    Defines the main function that combines all files which eachother.
    """

    total_houses = 20
    grid = Grid(180, 160)
    grid.create_water(Water(60, 100))
    print(algorithm)
    # Defines if a random, greedy or hillclimber algorithm will be used.
    if algorithm == "random":
        counter = 0
        print("How many itterations")
        itterations = input("> ")
        while name.isdigit() == False or int(name) > len(algoritme):
            print("wrong input")
            itterations = input("> ")
        while counter < int(itterations):
            coordinates = best_of_random(1, grid.grid)
            coordinates = random_to_vis(coordinates)
            counter += 1

    elif algorithm == "greedy":
        counter = 0
        print("How many itterations")
        itterations = input("> ")
        while name.isdigit() == False or int(name) > len(algoritme):
            print("wrong input")
            itterations = input("> ")
        while counter < int(itterations):
            coordinates = Greed(grid, LittleHouse(total_houses, 8, 8, 285000, 2, 0.03),
                          MediumHouse(total_houses, 10, 7.5, 399000, 3, 0.04),
                          LargeHouse(total_houses, 11, 10.5, 610000, 6, 0.06), 1).coordinates
            calc_score_greedy(coordinates)
            counter += 1

    elif algorithm == "hillclimber":
        coordinates = hillclimber(500, 3, 10, True)

    # elif algorithm == "random":                   !!!!!!!!!!! WEG? !!!!!!!!!!!!!!!!!!!!!!!!!
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
    algoritme = ["random", "greedy", "hillclimber"]
    print("Which algoritme do you want to use for you building plan")
    print("1 = random")
    print("2 = greedy")
    print("3 = hillclimber")
    name = input("> ")
    print(name.isdigit())
    while name.isdigit() == False or int(name) > len(algoritme):
        print("wrong input")
        name = input("> ")
    Main(algoritme[int(name) - 1])
    # Main("greedy")
