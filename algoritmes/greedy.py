import sys
from random import sample
from copy import deepcopy

class Greed(object):
    """
    Takes the grid, calculates the distance between houses and creates houses
    with their coordinates.
    """

    def __init__(self, grid, little, middle, large, steps):
        self.grid = grid
        self.houses = {"little": little, "medium": middle, "large": large}
        self.points = {}
        self.number_point = 0
        self.steps = steps
        self.coordinates = self.create_coordinates()

    # creates a list with all the houses name with the correct number
    def create_list_house(self):
        list_houses = []
        for key in self.houses.keys():
            list_houses += [key] * int(self.houses[key].number)

        return list_houses

    # creates coordinates for the houses
    def create_coordinates(self):
        """
        Creates the coordinates that need to be calculated and will get the
        coordinate that gives the highest score
        """

        random_list = self.create_list_house()
        coordinates = []
        valid_set = {}
        original_length = len(random_list)

        # Makes the coordinate and checks if the coordinates are valid
        while self.number_point < original_length:
            print(self.number_point)
            house = sample(set(random_list), 1)[0]

            # goes through the grid and looks if the detachment is large enough for the y axis
            for y_axe in range(0, self.grid.length, self.steps):
                if y_axe < self.houses[house].detachement or \
                y_axe > self.grid.length - self.houses[house].detachement:
                    pass
                else:

                    # Itterate over the x length and controle the detachment in the corners
                    for x_axe in range(0, self.grid.width, self.steps):
                        if x_axe < self.houses[house].detachement or \
                        x_axe > len(self.grid.grid[y_axe]) - self.houses[house].detachement \
                        or self.grid.grid[y_axe][x_axe] in range(1, 5):
                            pass

                        else:
                            if x_axe + self.houses[house].width < self.grid.width - \
                               self.houses[house].detachement and \
                               y_axe + self.houses[house].length < self.grid.length - \
                               self.houses[house].detachement:
                               coordinates.append({"x": x_axe, "y": y_axe })

            max_score_coordinate = self.max_score(coordinates)

            # Will append to the right key or will create the key.
            try:
                valid_set[house].append(deepcopy(coordinates[index]))
            except:
                valid_set[house] = [deepcopy(coordinates[index])]


            random_list.pop(random_list.index(house))
            self.number_point += 1
        return valid_set


    def max_score(self, coordinates):
        """
        Calculates the max_score in the grid and returns the max_score
        """
        score = []

        for coordinate in coordinates:
            if self.number_point < 1 and coordinate != None:
                distance = self.calc_grid_distance(self.calculate_coordinate
                (coordinate, self.houses[house]))
                score.append(self.score(distance, self.houses[house]))
            elif coordinate != None:
                distance = self.min_distance_other_houses
                (coordinate, self.houses[house], valid_set)

                if distance != False:
                    score.append(self.score(distance, self.houses[house]))
                else:
                    score.append(0)

            if all(0 == point for point in score):
                print("Failed them guys, we will get them next tine")
                sys.exit()

            else:
                index = score.index(max(score))

            return coordinates[index]

    def calculate_coordinate(self, calculation_point, house):
        return {"x1": calculation_point["x"], "x2": calculation_point["x"] + house.width,
                "y1": calculation_point["y"], "y2": calculation_point["y"] + house.length}

    def calc_grid_distance(self, coordinate):
        """
        Calculates the distance between the coordinate and the border of the grid
        """
        right = coordinate["x1"]
        left = self.grid.width - coordinate["x2"]
        south = coordinate["y1"]
        north = self.grid.length - coordinate["y2"]
        return min(right, left, south, north)

    def score(self, distance, house):
        """
        Calculates the score.
        """

        factor = ((distance - house.detachement)* house.price_improvement) + 1
        score = int(house.price * factor)
        return score

    def min_distance_other_houses(self, control_coordinate, house, existing_coordinates):
        minimum_distance = None
        valid_set = self.calculate_coordinate(control_coordinate, house)

        for key in existing_coordinates.keys():
            for i in range(len(existing_coordinates[key])):
                selected = self.calculate_coordinate(existing_coordinates[key][i],
                           self.houses[key])
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
        """
        Checks if the coordinates are partially in a house or between a house.
        """

        # Checks if the existing house is in the selected coordinates
        if (selected["x1"] <= valid_set["x1"] <= selected["x2"] or \
        selected["x1"] <= valid_set["x2"] <= selected["x2"]) and \
        (selected["y1"] <= valid_set["y1"] <= selected["y2"] or \
        selected["y1"] <= valid_set["y2"] <= selected["y2"]):
            return False

        # Checks if the house is in a existing house
        elif (valid_set["x1"] <= selected["x1"] <= valid_set["x2"] or \
        valid_set["x1"] <= selected["x2"] <= valid_set["x2"]) and \
        (valid_set["y1"] <= selected["y1"] <= valid_set["y2"] or \
        valid_set["y1"] <= selected["y2"] <= valid_set["y2"]):
            return False

        else:
            return True


    def controle_function (self, check, existing):
        """
        Checks if the coordinate is valid on the restrictions given
        """

        valid_set = check
        selected = existing

        # Checks if the house is partially in a house or between a house.
        if self.house_in_house(valid_set, selected) == False:
            return False

        # Checks if the house is in a vertical or horizontal position of the checkcoordianate
        if valid_set["x1"] < selected["x1"] < valid_set["x2"] or \
        valid_set["x1"] < selected["x2"] < valid_set["x2"]:
            dist = min(abs(valid_set["y1"] - selected["y2"]), abs(selected["y1"] - valid_set["y2"]))

        elif valid_set["y1"] < selected["y1"] < valid_set["y2"] or \
        valid_set["y1"] < selected["y2"] < valid_set["y2"]:
            dist = min(abs(valid_set["x1"] - selected["x2"]), abs(selected["x1"] - valid_set["x2"]))

        # Calculates the if the house are diagonal from eachother.
        else:

            # Checks if the house are left or right from eachother and calculate minimum_distance.
            if (valid_set["x1"] - selected["x2"]) > 0:
                dist1 = ((valid_set["x1"] - selected["x2"]) ** 2 + (valid_set["y1"] \
                        - selected["y1"]) **2)**0.5
                dist2 = ((valid_set["x1"] - selected["x2"]) ** 2 + (valid_set["y1"] \
                         - selected["y2"]) **2)**0.5
                dist3 = ((valid_set["x1"] - selected["x2"]) ** 2 + (valid_set["y2"] \
                         - selected["y1"]) **2)**0.5
                dist4 = ((valid_set["x1"] - selected["x2"]) ** 2 + (valid_set["y2"] \
                        - selected["y2"]) **2)**0.5

            elif (valid_set["x2"] - selected["x1"]) < 0:
                dist1 = ((valid_set["x2"] - selected["x1"]) ** 2 + (valid_set["y1"] \
                         - selected["y1"]) **2)**0.5
                dist2 = ((valid_set["x2"] - selected["x1"]) ** 2 + (valid_set["y1"] \
                        - selected["y2"]) **2)**0.5
                dist3 = ((valid_set["x2"] - selected["x1"]) ** 2 + (valid_set["y2"] \
                        - selected["y1"]) **2)**0.5
                dist4 = ((valid_set["x2"] - selected["x1"]) ** 2 + (valid_set["y2"] \
                        - selected["y2"]) **2)**0.5
            else:
                return False

            dist = min(dist1, dist2, dist3, dist4)

        return dist

class Score(object):
    def __init__(self, coordinates):
        print(coordinates)
        self.coordinates = coordinates
