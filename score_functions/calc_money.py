import sys

# get the path to the coordinates
sys.path.append(sys.path[0].replace('\\score_functions', '\\coordinates'))
from coordinate import *
from generator import *

sys.path.append(sys.path[0].replace('\\score_functions', '\\classes'))
from Opzet import *

sys.path.append(sys.path[0].replace('\\score_functions', '\\grid'))
from grid_houses import *

# sys.path.append(sys.path[0].replace('\\clases', '\\coordinates'))



def calc_money():
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
    # Create local variable that cannot be a result value and loop over the list of coordinates
    for s in range(len(comparisons)):
        selected = comparisons[s]

        # loop over all coordinates of selected house
        for i in range(4):
            minimum_distance = 9999.999

            # Loop over the list of houses to select one
            for house in range(len(comparisons)):
                if comparisons[house] == selected:
                    break

                # Loop over all coordinates of the other houses
                for j in range(4):
                    temp = ((selected[0][i] - comparisons[house][0][j])**2 + (selected[1][i] - comparisons[house][1][j])**2)**0.5
                    # print(temp)

                    # Check for house in house and append lisst of distances if so
                    if comparisons[house][0][0] < selected[0][i] < comparisons[house][0][2] and comparisons[house][1][0] < selected[1][i] < comparisons[house][1][1]:
                        # print(comparisons[house][0][0], comparisons[house][0][2], comparisons[house][1][0], comparisons[house][1][1], selected[0][i], selected[1][i])
                        distances.append("House in house")
                    if temp < minimum_distance:
                        minimum_distance = temp
                        # print(house, minimum_distance, sep='\t')
            temp = min(selected[0][i] - 0, 160 - selected[0][i], selected[1][i] - 0, 180 - selected[1][i])
            if temp < minimum_distance:
                minimum_distance = temp
                # print("BOUNDS", minimum_distance, sep='\t')
        distances.append(minimum_distance)

    # print(distances)
    return(coordinates, distances, comparisons)

def calc_validity(distances):
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
                    break
            elif i < 8:
                if distances[i] < 3:
                    return False
                    break
            else:
                if distances[i] < 2:
                    return False
                    break
    return True

def calc_score(distances):
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

def place_water(comparisons):
    """
    This function looks for the four biggest water bodies to be placed on the grid
    and returns its coordinates and dimensions
    """


if __name__ == "__main__":

    tries = 0
    instances = 0
    max_worth = 0
    max_distances = []
    max_coordinates = []

    while(instances < 1):
        money = []
        check = False
        while(check == False):
            tries += 1
            outcome = calc_money()
            coordinates = outcome[0]
            distances = outcome[1]
            comparions = outcome[2]
            check = calc_validity(distances)
            # print(instances)

        instances += 1
        worth = calc_score(distances)
        if worth > max_worth:
            max_worth = worth
            max_coordinates = coordinates
            max_distances = distances

    # print(coordinates)
    # print(distances)
    # print(worth)

    print(instances/tries * 100)
    print(max_worth)
    print(max_coordinates)
    print(max_distances)

    # Create visualiation
    grid = Grid(180, 160)
    total_houses = 20
    x = Visualator(grid.grid, LittleHouse(total_houses, 8, 8, 285000, 2), MediumHouse(total_houses, 10, 7.5, 399000), LargeHouse(total_houses, 11, 10.5, 610000))
    show(x.bokeh())
