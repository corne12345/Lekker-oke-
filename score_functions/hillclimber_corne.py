import pathlib as pathlib
import sys
from bokeh.plotting import show
import random
import copy
import csv

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

# calculates the coordinates by changing the coordinates from the random function
def hillclimber(reps, steps, randoms):

    # takes the random coordinates
    score, distances, coordinates = best_of_random(randoms)
    counter = 0
    new_coordinates = copy.deepcopy(coordinates)
    max_score, max_distances, max_coordinates = 0, 0, 0

    # write to csv
    f = open("result.csv", "w", newline='')
    writer = csv.writer(f)

    # moves the coordinates until the amount of reps
    while counter < reps:
        for i in range(len(coordinates)):

            # changes the coordinates with a pseudo random amount of steps
            mover_x = random.randint(-steps, steps)
            mover_y = random.randint(-steps, steps)
            new_coordinates[i]["x1"] = new_coordinates[i]["x1"] + mover_x
            new_coordinates[i]["x2"] = new_coordinates[i]["x2"] + mover_x
            new_coordinates[i]["y1"] = new_coordinates[i]["y1"] + mover_y
            new_coordinates[i]["y2"] = new_coordinates[i]["y2"] + mover_y
            new_distances = []

            # calculates the new shortest distance between the house and the other houses
            for j in range(len(coordinates)):
                new_distance = calc_distance(new_coordinates[j], new_coordinates, j)
                new_distances.append(new_distance)
            new_score = calc_score(new_distances)

            # determines if the score is larger than the last score
            if new_score > max_score:
                max_score = round(new_score)
                max_distances = new_distances
                max_coordinates = new_coordinates
                writer.writerow([counter, max_score])

            # else it keeps the old coordinates
            else:
                new_coordinates[i]["x1"] = new_coordinates[i]["x1"] - mover_x
                new_coordinates[i]["x2"] = new_coordinates[i]["x2"] - mover_x
                new_coordinates[i]["y1"] = new_coordinates[i]["y1"] - mover_y
                new_coordinates[i]["y2"] = new_coordinates[i]["y2"] - mover_y
            counter += 1

    print(score, max_score)
    print(distances, max_distances, sep='\n')
    print(coordinates, max_coordinates, sep='\n')
    return max_coordinates, max_distances, max_score

if __name__ == "__main__":
    # a = input("how many reps would you like")
    # b = input("in what range can the changes be?")
    # c = input("how many randoms to do first?")
    # hillclimber(a, b, c)

    hillclimber(5000, 2, 10)
