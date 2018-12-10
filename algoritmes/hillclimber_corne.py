import pathlib as pathlib
import sys
from bokeh.plotting import show
import random
import copy
import csv
import matplotlib.pyplot as plt

# # get the path to the classes
path = pathlib.Path.cwd()
path = pathlib.Path(path).iterdir()
for submap in path:
    sys.path.append(str(submap))

from score_function_new import *

# set constants to work with
DIMENSIONS = [160,180]
SMALL = [8, 8, 2]
MEDIUM = [10, 7.5, 3]
LARGE = [11, 10.5, 6]
NUM_HOUSES = 20


def hillclimber(reps, steps, randoms, printplot = False):
    score, distances, coordinates = best_of_random(randoms)
    counter = 0
    new_coordinates = copy.deepcopy(coordinates)
    max_score, max_distances, max_coordinates = 0, 0, 0

    # Write to csv
    f = open("result.csv", "w", newline='')
    writer = csv.writer(f)
    counters = [0]
    max_scores = [0]

    while counter < reps:
        for i in range(len(coordinates)):
            mover_x = random.randint(-steps, steps)
            mover_y = random.randint(-steps, steps)
            new_coordinates[i]["x1"] = new_coordinates[i]["x1"] + mover_x
            new_coordinates[i]["x2"] = new_coordinates[i]["x2"] + mover_x
            new_coordinates[i]["y1"] = new_coordinates[i]["y1"] + mover_y
            new_coordinates[i]["y2"] = new_coordinates[i]["y2"] + mover_y
            new_distances = []
            # print("hoi")
            for j in range(len(coordinates)):
                new_distance = calc_distance(new_coordinates[j], new_coordinates, j)
                new_distances.append(new_distance)
            new_score = calc_score(new_distances)
            if new_score > max_score:
                max_score = round(new_score)
                max_scores.append(max_score)
                counters.append(counter)
                max_distances = new_distances
                max_coordinates = new_coordinates
                writer.writerow([counter, max_score])
            else:
                new_coordinates[i]["x1"] = new_coordinates[i]["x1"] - mover_x
                new_coordinates[i]["x2"] = new_coordinates[i]["x2"] - mover_x
                new_coordinates[i]["y1"] = new_coordinates[i]["y1"] - mover_y
                new_coordinates[i]["y2"] = new_coordinates[i]["y2"] - mover_y
            counter += 1

    if printplot == True:
        plt.plot(counters, max_scores)
        plt.xlabel("counter")
        plt.ylabel("score")
        plt.title("plot of hillclimber with %i reps" %reps)
        plt.text(1, 5000000, "final score: %i" %max_score)
        plt.savefig('hillclimber.png')
        plt.show()


    # print(score, max_score)
    # print(distances, max_distances, sep='\n')
    # print(coordinates, max_coordinates, sep='\n')
    intermediate  = max_score, max_distances, max_coordinates
    return random_to_vis(intermediate)
    # return  max_score, max_distances, max_coordinates


if __name__ == "__main__":
    # a = input("how many reps would you like")
    # b = input("in what range can the changes be?")
    # c = input("how many randoms to do first?")
    # hillclimber(a, b, c)
    hillclimber(1000, 5, 1, True)
