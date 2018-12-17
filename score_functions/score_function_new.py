import random
import sys
import csv
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

        counter = 0
        mistakes = 0

        # Makes valid coordinates of the houses.
        while counter < num_houses:
            valid_set = {}
            x_coordinate = random.randint(0, self.grid.width)
            y_coordinate = random.randint(0, self.grid.length)
            while self.grid.grid[y_coordinate - 1][x_coordinate - 1] in range(1, 5):
                x_coordinate = random.randint(0, self.grid.width)
                y_coordinate = random.randint(0, self.grid.length)

            # Checks if the coordinates meet the conditions.
            grid_space = self.calc_min_grid_space(x_coordinate, y_coordinate, house_type)
            if grid_space >= house_type.detachement:
                valid_set = self.calc_all_coordinates(y_coordinate, x_coordinate, house_type)
                if len(valid_coordinates) > 0:
                    if self.house_in_house(valid_set, valid_coordinates):
                        valid_coordinates.append(valid_set)
                        counter += 1
                    else:
                        mistakes += 1
                elif len(valid_coordinates) == 0:
                    valid_coordinates.append(valid_set)
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

    def calc_min_grid_space2 (self, valid_set):
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

    def house_in_house (self, valid_set, valid_coordinates):
        """
        Checks if two houses are placed in eachother.
        """

        for selected in valid_coordinates:

            # Checks if the existing house is in the selected coordinates
            if (selected["x1"] <= valid_set["x1"] <= selected["x2"] or selected["x1"] <= valid_set["x2"] <= selected["x2"]) and \
            (selected["y1"] <= valid_set["y1"] <= selected["y2"] or selected["y1"] <= valid_set["y2"] <= selected["y2"]):
                return False

            # Checks if the house is in a existing house
            elif (valid_set["x1"] <= selected["x1"] <= valid_set["x2"] or valid_set["x1"] <= selected["x2"] <= valid_set["x2"]) and \
            (valid_set["y1"] <= selected["y1"] <= valid_set["y2"] or valid_set["y1"] <= selected["y2"] <= valid_set["y2"]):
                return False

        return True

    def calc_distance(self, valid_set, valid_coordinates, index):
        """
        Calculates the distances between houses.
        """

        # Calculates the distances by iterating over the valid coordinates.
        for i in range(len(valid_coordinates)):

            # Skip the comparison between the same data.
            if i == index:
                continue

            selected = valid_coordinates[i]

            # Use straight line if walls match in horizontal or vertical orientation.
            if valid_set["x1"] <= selected["x1"] <= valid_set["x2"] or valid_set["x1"] <= selected["x2"] <= valid_set["x2"] or selected["x1"] <= valid_set["x1"] <= selected["x2"] or selected["x1"] <= valid_set["x2"] <= selected["x2"]  :
                dist = min(abs(valid_set["y1"] - selected["y2"]), abs(selected["y1"] - valid_set["y2"]))
            elif valid_set["y1"] <= selected["y1"] <= valid_set["y2"] or valid_set["y1"] <= selected["y2"] <= valid_set["y2"] or selected["y1"] <= valid_set["y1"] <= selected["y2"] or selected["y1"] <= valid_set["y2"] <= selected["y2"]:
                dist = min(abs(valid_set["x1"] - selected["x2"]), abs(selected["x1"] - valid_set["x2"]))

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
                    dist = ((valid_set[x_valid] - selected[x_selected]) ** 2 + (valid_set[coord[0]] - selected[coord[1]]) **2)**0.5
                    list_dist.append(dist)

                dist = min(list_dist)
        # Compare grid space and house space to find the lowest.
        grid_space = self.calc_min_grid_space2(valid_set)

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

    def best_of_random(self, reps, grid, nr_of_houses):
        """
        Defines the best of all random coordinates.
        """

        max_score, max_distances, max_coordinates = 0, 0, 0
        counter = 0
        check = False

        # Makes a specific amount of valid coordinates of the houses.
        while counter < reps:
            valid_coordinates = []
            for key in self.houses.keys():
                self.create_valid_coordinates (self.houses[key], valid_coordinates, nr_of_houses)

            distances = []
            for count in range(len(valid_coordinates)):
                valid_set = valid_coordinates[count]
                temp = self.calc_distance(valid_set, valid_coordinates, count)
                distances.append(temp)

            check = self.calc_score(distances)
            if check != False:
                counter += 1
                if check > max_score:
                    max_score = check
                    max_distances = distances
                    max_coordinates = valid_coordinates

        print(max_score)

        return max_score, max_distances, max_coordinates

    def random_to_vis(self, intermediate):
        """
        Orders the coordinates of the different houses.
        """

        little, medium, large = [], [], []
        coordinates = intermediate[2]

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

    def vis_to_random(self, coordinates):
        """
        Gives the corners of all the coordinates of the houses.
        """

        coordinates_simple = []

        for i in range(len(coordinates["large"])):
            selected = coordinates["large"][i]
            x1 = selected["x"]
            x2 = selected["x"] + 11
            y1 = selected["y"]
            y2 = selected["y"] + 10.5
            temp = {"x1":x1, "y1":y1, "x2":x2, "y2":y2}
            coordinates_simple.append(temp)
        for i in range(len(coordinates["medium"])):
            selected = coordinates["medium"][i]
            x1 = selected["x"]
            x2 = selected["x"] + 10
            y1 = selected["y"]
            y2 = selected["y"] + 7.5
            temp = {"x1":x1, "y1":y1, "x2":x2, "y2":y2}
            coordinates_simple.append(temp)
        for i in range(len(coordinates["little"])):
            selected = coordinates["little"][i]
            x1 = selected["x"]
            x2 = selected["x"] + 8
            y1 = selected["y"]
            y2 = selected["y"] + 8
            temp = {"x1":x1, "y1":y1, "x2":x2, "y2":y2}
            coordinates_simple.append(temp)

        return coordinates_simple

    def calc_score_greedy(self, coordinates):
        """
        Gives the score of the coordinates determined by the Greedy algorithm.
        """

        # Moet allemaal in greedy komen, met de benodigde imports (Coen was hier echter mee bezig) !!!!!!!!!!!!!!!!!
        coordinates_simple = vis_to_random(coordinates)
        distances = []

        # Calculates the shortest distance between all houses and the closest neighbor.
        for i in range(len(coordinates_simple)):
            valid_set = coordinates_simple[i]
            temp = calc_distance(valid_set, coordinates_simple, i )
            distances.append(temp)
        check = calc_score(distances)
        return check
