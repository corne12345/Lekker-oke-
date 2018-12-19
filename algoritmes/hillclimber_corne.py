import pathlib as pathlib
import sys
from bokeh.plotting import show
import random
import copy
import csv
import matplotlib.pyplot as plt

# Get the path to the classes.
path = pathlib.Path.cwd()
path = pathlib.Path(path).iterdir()
for submap in path:
    sys.path.append(str(submap))

from score_function_new import *

# Set the constants.
DIMENSIONS = [160,180]
SMALL = [8, 8, 2]
MEDIUM = [10, 7.5, 3]
LARGE = [11, 10.5, 6]
NUM_HOUSES = 20

def calc_grid_distance(coordinate, grid):
    """
    Calculates the distance between the coordinate and the border of the grid
    """
    right = coordinate["x1"]
    left = grid.width - coordinate["x2"]
    south = coordinate["y1"]
    north = grid.length - coordinate["y2"]
    return min(right, left, south, north)

def vis_to_random(coordinates, houses):
    """
    Gives the corners of all the coordinates of the houses.
    """

    coordinates_simple = []

    for key in coordinates.keys():
        for selected in coordinates[key]:
            x1 = selected["x"]
            x2 = selected["x"] + houses[key].width
            y1 = selected["y"]
            y2 = selected["y"] + houses[key].length
            temp = {"x1":x1, "y1":y1, "x2":x2, "y2":y2}
            coordinates_simple.append(temp)

    return coordinates_simple

def random_to_vis(coordinates):
    """
    Orders the coordinates of the different houses.
    """

    little, medium, large = [], [], []

    for i in range(len(coordinates)):
        coordinates_1 = coordinates[i]
        coordinate = {"x": coordinates_1["x1"], "y": coordinates_1["y1"]}
        if i < len(coordinates) * 0.15:
            large.append(coordinate)
        elif i < len(coordinates) * 0.4:
            medium.append(coordinate)
        else:
            little.append(coordinate)

    coordinates_ordered = {"little": little, "medium": medium, "large": large}

    return coordinates_ordered

def hillclimber(reps, steps, randoms, score_function, houses, grid, printplot = False):
    """
    Tries to calculate the best score by changing coordinates of the houses.
    """

    # Defines the start coordinates of the houses and other constants.
    score, distances, coordinates = score_function.best_of_random(randoms)
    while coordinates == 0:
        score, distances, coordinates = score_function.best_of_random(randoms)
    counter = 0

    new_coordinates = copy.deepcopy(coordinates)
    max_score, max_distances, max_coordinates = 0, 0, 0

    # Write to csv.
    f = open("result.csv", "w", newline='')
    writer = csv.writer(f)
    counters = []
    max_scores = []

    # Changes a coordinate of one house.
    while counter < reps:
        print(reps)
        print(counter)
        for select in new_coordinates.keys():
            for i in range(len(new_coordinates[select])):
                control = True
                mover_x = random.randint(-steps, steps)
                mover_y = random.randint(-steps, steps)
                for dim in [("x", mover_x), ("y", mover_y)]:
                    new_coordinates[select][i][dim[0]] = new_coordinates[select][i][dim[0]] - dim[1]

                new_distances = {}

                # Checks if the score of the new coordinates is higher than the last score.
                for key in new_coordinates.keys():
                    new_distances[key] = []
                    for coordinate in new_coordinates[key]:
                        valid_set = {"y1": coordinate["y"], "x1": coordinate["x"],
                                     "y2": coordinate["y"] + houses[key].length, "x2": coordinate["x"]+ houses[key].width}

                        new_distance = score_function.calc_distance(key, valid_set, new_coordinates)

                        try:
                            if grid.grid[coordinate["y"] - 1][coordinate["x"] - 1] in range(1, 5):
                                control = False
                        except:
                            control = False

                        new_distances[key].append(new_distance)


                new_score = score_function.calc_score(new_distances)

                # Changes all the data to the new coordinates.
                if new_score > max_score and control == True:
                    print(max_score)

                    max_score = round(new_score)
                    max_scores.append(max_score)
                    counters.append(counter)
                    max_distances = new_distances
                    max_coordinates = new_coordinates
                    writer.writerow([counter, max_score])


                # Changes the coordinates otherwise back.
                else:
                    for dim in [("x", mover_x), ("y", mover_y)]:
                        new_coordinates[select][i][dim[0]] = new_coordinates[select][i][dim[0]] + dim[1]
                counter += 1



    # Shows a plot of the score against the amount of runs.
    if printplot == True:
        plt.plot(counters, max_scores)
        plt.xlabel("counter")
        plt.ylabel("score")
        plt.title("plot of hillclimber with %i reps" %reps)
        plt.text(1, 5000000, "final score: %i" %max_score)
        plt.text(1, 7000000, "initial score: %i" %score)
        plt.savefig('hillclimber.png')
        plt.show()
    print(max_score)
    intermediate  = max_score, max_distances, max_coordinates
    print(max_coordinates)
    return max_coordinates
