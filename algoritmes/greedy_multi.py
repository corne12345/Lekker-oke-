import sys
import math
import datetime
from multiprocessing import Process, Pipe
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
        self.scores = []

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
            print(valid_set)
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
                        x_axe > len(self.grid.grid[y_axe]) - self.houses[house].detachement or \
                        self.grid.grid[y_axe][x_axe] in range(1, 5):
                            pass

                        else:
                            if (x_axe + self.houses[house].width < self.grid.width - self.houses[house].detachement) and \
                            (y_axe + self.houses[house].length < self.grid.length - self.houses[house].detachement):
                                coordinates.append({"x": x_axe, "y": y_axe })

            score_coordinate = self.max_score(coordinates, house, valid_set)
            print("score" + str(score_coordinate))
            # Will append to the right key or will create the key.
            try:
                valid_set[house].append(deepcopy(score_coordinate))
            except:
                valid_set[house] = [deepcopy(score_coordinate)]


            random_list.pop(random_list.index(house))
            self.number_point += 1
        return valid_set


    def max_score(self, coordinates, house, valid_set):
        """
        Calculates the max_score in the grid and returns the max_score
        """
        score = []
        self.scores = []
        threads = {}
        processes = {}
        receivers = []
        max_score = None
        max_coordinate = None
        list = []

        if self.number_point < 1:
            for coordinate in coordinates:
                distance = self.calc_grid_distance(self.calculate_coordinate(coordinate, self.houses[house]))
                score.append(self.score(distance, self.houses[house]))

            index = score.index(max(score))
            return coordinates[index]

        else:
            # make 4 different lists
            half = len(coordinates)//2

            half1 = coordinates[:half]
            half2 = coordinates[half:]
            quarter = len(half1)//2
            list.append(half1[:quarter])
            list.append(half1[quarter:])
            list.append(half2[:quarter])
            list.append(half2[quarter:])

            for count in range(len(list)):
                parent_conn, child_conn = Pipe()
                receivers.append({"parent" + str(count): parent_conn, "child" + str(count): child_conn })
                processes["process" + str(count)] = Thread(list[count], self.houses, house, valid_set, self.grid)

            for count, key in enumerate(processes.keys()):
                threads["thread" + str(count)] = Process(target=processes[key].run, args=(receivers[count]["child" + str(count)], ))

            for key in threads.keys():
                threads[key].start()

            for count, t in enumerate(threads.keys()):
                self.scores.append(deepcopy(receivers[count]["parent" + str(count)].recv()))
                threads[t].join()

            print(self.scores)
            for score in self.scores:

                if max_score == None or max_score < score["score"]:
                    max_score = score["score"]
                    max_coordinate = score["coordinate"]
        self.score= []
        return deepcopy(max_coordinate)

    def calc_grid_distance(self, coordinate):
        """
        Calculates the distance between the coordinate and the border of the grid
        """
        right = coordinate["x1"]
        left = self.grid.width - coordinate["x2"]
        south = coordinate["y1"]
        north = self.grid.length - coordinate["y2"]
        return min(right, left, south, north)

    def calculate_coordinate(self, calculation_point, house):
        return {"x1": calculation_point["x"], "x2": calculation_point["x"] + house.width,
                "y1": calculation_point["y"], "y2": calculation_point["y"] + house.length}

    def score(self, distance, house):
        """
        Calculates the score.
        """

        factor = ((distance - house.detachement)* house.price_improvement) + 1
        score = int(house.price * factor)
        return score


