import pathlib as pathlib
import sys
from bokeh.plotting import show
import random
import copy

# # get the path to the classes
path = pathlib.Path.cwd()
path = pathlib.Path(path).iterdir()
for submap in path:
    sys.path.append(str(submap))

from score_function_new import *

DIMENSIONS = [160,180]
SMALL = [8, 8, 2]
MEDIUM = [10, 7.5, 3]
LARGE = [11, 10.5, 6]
NUM_HOUSES = 20

score, distances, coordinates = best_of_random(10)
# print(score)
# print(distances)
# print(coordinates)
counter = 0
new_coordinates = copy.deepcopy(coordinates)

while counter < 10000:
    for i in range(len(coordinates)):
        mover_x = random.randint(-5, 5)
        mover_y = random.randint(-5, 5)
        # print(mover_x, mover_y)
        new_coordinates[i]["x1"] = new_coordinates[i]["x1"] + mover_x
        new_coordinates[i]["x2"] = new_coordinates[i]["x2"] + mover_x
        new_coordinates[i]["y1"] = new_coordinates[i]["y1"] + mover_y
        new_coordinates[i]["y2"] = new_coordinates[i]["y2"] + mover_y
        max_score, max_distances, max_coordinates = 0, 0, 0
        new_distances = []
        for j in range(len(coordinates)):
            new_distance = calc_distance(new_coordinates[j], new_coordinates, j)
            new_distances.append(new_distance)
            new_score = calc_score(new_distances)
        if new_score > score:
            max_score = new_score
            max_distances = new_distances
            max_coordinates = new_coordinates
        else:
            new_coordinates[i]["x1"] = new_coordinates[i]["x1"] - mover_x
            new_coordinates[i]["x2"] = new_coordinates[i]["x2"] - mover_x
            new_coordinates[i]["y1"] = new_coordinates[i]["y1"] - mover_y
            new_coordinates[i]["y2"] = new_coordinates[i]["y2"] - mover_y
        counter += 1

print(score, max_score)
print(distances, max_distances, sep='\n')
print(coordinates, max_coordinates, sep='\n')
