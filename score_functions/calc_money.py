import sys

# get the path to the coordinates
sys.path.append(sys.path[0].replace('\\score_functions', '\\coordinates'))
from coordinate import *
from generator import *

sys.path.append(sys.path[0].replace('\\score_functions', '\\classes'))
from Opzet import *

sys.path.append(sys.path[0].replace('\\score_functions', '\\grid'))
from grid_houses import *

class Calculations(object):
    def calc_money(self):
        """
        This function takes the length of the newly created detachement around the houses
        and calculates the money each house yields.
        """

        # Create sample coordinates by using random
        coordinates = Coordinates(20, 180, 160).coordinates
        # print(coordinates)
        comparisons = []
        distances = []

        # Create 4-point coordinates for each house by making 3 large, 5 medium
        # and 12 small houses
        for i in range(20):
            y = coordinates[i]['y']
            x = coordinates[i]['x']
            if i < 3:
                temp = Coordinates_large(x, y)
            elif i < 8:
                temp = Coordinates_medium(x,y)
            else:
                temp = Coordinates_little(x,y)
            temp = temp.coordinates()
            comparisons.append(temp)

        # print(comparisons)
        # Create local variable that can't be a result value and loop over the list of coordinates
        for s in range(len(comparisons)):
            selected = comparisons[s]
            # loop over all coordinates of selected house
            for i in range(4):
                minimum_distance = 9999.999
                # Loop over the list of houses to select one
                for house in range(len(comparisons)):
                    if comparisons[house] == selected:
                        continue
                    # Loop over all coordinates of the other houses
                    for j in range(4):
                        temp = ((selected[0][i] - comparisons[house][0][j])**2 + (selected[1][i] - comparisons[house][1][j])**2)**0.5

                        # Check for house in house and append lisst of distances if so
                        if comparisons[house][0][0] < selected[0][i] < comparisons[house][0][2] and comparisons[house][1][0] < selected[1][i] < comparisons[house][1][1]:
                            distances.append("House in house")
                        if temp < minimum_distance:
                            minimum_distance = temp
            temp = min(selected[0][0] - 0, 160 - selected[0][2], selected[1][0] - 0, 180 - selected[1][1])
            if temp < minimum_distance:
                minimum_distance = temp
                # print("BOUNDS", minimum_distance, sep='\t')
            distances.append(minimum_distance)


        # print(distances)
        return(coordinates, distances, comparisons)

    def calc_validity(self, distances):
        """
        This function checks if the distances provided as a list as argument fulfill
        the constraints in terms of free space. It returns a boolean
        """
        if (len(distances) != 20):
            return False
        else:
            for i in range(len(distances)):
                if i < 3:
                    if distances[i] < 6:
                        return False
                elif i < 8:
                    if distances[i] < 3:
                        return False
                else:
                    if distances[i] < 2:
                        return False
        return True

    def calc_score(self, distances):
        """
        This function takes the distances of all the houses to its closest neighbour
        as input and returns the worth of the neigborhood
        """
        worth = 0
        for i in range(len(distances)):
            if i < 3:
                factor = ((distances[i] - 6) * 6)/100 + 1
                price = 610000 * factor
                worth += price
            elif i < 8:
                factor = ((distances[i] - 3) * 4)/100 + 1
                price = 399000 * factor
                worth += price
            else:
                factor = ((distances[i] - 2) * 3)/100 + 1
                price = 285000 * factor
                worth += price

        return worth

class Check (object):
    def __init__(self):

        self.calculations = Calculations()

    def check(self):
        instances = 0
        tries = 0
        max_worth = 0
        max_distances = []
        max_coordinates = []
        comparisons = []
        distances = None
        houses = {"large": [], "medium": [], "little": []}

        # total check
        while(instances < 1):
            money = []
            check = False
            while(check == False):
                tries += 1
                outcome = self.calculations.calc_money()
                coordinates = outcome[0]
                distances = outcome[1]
                comparisons = outcome[2]
                check = self.calculations.calc_validity(distances)

            instances += 1
            print(instances , "fixed")
            worth = self.calculations.calc_score(distances)
            if worth > max_worth:
                max_worth = worth
            max_coordinates = coordinates
            max_distances = distances

        # put the distances by the right house
        for count in range(len(max_coordinates)):
            if count < 3:
                houses["large"].append(max_coordinates[count])
            elif count < 8:
                houses["medium"].append(max_coordinates[count])
            else:
                houses["little"].append(max_coordinates[count])

        # Print characteristics of the best score
        print(instances/tries * 100)
        print(max_worth)
        print(max_coordinates)
        print(max_distances)

        return houses



def place_water(comparisons):
    """
    This function looks for the four biggest water bodies to be placed on the grid
    and returns its coordinates and dimensions
    """


if __name__ == "__main__":

    calculations = Check()
    instances, tries, max_coordinates, max_distances, max_worth = calculations.check()


    # Print characteristics of the best score
    print(instances/tries * 100)
    print(max_worth)
    print(max_coordinates)
    print(max_distances)