class Thread (object):
    """
    Multithreading and fast calculations
    """

    def __init__(self, control_coordinate, houses, key, existing_coordinates, grid):
        self.grid = grid
        self.coordinates = control_coordinate
        self.houses = houses
        self.key = key
        self.existing_coordinates = existing_coordinates
        self.max_score = None

    def calc_grid_distance(self, coordinate):
        """
        Calculates the distance between the coordinate and the border of the grid
        """
        right = coordinate["x1"]
        left = self.grid.width - coordinate["x2"]
        south = coordinate["y1"]
        north = self.grid.length - coordinate["y2"]
        return min(right, left, south, north)

    def house_in_house (self, valid_set, selected):
        """
        Checks if the coordinates are partially in a house or between a house.
        """

        # Checks if the existing house is in the selected coordinates
        if (selected["x1"] <= valid_set["x1"] <= selected["x2"] or selected["x1"] <= valid_set["x2"] <= selected["x2"]) and \
        (selected["y1"] <= valid_set["y1"] <= selected["y2"] or selected["y1"] <= valid_set["y2"] <= selected["y2"]):
            return False

        # Checks if the house is in a existing house
        elif (valid_set["x1"] <= selected["x1"] <= valid_set["x2"] or valid_set["x1"] <= selected["x2"] <= valid_set["x2"]) and \
        (valid_set["y1"] <= selected["y1"] <= valid_set["y2"] or valid_set["y1"] <= selected["y2"] <= valid_set["y2"]):
            return False

        else:
            return True


    def controle_function (self, check, existing):
        """
        Checks if the coordinate is valid on the restrictions given
        """

        valid_set = check
        selected = existing
        x_valid = None
        x_selected = None

        # Checks if the house is partially in a house or between a house.
        if self.house_in_house(valid_set, selected) == False:
            return False

        # Checks if the house is in a vertical or horizontal position of the checkcoordianate
        elif valid_set["x1"] < selected["x1"] < valid_set["x2"] or \
        valid_set["x1"] < selected["x2"] < valid_set["x2"]:
            dist = min(abs(valid_set["y1"] - selected["y2"]), abs(selected["y1"] - valid_set["y2"]))
            return dist

        elif valid_set["y1"] < selected["y1"] < valid_set["y2"] or \
        valid_set["y1"] < selected["y2"] < valid_set["y2"]:
            dist = min(abs(valid_set["x1"] - selected["x2"]), abs(selected["x1"] - valid_set["x2"]))
            return dist

        # Calculates the if the house are diagonal from eachother.
        else:

            # Checks if the house are left or right from eachother and calculate minimum_distance.
            if (valid_set["x1"] - selected["x2"]) > 0:
                x_valid = "x1"
                x_selected = "x2"

            elif (valid_set["x2"] - selected["x1"]) < 0:
                x_valid = "x2"
                x_selected = "x1"

            else:
                return False

            dist1 = ((valid_set[x_valid] - selected[x_selected]) ** 2 + (valid_set["y1"] - selected["y1"]) **2)**0.5
            dist2 = ((valid_set[x_valid] - selected[x_selected]) ** 2 + (valid_set["y1"] - selected["y2"]) **2)**0.5
            dist3 = ((valid_set[x_valid] - selected[x_selected]) ** 2 + (valid_set["y2"] - selected["y1"]) **2)**0.5
            dist4 = ((valid_set[x_valid] - selected[x_selected]) ** 2 + (valid_set["y2"] - selected["y2"]) **2)**0.5

            dist = min(dist1, dist2, dist3, dist4)
            return dist

    def calculate_coordinate(self, calculation_point, house):
        return {"x1": calculation_point["x"], "x2": calculation_point["x"] + house.width,
                "y1": calculation_point["y"], "y2": calculation_point["y"] + house.length}

    def score(self, distance, house):
        """
        Calculates the score.
        """

        factor = ((distance - house.detachement)* house.price_improvement) + 1
        score = int(house.price * factor)
        return score

    def run(self, conn):
        score = []
        max_score = None
        minimum_distance = None

        for coordinate in self.coordinates:
            minimum_distance = None
            control = True
            selected = self.calculate_coordinate(coordinate , self.houses[self.key])

            for key, check in self.existing_coordinates.items():
                for check_coordinate in check:
                    valid = self.calculate_coordinate(check_coordinate, self.houses[key])
                    if valid == selected:
                        control = False
                        break

                    dist = self.controle_function(valid, selected)

                    if dist == False:
                        control = False
                        break

                    # checks if the distance bigger then the detachement
                    if dist < max(self.houses[key].detachement, self.houses[self.key].detachement):
                        control = False
                        break

                    elif minimum_distance == None or dist < minimum_distance:
                        minimum_distance = dist

                if control == False:
                    score.append(0)
                    break

            if control == False:
                control = True
            else:
                grid_space = self.calc_grid_distance(selected)
                distance = min(grid_space, minimum_distance)
                if grid_space < self.houses[self.key].detachement:
                    score.append(0)
                    break
                    
                else:
                    score.append(self.score(minimum_distance, self.houses[self.key]))

        index = score.index(max(score))
        max_score = {"score": score[index], "coordinate": self.coordinates[index]}
        conn.send(max_score)
        conn.close()
