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
        self.houses = {"little": little, "middle": middle, "large": large}
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

        # (Vraagje: het number_point is toch nooit negatief, dus dan komt hij toch nooit in de if statement?)
        while self.number_point < len(random_list):
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
                            coordinate = self.calculate_coordinate({"x": x_axe, "y": y_axe }, self.houses[house])
                            if self.number_point < 1 and coordinate != None:
                                distance = self.calc_grid_distance(coordinate)
                                score.append(self.score(distance, self.houses[house]))
                            elif coordinate != None:
                                min_distance_other_house = self.min_distance_other_houses(self)


                            coordinates.append(coordinate)
            index = score.index(max(score))
            coordinate_max_score = deepcopy(coordinates[index])

            self.number_point += 1


    def calculate_coordinate(self, calculation_point, house):
        if calculation_point["x"] + house.width < self.grid.width - house.detachement and \
           calculation_point["y"] + house.length < self.grid.length - house.detachement:
           return {"x1": calculation_point["x"], "x2": calculation_point["x"] + house.width,
                   "y1": calculation_point["y"], "y2": calculation_point["y"] + house.length}
        else:
            pass

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


    # def calculate_point(self):
    #     # greedy algoritme
    #     while self.number_point < 20:
    #         sectors = {}
    #         degrees_vertical, degrees_horizontal = self.calculate_degree()
    #         max = []
    #         distances = []
    #         max_distance = 0
    #         max_degree = 0
    #         # calculate the first point with the greatest point
    #         if self.points == {}:
    #             self.points["point" + str(self.number_point)] =({"y": self.length/2, "x": self.width/2})
    #
    #         else:
    #
    #             # makes different sector
    #             if self.number_point == 1:
    #                 count = 0
    #                 for count in range(1, 5):
    #
    #                     # sector1
    #                     sector_x = self.points["point" + str(self.number_point)]["x"]
    #                     sector_y = self.points["point" + str(self.number_point)]["y"]
    #
    #                     if count == 2:
    #                         sector_x = self.width - sector_x
    #
    #                     elif count == 3:
    #                         sector_y = self.length - sector_y
    #
    #                     elif count == 4:
    #                         sector_x = self.width - sector_x
    #                         sector_y = self.length - sector_y
    #
    #                     for degree in degrees_horizontal:
    #                         distances.append({"degree": degree, "distance": (sector_x/degree)})
    #
    #                     for degree in degrees_vertical:
    #                         distances.append({"degree": degree, "distance": (sector_y/degree)})
    #
    #
    #             for key, values in sectors:
    #                 max_value = None
    #                 point = self.points["point" + str(self.number_point)]
    #
    #                 if distances == []:
    #                     print("No Data")
    #                 else:
    #                     if float(distance["distance"]) > max_distance:
    #                         print(max_distance)
    #                         max_distance = distance["distance"]
    #
    #             print(max_distance)
    #
    #             break


if __name__ == "__main__":
    Greed().calculate_point()
