import math
from random import sample
from copy import deepcopy

class Greed(object):
    """
    Takes the grid, calculates the distance between houses and creates houses
    with their coordinates.
    """

    def __init__(self, grid, little, middle, large):
        self.grid = grid
        self.houses = {"little": little, "medium": middle, "large": large}
        self.points = {}
        self.number_point = 0
        self.count_little = 0
        self.count_middle = 0
        self.count_large = 0
        self.coordinates = self.create_coordinates()

    # calculates the degrees between houses for the amount of detachment
    def calculate_degree(self):
        pi = math.pi
        degrees_horizontal = []
        degrees_vertical = []

        for count in range(1, 101):
            degree = 0.5 * pi * (count  / 100)
            if math.cos(degree) > 0.25 * pi:
                degrees_horizontal.append(math.cos(degree))
            else:
                degrees_vertical.append(math.sin(degree))

        return degrees_vertical, degrees_horizontal

    # creates a list with all the houses
    def create_list_house(self):
        list_houses = []
        for key in self.houses.keys():
            list_houses += [key] * int(self.houses[key].number)

        return list_houses

    # creates coordinates for the houses
    def create_coordinates(self):
        random_list = self.create_list_house()
        score = []
        coordinates = []
        valid_set = {}
        original_length = len(random_list)

        # (Vraagje: het number_point is toch nooit negatief, dus dan komt hij toch nooit in de if statement?)
        while self.number_point < original_length:
            house = sample(set(random_list), 1)[0]

            # goes through the grid and looks if the detachment is large enough for the y axis
            for y_axe in range(len(self.grid.grid)):
                if y_axe < self.houses[house].detachement or \
                y_axe > len(self.grid.grid) - self.houses[house].detachement:
                    pass
                else:

                    # looks if the detachment is large enough for the x axis
                    for x_axe in range(len(self.grid.grid[y_axe])):
                        if x_axe < self.houses[house].detachement or \
                        x_axe > len(self.grid.grid[y_axe]) - self.houses[house].detachement \
                        or self.grid.grid[y_axe][x_axe] in range(1, 5):
                            # volgensmij kan het or statement met y_axe > weg, want die zeg je in het if statement erboven al!
                            pass
                        else:
                            if x_axe + self.houses[house].width < self.grid.width - self.houses[house].detachement and \
                               y_axe + self.houses[house].length < self.grid.length - self.houses[house].detachement:
                               coordinates.append({"x": x_axe, "y": y_axe })

            for coordinate in coordinates:
                if self.number_point < 1 and coordinate != None:
                    distance = self.calc_grid_distance(self.calculate_coordinate(coordinate, self.houses[house]))
                    score.append(self.score(distance, self.houses[house]))
                elif coordinate != None:
                    distance = self.min_distance_other_houses(coordinate, self.houses[house], valid_set)
                    score.append(self.score(distance, self.houses[house]))

            index = score.index(max(score))
            try:
                valid_set[house].append(deepcopy(coordinates[index]))
            except:
                valid_set[house] = [deepcopy(coordinates[index])]
            coordinates = []
            score = []
            self.number_point += 1
            print(self.number_point)
            random_list.pop(random_list.index(house))
        return valid_set

    def calculate_coordinate(self, calculation_point, house):
        return {"x1": calculation_point["x"], "x2": calculation_point["x"] + house.width,
                "y1": calculation_point["y"], "y2": calculation_point["y"] + house.length}

    def calc_grid_distance(self, coordinate):
        right = coordinate["x1"]
        left = self.grid.width - coordinate["x2"]
        south = coordinate["y1"]
        north = self.grid.length - coordinate["y2"]
        return min(right, left, south, north)

    def score(self, distance, house):
        factor = ((distance - house.detachement)* house.price_improvement) + 1
        score = int(house.price * factor)
        return score

    def min_distance_other_houses(self, control_coordinate, house, existing_coordinates):
        minimum_distance = None
        valid_set = self.calculate_coordinate(control_coordinate, house)

        for key in existing_coordinates.keys():
            for i in range(len(existing_coordinates[key])):
                selected = self.calculate_coordinate(existing_coordinates[key][i] , house)

                # Use straight line if walls match in horizontal or vertical orientation
                if valid_set["x1"] <= selected["x1"] <= valid_set["x2"] or valid_set["x1"] <= selected["x2"] <= valid_set["x2"]:
                    dist = min(abs(valid_set["y1"] - selected["y2"]), abs(selected["y1"] - valid_set["y2"]))
                elif valid_set["y1"] <= selected["y1"] <= valid_set["y2"] or valid_set["y1"] <= selected["y2"] <= valid_set["y2"]:
                    dist = min(abs(valid_set["x1"] - selected["x2"]), abs(selected["x1"] - valid_set["x2"]))

                # Calculate Euclidian distance in other cases
                else:
                    dist1 = ((valid_set["x1"] - selected["x1"]) ** 2 + (valid_set["y1"] - selected["y1"]) **2)**0.5
                    dist2 = ((valid_set["x1"] - selected["x1"]) ** 2 + (valid_set["y1"] - selected["y2"]) **2)**0.5
                    dist3 = ((valid_set["x1"] - selected["x1"]) ** 2 + (valid_set["y2"] - selected["y1"]) **2)**0.5
                    dist4 = ((valid_set["x1"] - selected["x1"]) ** 2 + (valid_set["y1"] - selected["y2"]) **2)**0.5

                    dist5 = ((valid_set["x1"] - selected["x2"]) ** 2 + (valid_set["y1"] - selected["y1"]) **2)**0.5
                    dist6 = ((valid_set["x1"] - selected["x2"]) ** 2 + (valid_set["y1"] - selected["y2"]) **2)**0.5
                    dist7 = ((valid_set["x1"] - selected["x2"]) ** 2 + (valid_set["y2"] - selected["y1"]) **2)**0.5
                    dist8 = ((valid_set["x1"] - selected["x2"]) ** 2 + (valid_set["y1"] - selected["y2"]) **2)**0.5

                    dist9 = ((valid_set["x2"] - selected["x1"]) ** 2 + (valid_set["y1"] - selected["y1"]) **2)**0.5
                    dist10 = ((valid_set["x2"] - selected["x1"]) ** 2 + (valid_set["y1"] - selected["y2"]) **2)**0.5
                    dist11 = ((valid_set["x2"] - selected["x1"]) ** 2 + (valid_set["y2"] - selected["y1"]) **2)**0.5
                    dist12 = ((valid_set["x2"] - selected["x1"]) ** 2 + (valid_set["y1"] - selected["y2"]) **2)**0.5

                    dist13 = ((valid_set["x2"] - selected["x2"]) ** 2 + (valid_set["y1"] - selected["y1"]) **2)**0.5
                    dist14 = ((valid_set["x2"] - selected["x2"]) ** 2 + (valid_set["y1"] - selected["y2"]) **2)**0.5
                    dist15 = ((valid_set["x2"] - selected["x2"]) ** 2 + (valid_set["y2"] - selected["y1"]) **2)**0.5
                    dist16 = ((valid_set["x2"] - selected["x2"]) ** 2 + (valid_set["y1"] - selected["y2"]) **2)**0.5
                    dist = min(dist1, dist2, dist3, dist4, dist5, dist6, dist7, dist8, dist9, dist10, dist11, dist12, dist13, dist14, dist15, dist16)

                if minimum_distance == None or dist < minimum_distance :
                    minimum_distance = dist

        # Compare grid space and house space to find lowest
        grid_space = self.calc_grid_distance(valid_set)
        return min(minimum_distance, grid_space)
