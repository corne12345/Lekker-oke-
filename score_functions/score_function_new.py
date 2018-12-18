import random
import sys
import csv
from copy import deepcopy
from matplotlib import pyplot as plt

class newScore(object):
    def __init__(self, grid, small, medium, large):
        self.grid = grid
        self.dimensions = [grid.width, grid.length]
        self.houses = {"little": small, "medium": medium, "large": large}

    def create_valid_coordinates (self, house_type, valid_coordinates, num_houses):
        """
        Creates coordinates for the houses which meet the conditions.
        """
        coordinates = []
        counter = 0

        # Makes valid coordinates of the houses.
        while counter < num_houses:
            control = False
            dist = None

            x_coordinate = random.randint(0, self.grid.width)
            y_coordinate = random.randint(0, self.grid.length)
            while self.grid.grid[y_coordinate - 1][x_coordinate - 1] in range(1, 5):
                x_coordinate = random.randint(0, self.grid.width)
                y_coordinate = random.randint(0, self.grid.length)

            if valid_coordinates == {}:
                valid_set = self.calc_all_coordinates(y_coordinate, x_coordinate, self.houses[house_type])
                valid_coordinates[house_type] = [deepcopy({"y": y_coordinate, "x": x_coordinate})]
                counter += 1
                continue


            # Checks if the coordinates meet the conditions.
            valid_set = self.calc_all_coordinates(y_coordinate, x_coordinate, self.houses[house_type])
            dist = self.calc_distance(valid_set, valid_coordinates)
            grid_space = self.calc_min_grid_space2(valid_set)
            dist = min(dist, grid_space)

            while dist > self.houses[house_type].detachement or \
            x_coordinate + self.houses[house_type].detachement > self.grid.width or \
            y_coordinate + self.houses[house_type].detachement > self.grid.length:
                x_coordinate = random.randint(0, self.grid.width)
                y_coordinate = random.randint(0, self.grid.length)
                valid_set = self.calc_all_coordinates(y_coordinate, x_coordinate, self.houses[house_type])
                dist = self.calc_distance(valid_set, valid_coordinates)
            # Will append to the right key or will create the key.
            try:
                valid_coordinates[house_type].append(deepcopy({"y": y_coordinate, "x": x_coordinate}))
            except:
                valid_coordinates[house_type] = [deepcopy({"y": y_coordinate, "x": x_coordinate})]
            control = True
            counter += 1





    def calc_min_grid_space (self, x_coordinate, y_coordinate, house):
        """
        This function returns the shortest distance to the grid of a certain house
        with given coordinates.
        """

        temp1 = x_coordinate - 0
        temp2 = self.grid.width - house.width - x_coordinate
        temp3 = y_coordinate - 0
        temp4 = self.grid.length - house.length - y_coordinate

        return min(temp1, temp2, temp3, temp4)

    def calc_min_grid_space2(self, valid_set):
        """
        This function returns the shortest distance to the grid of a certain house
        with given coordinates.
        """
        print(valid_set)
        temp1 = valid_set["x1"]
        temp2 = self.grid.width - valid_set["x2"]
        temp3 = valid_set["y1"]
        temp4 = self.grid.length - valid_set["y2"]
        return min(temp1, temp2, temp3, temp4)

    def calc_all_coordinates(self, y_coordinate, x_coordinate, house):
        """
        Gives the coordinates of a house.
        """

        return {"y1": y_coordinate, "x1": x_coordinate, "y2": y_coordinate + house.length, "x2": x_coordinate + house.width}

    def house_in_house (self, valid_set, selected):
        """
        Checks if two houses are placed in eachother.
        """

        # Checks if the existing house is in the selected coordinates
        if (selected["x1"] <= valid_set["x1"] <= selected["x2"] or selected["x1"] <= valid_set["x2"] <= selected["x2"]) and \
        (selected["y1"] <= valid_set["y1"] <= selected["y2"] or selected["y1"] <= valid_set["y2"] <= selected["y2"]):
            return False

        # Checks if the house is in a existing house
        elif (valid_set["x1"] <= selected["x1"] <= valid_set["x2"] or valid_set["x1"] <= selected["x2"] <= valid_set["x2"]) and \
        (valid_set["y1"] <= selected["y1"] <= valid_set["y2"] or valid_set["y1"] <= selected["y2"] <= valid_set["y2"]):
            return False

        return True

    def calc_distance(self, valid_set, valid_coordinates):
        """
        Calculates the distances between houses.
        """
        dist = None
        print(valid_set)
        # Calculates the distances by iterating over the valid coordinates.
        for key in valid_coordinates.keys():
            for coordinate in valid_coordinates[key]:

                selected = self.calc_all_coordinates(coordinate["y"], coordinate["x"], self.houses[key])
                if selected == valid_set:
                    continue

                if self.house_in_house(valid_set, selected) == False:

                    return False

                # Checks if the house is in a vertical or horizontal position of the checkcoordianate
                if valid_set["x1"] < selected["x1"] < valid_set["x2"] or valid_set["x1"] < selected["x2"] < valid_set["x2"]:
                    dist = min(abs(valid_set["y1"] - selected["y2"]), abs(selected["y1"] - valid_set["y2"]),
                               abs(valid_set["y1"] - selected["y1"]), abs(selected["y2"] - valid_set["y2"]))

                elif valid_set["y1"] < selected["y1"] < valid_set["y2"] or valid_set["y1"] < selected["y2"] < valid_set["y2"]:
                    dist = min(abs(valid_set["x1"] - selected["x2"]), abs(selected["x1"] - valid_set["x2"]),
                               abs(valid_set["x2"] - selected["x2"]), abs(selected["x1"] - valid_set["x1"]))

                # Calculate Euclidian distance in other cases.
                else:
                    list_dist = []
                    # Checks if the houses are left or right from eachother and
                    # calculates the minimum distance.
                    if (valid_set["x1"] - selected["x2"]) > 0:
                        x_valid = "x1"
                        x_selected = "x2"

                    elif (valid_set["x2"] - selected["x1"]) < 0:
                        x_valid = "x2"
                        x_selected = "x1"

                    else:
                        return False

                    for coord in ([["y1", "y1"], ["y1", "y2"], ["y2", "y1"], ["y2", "y2"]]):
                        dist = (abs(valid_set[x_valid] - selected[x_selected]) ** 2 + abs(valid_set[coord[0]] - selected[coord[1]]) **2)**0.5
                        list_dist.append(dist)

                    dist = min(list_dist)
        print("joe")
        print(dist)
        # Compare grid space and house space to find the lowest.
        grid_space = self.calc_min_grid_space2(valid_set)
        print(grid_space)
        return min(dist, grid_space)

    def calc_score(self, distances):
        """
        This function takes the distances of all the houses to its closest
        neighbour as input and returns the worth of the neigborhood.
        """

        score = 0

        for i in range(int(len(distances) * 0.15)):
            if distances[i] < 6:
                return False
            factor = ((distances[i] - 6) * 6) / 100 + 1
            price = 610000 * factor
            score += price

        for i in range(int(len(distances) * 0.15) , int(len(distances)* 0.40)):
            if distances[i] < 3:
                return False
            factor = ((distances[i] - 3) * 4) / 100 + 1
            price = 399000 * factor
            score += price

        for i in range(int(len(distances) * 0.40), len(distances)):
            if distances[i] < 2:
                return False
            factor = ((distances[i] - 2) * 3) / 100 + 1
            price = 285000 * factor
            score += price

        return score

    def best_of_random(self, reps):
        """
        Defines the best of all random coordinates.
        """

        max_score, max_distances, max_coordinates = 0, 0, 0
        counter = 0
        dist = 0
        check = False
        distances = []
        while False in distances or distances == []:
            print(distances)
            # Makes a specific amount of valid coordinates of the houses
            valid_coordinates = {}
            for key in self.houses.keys():
                self.create_valid_coordinates(key, valid_coordinates, self.houses[key].number)

            distances = []
            print(valid_coordinates)
            for key in valid_coordinates.keys():
                for count in range(len(valid_coordinates[key])):
                    dist = 0
                    while dist < self.houses[key].detachement or \
                    self.grid.grid[valid_coordinates[key][count]["y"] - 1][ valid_coordinates[key][count]["x"] - 1] in range(1, 5):
                        valid_coordinates[key][count]["y"] = x_coordinate = random.randint(0, self.grid.width)
                        valid_coordinates[key][count]["x"] = x_coordinate = random.randint(0, self.grid.width)
                        valid_set = self.calc_all_coordinates(valid_coordinates[key][count]["y"], valid_coordinates[key][count]["x"], self.houses[key])
                        dist = self.calc_distance(valid_set, valid_coordinates)
                        print(valid_coordinates)
                    distances.append(dist)

            check = self.calc_score(distances)
            if check != False:
                if check > max_score:
                    max_score = check
                    max_distances = distances
                    max_coordinates = valid_coordinates

        print(max_score)

        return max_score, max_distances, max_coordinates

    def calc_score_greedy(self, coordinates):
        """
        Gives the score of the coordinates determined by the Greedy algorithm.
        """

        # Moet allemaal in greedy komen, met de benodigde imports (Coen was hier echter mee bezig) !!!!!!!!!!!!!!!!!
        distances = []

        # Calculates the shortest distance between all houses and the closest neighbor.
        for key in coordinates.keys():
            for coordinate in coordinates[key]:
                valid_set = self.calc_all_coordinates(coordinate["y"], coordinate["x"], self.houses[key])
                temp = self.calc_distance(valid_set, coordinates)
                distances.append(temp)
        check = self.calc_score(distances)

        return check
