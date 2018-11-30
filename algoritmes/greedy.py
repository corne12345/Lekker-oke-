import math
from random import sample

class Greed(object):
    def __init__(self, grid, little, middle, large):
        self.grid = grid
        self.houses = {"little": little, "middle": middle, "large": large}
        self.points = {}
        self.number_point = 0
        self.count_little = 0
        self.count_middle = 0
        self.count_large = 0
        self.coordinates = self.create_coordinates()

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

    def create_list_house(self):
        list_houses = []
        for key in self.houses.keys():
            list_houses += [key] * int(self.houses[key].number)

        return list_houses


    def create_coordinates(self):
        random_list = self.create_list_house()
        house = sample(set(random_list), 1)[0]

        while self.number_point < len(random_list):
            self.number_point += 1
            if self.number_point < 1:

                # goes throught the grid
                for y_axe in range(len(self.grid)):
                    if y_axe < self.detachment[house] or \
                    y_axe > self.grid.length - self.detachment:
                        pass
                    else:
                        for x_axe in range(len(y_axe)):
                            if x_axe < self.detachment[house] or \
                            y_axe > self.grid.length - self.detachement:
                                pass
                            elif self.grid[y_axe][x_axe] in range(1, 5):
                                pass







    def calc_money(self):
        """
        This function takes the length of the newly created detachement around the houses
        and calculates the money each house yields.
        """

        print(self.houses)

        # Create sample coordinates by using random
        coordinates = Coordinates(20, 180, 160, self.grid).coordinates
        comparisons = []
        distances = []
        name = list(self.houses.keys())

        # Create 4-point coordinates for each house by making 3 large, 5 medium
        # and 12 small houses

        house_number = 0

        for house in list(self.houses.keys()):
            number_houses = int(self.houses[house].number)
            for count in range(number_houses):
                y = coordinates[house_number]['y']
                x = coordinates[house_number]['x']
                temp = CoordinatesHouse(x, y, self.houses[house])
                temp = temp.coordinates()

                comparisons.append(temp)
                house_number += 1


        print(comparisons)
        # Create local variable that can't be a result value and loop over the list of coordinates
        for s in range(len(comparisons)):
            selected = comparisons[s]
            print(selected)
            # loop over all coordinates of selected house
            for i in range(4):
                minimum_distance = 9999.999
                # Loop over the list of houses to select one
                for house in range(len(comparisons)):
                    if comparisons[house] == selected:
                        continue
                    # Loop over all coordinates of the other houses
                    for j in range(4):
                        if comparisons[house][0][1] > selected[0][i] > comparisons[house][0][2]:
                            temp = abs(comparisons[house][1][i] -  selected[1][i])

                        elif comparisons[house][1][0] > selected[1][i] > comparisons[house][1][1]:
                            temp = abs(comparisons[house][0][i] - selected[0][i])

                        else:
                            temp = ((selected[0][i] - comparisons[house][0][j])**2 + (selected[1][i] - comparisons[house][1][j])**2)**0.5



                        # Check for house in house and append lisst of distances if so
                        if comparisons[house][0][0] < selected[0][i] < comparisons[house][0][2] and comparisons[house][1][0] < selected[1][i] < comparisons[house][1][1]:
                            distances.append("House in house")
                        if temp < minimum_distance:
                            minimum_distance = temp
            temp = min(selected[0][0] - 0, 160 - selected[0][2], selected[1][0] - 0, 180 - selected[1][1])
            if temp < minimum_distance:
                minimum_distance = temp
            print(minimum_distance)
            distances.append(minimum_distance)

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
