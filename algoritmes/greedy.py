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

                    if distance != False:
                        score.append(self.score(distance, self.houses[house]))
                    else:
                        score.append(0)

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
                selected = self.calculate_coordinate(existing_coordinates[key][i] , self.houses[key])
                dist = self.controle_function(valid_set, selected)

                if dist == False:
                    return False

                # checks if the distance bigger then the detachement
                if dist < max(house.detachement, self.houses[key].detachement):
                    return False
                elif minimum_distance == None or dist < minimum_distance:
                    minimum_distance = dist

        # Compare grid space and house space to find lowest
        grid_space = self.calc_grid_distance(valid_set)
        return min(minimum_distance, grid_space)



    def house_in_house (self, valid_set, selected):
        test = selected
        x1 = test["x1"] <= valid_set["x1"] <= test["x2"]
        x2 = test["x1"] <= valid_set["x2"] <= test["x2"]
        y1 = test["y1"] <= valid_set["y1"] <= test["y2"]
        y2 = test["y1"] <= valid_set["y2"] <= test["y2"]
        if (x1 == True or x2 == True) and (y1 == True or y2 == True):
            return True
        return False

    def controle_function (self, check, existing):
        valid_set = check
        selected = existing

        # Checks if the house is in a a house
        if self.house_in_house(valid_set, selected) == True:
            return False


        # dit stuk code verplaatsen naar de house in house stuk
        elif (selected["x1"] < valid_set["x1"] < selected["x2"] or selected["x1"] < valid_set["x2"] <= selected["x2"]) and \
        (selected["y1"] < valid_set["y1"] < selected["y2"] or selected["y1"] < valid_set["y2"] < selected["y2"]):
            return False

        elif (valid_set["x1"] <= selected["x1"] <= valid_set["x2"] or valid_set["x1"] <= selected["x2"] <= valid_set["x2"]) and \
        (valid_set["y1"] < selected["y1"] < valid_set["y2"] or valid_set["y1"] <= selected["y2"] <= valid_set["y2"]):
            return False

        # Checks if the house is in a vertical or horizontal position of the checkcoordianate
        if valid_set["x1"] < selected["x1"] < valid_set["x2"] or valid_set["x1"] < selected["x2"] < valid_set["x2"]:
            dist = min(abs(valid_set["y1"] - selected["y2"]), abs(selected["y1"] - valid_set["y2"]))

        elif valid_set["y1"] < selected["y1"] < valid_set["y2"] or valid_set["y1"] <= selected["y2"] <= valid_set["y2"]:
            dist = min(abs(valid_set["x1"] - selected["x2"]), abs(selected["x1"] - valid_set["x2"]))

        # Calculates the if the house are diagonal in eachother
        else:

            # Checks if the house are left or right from eachother
            if (valid_set["x1"] - selected["x2"]) > 0:
                dist1 = ((valid_set["x1"] - selected["x2"]) ** 2 + (valid_set["y1"] - selected["y1"]) **2)**0.5
                dist2 = ((valid_set["x1"] - selected["x2"]) ** 2 + (valid_set["y1"] - selected["y2"]) **2)**0.5
                dist3 = ((valid_set["x1"] - selected["x2"]) ** 2 + (valid_set["y2"] - selected["y1"]) **2)**0.5
                dist4 = ((valid_set["x1"] - selected["x2"]) ** 2 + (valid_set["y2"] - selected["y2"]) **2)**0.5

            elif (valid_set["x2"] - selected["x1"]) < 0:
                dist1 = ((valid_set["x2"] - selected["x1"]) ** 2 + (valid_set["y1"] - selected["y1"]) **2)**0.5
                dist2 = ((valid_set["x2"] - selected["x1"]) ** 2 + (valid_set["y1"] - selected["y2"]) **2)**0.5
                dist3 = ((valid_set["x2"] - selected["x1"]) ** 2 + (valid_set["y2"] - selected["y1"]) **2)**0.5
                dist4 = ((valid_set["x2"] - selected["x1"]) ** 2 + (valid_set["y2"] - selected["y2"]) **2)**0.5
            else:
                return False

            dist = min(dist1, dist2, dist3, dist4)

        return dist
