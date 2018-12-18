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
from greedy import Greed
from score_function_new import newScore
from hillclimber_corne import hillclimber
from graphs import Graph
from dept_first import Depthfirst

def Main(algorithm, reps = 0, steps = 0, randoms = 0):
    """
    Defines the main function that combines all files which eachother.
    """

    print("How many houses do you want?")
    total_houses = input("> ")
    while total_houses.isdigit() == False:
        print("Wrong Input")
        total_houses = input("> ")

    total_houses = int(total_houses)
    grid = Grid(180, 160)
    grid.create_water(Water(60, 100))
    score_function = newScore(grid,  LittleHouse(total_houses, 8, 8, 285000, 2, 0.03),
                                     MediumHouse(total_houses, 10, 7.5, 399000, 3, 0.04),
                                     LargeHouse(total_houses, 11, 10.5, 610000, 6, 0.06))
    list_houses = {"little": LittleHouse(total_houses, 8, 8, 285000, 2, 0.03),
                   "medium":MediumHouse(total_houses, 10, 7.5, 399000, 3, 0.04),
                   "large":LargeHouse(total_houses, 11, 10.5, 610000, 6, 0.06) }

    # Calls random algorithm.
    if algorithm == "random":
        score_list = []
        counter = 0

        print("How many itterations?")
        itterations = input("> ")
        while name.isdigit() == False or int(name) <= 0:
            print("wrong input")
            itterations = input("> ")

        while counter < int(itterations):
            coordinates = score_function.best_of_random(1)
            print(coordinates)
            score_list.append(coordinates[0])
            counter += 1
            coordinates = coordinates[2]

        print("Do you want to make a graph? y/n")
        graph = input("> ").strip()
        graph = graph.lower()
        yes_no = ["n", "y"]
        while graph not in yes_no:
            graph = input("> ")
            graph = graph.lower()

        if graph == "n":
            pass
        else:
            file = Graph().make_csv(score_list, algorithm)
            Graph().bokeh(Graph().load_csv(file), algorithm)

    # Calls depth first.
    elif algorithm == "depthfirst":
        depth = Depthfirst(8, grid.length, grid.width, grid.grid)
        first = depth.create_coordinates()
        depth.create_coordinates_2(first)

    # Calls greedy algorithm.
    elif algorithm == "greedy":
        counter = 0
        score_list = []
        print("How many itterations?")
        itterations = input("> ")
        while name.isdigit() == False or 0 > int(name) > len(algoritme):
            print("wrong input")
            itterations = input("> ")
        while counter < int(itterations):
            coordinates = Greed(grid, LittleHouse(total_houses, 8, 8, 285000, 2, 0.03),
                          MediumHouse(total_houses, 10, 7.5, 399000, 3, 0.04),
                          LargeHouse(total_houses, 11, 10.5, 610000, 6, 0.06), 1).coordinates
            score_list.append(score_function.calc_score_greedy(coordinates))
            counter += 1

        print("Do you want to make a graph? y/n")
        graph = input("> ").strip()
        graph = graph.lower()
        yes_no = ["n", "y"]
        while graph not in yes_no:
            graph = input("> ")
        file = Graph().make_csv(score_list, algorithm)
        Graph().bokeh(Graph().load_csv(file), algorithm)

    elif algorithm == "hillclimber":
        score_list = []
        counter = 0

        print("How many itterations?")
        itterations = input("> ")
        while name.isdigit() == False or int(name) <= 0:
            print("wrong input")
            itterations = input("> ")

        while counter < int(itterations):
            coordinates = hillclimber(500, 3, 10, score_function, list_houses)
            score_list.append(score_function.calc_score_greedy(coordinates))
            counter += 1

        print("Do you want to make a graph? y/n")
        graph = input("> ").strip()
        graph = graph.lower()
        yes_no = ["n", "y"]
        while graph not in yes_no:
            graph = input("> ")
            graph = graph.lower()

        if graph == "n":
            pass
        else:
            file = Graph().make_csv(score_list, algorithm)
            Graph().bokeh(Graph().load_csv(file), algorithm)

    model = Visualator(grid, LittleHouse(total_houses, 8, 8, 285000, 2, 0.03),
                             MediumHouse(total_houses, 10, 7.5, 399000, 3, 0.04),
                             LargeHouse(total_houses, 11, 10.5, 610000, 6, 0.06),
                             Water(60, 100), coordinates)

    show(model.bokeh())

if __name__ == "__main__":
    algoritme = ["random", "depthfirst", "greedy", "hillclimber"]
    print("Which algoritme do you want to use for you building plan")
    print("1 = random")
    print("2 = Depth First")
    print("3 = greedy")
    print("4 = hillclimber")
    name = input("> ")

    while name.isdigit() == False or int(name) > len(algoritme) or int(name) <= 0:
        print("wrong input")
        name = input("> ")
    Main(algoritme[int(name) - 1])
    # Main("greedy")
