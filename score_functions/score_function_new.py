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
            valid_set = self.calc_all_coordinates(y_coordinate, x_coordinate, self.houses[house_type])
            grid_space = self.calc_min_grid_space2(valid_set)
            while self.grid.grid[y_coordinate - 1][x_coordinate - 1] in range(1, 5) or \
            grid_space < self.houses[house_type].detachement:
                x_coordinate = random.randint(0, self.grid.width)
                y_coordinate = random.randint(0, self.grid.length)
                valid_set = self.calc_all_coordinates(y_coordinate, x_coordinate, self.houses[house_type])
                grid_space = self.calc_min_grid_space2(valid_set)


            if valid_coordinates == {}:
                valid_coordinates[house_type] = [deepcopy({"y": y_coordinate, "x": x_coordinate})]
                counter += 1
                continue


            # Checks if the coordinates meet the conditions.
            valid_set = self.calc_all_coordinates(y_coordinate, x_coordinate, self.houses[house_type])
            dist = self.calc_distance(valid_set, valid_coordinates)
            grid_space = self.calc_min_grid_space2(valid_set)
            dist = min(dist, grid_space)

            while dist == False or dist <= self.houses[house_type].detachement or \
            self.grid.grid[y_coordinate - 1][x_coordinate - 1] in range(1, 5):
                x_coordinate = random.randint(0, self.grid.width)
                y_coordinate = random.randint(0, self.grid.length)
                valid_set = self.calc_all_coordinates(y_coordinate, x_coordinate, self.houses[house_type])
                dist = self.calc_distance(valid_set, valid_coordinates)
                if dist == False or self.houses[house_type].detachement:
                    continue

                grid_space = self.calc_min_grid_space2(valid_set)
                dist = min(grid_space, dist)

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

        temp1 = x_coordinate
        temp2 = self.grid.width - (house.width + x_coordinate)
        temp3 = y_coordinate
        temp4 = self.grid.length - (house.length + y_coordinate)

        return min(temp1, temp2, temp3, temp4)

    def calc_min_grid_space2(self, valid_set):
        """
        This function returns the shortest distance to the grid of a certain house
        with given coordinates.
        """

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

        # Calculates the distances by iterating over the valid coordinates.
        for key in valid_coordinates.keys():
            for coordinate in valid_coordinates[key]:

                selected = self.calc_all_coordinates(coordinate["y"], coordinate["x"], self.houses[key])
                if selected["x1"] == valid_set["x1"] and selected["y1"] == valid_set["y1"]:
                    continue

                if self.house_in_house(valid_set, selected) == False:
                    return False

                # Checks if the house is in a vertical or horizontal position of the checkcoordianate
                if valid_set["x1"] <= selected["x1"] <= valid_set["x2"] or valid_set["x1"] <= selected["x2"] <= valid_set["x2"]:
                    dist = min(abs(valid_set["y1"] - selected["y2"]), abs(selected["y1"] - valid_set["y2"]),
                               abs(valid_set["y1"] - selected["y1"]), abs(selected["y2"] - valid_set["y2"]))

                elif valid_set["y1"] <= selected["y1"] <= valid_set["y2"] or valid_set["y1"] <= selected["y2"] <= valid_set["y2"]:
                    dist = min(abs(valid_set["x1"] - selected["x2"]), abs(selected["x1"] - valid_set["x2"]),
                               abs(valid_set["x2"] - selected["x2"]), abs(selected["x1"] - valid_set["x1"]))

                # Calculate Euclidian distance in other cases.
                else:
                    list_dist = []
                    # Checks if the houses are left or right from eachother and
                    # calculates the minimum distance.
                    if (selected["x1"]  - valid_set["x2"]) > 0:
                        x_valid = "x1"
                        x_selected = "x2"

                    elif (selected["x2"] - valid_set["x1"]) < 0:
                        x_valid = "x2"
                        x_selected = "x1"

                    else:
                        return False

                    for coord in ([["y1", "y1"], ["y1", "y2"], ["y2", "y1"], ["y2", "y2"]]):
                        dist = (abs(valid_set[x_valid] - selected[x_selected]) ** 2 + abs(valid_set[coord[0]] - selected[coord[1]]) **2)**0.5
                        list_dist.append(dist)

                    dist = min(list_dist)

                if dist < self.houses[key].detachement:
                    return False

        # Compare grid space and house space to find the lowest.
        grid_space = self.calc_min_grid_space2(valid_set)

        return min(dist, grid_space)

    def calc_score(self, distances):
        """
        This function takes the distances of all the houses to its closest
        neighbour as input and returns the worth of the neigborhood.
        """

        score = 0
        for key in distances.keys():
            house = self.houses[key]
            for distance in distances[key]:
                score += (distance - house.detachement) * house.price_improvement + house.price

        return score

    def best_of_random(self, reps):
        """
        Defines the best of all random coordinates.
        """

        max_score, max_distances, max_coordinates = 0, 0, 0
        counter = 0
        dist = 0
        check = False
        distances = {}


            # Makes a specific amount of valid coordinates of the houses
        valid_coordinates = {}
        for key in self.houses.keys():
            self.create_valid_coordinates(key, valid_coordinates, self.houses[key].number)

        for key in valid_coordinates.keys():
            for coordinate in valid_coordinates[key]:
                valid_set = self.calc_all_coordinates(coordinate["y"], coordinate["x"], self.houses[key])
                dist = self.calc_distance(valid_set, valid_coordinates)
                try:
                    distances[key].append(dist)
                except:
                    distances[key] = [dist]
        print(distances)
        check = self.calc_score(distances)

        if check != False:
            if check > max_score:
                max_score = check
                max_distances = distances
                max_coordinates = valid_coordinates

        return max_score, max_distances, max_coordinates

    def calc_score_greedy(self, coordinates):
        """
        Gives the score of the coordinates determined by the Greedy algorithm.
        """

        # Moet allemaal in greedy komen, met de benodigde imports (Coen was hier echter mee bezig) !!!!!!!!!!!!!!!!!
        distances = {}

        # Calculates the shortest distance between all houses and the closest neighbor.
        for key in coordinates.keys():
            distances[key] = []
            for coordinate in coordinates[key]:
                valid_set = self.calc_all_coordinates(coordinate["y"], coordinate["x"], self.houses[key])
                temp = self.calc_distance(valid_set, coordinates)
                distances[key].append(temp)
        check = self.calc_score(distances)
        if check == False:
            print(distances)
            sys.exit()

        return check
