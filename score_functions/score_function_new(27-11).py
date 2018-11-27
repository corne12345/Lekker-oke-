import random
DIMENSIONS = [160,180]
SMALL = [8, 8, 2]
MEDIUM = [10, 7.5, 3]
LARGE = [11, 10.5, 6]
NUM_HOUSES = 20

def create_valid_coordinates (house_type, valid_coordinates, DIMENSIONS, no_houses):
    counter = 0
    mistakes = 0
    while counter < no_houses:
        valid_set = {}
        x_coordinate = random.randint(0, DIMENSIONS[0])
        y_coordinate = random.randint(0, DIMENSIONS[1])

        grid_space = calc_min_grid_space(x_coordinate, y_coordinate, DIMENSIONS, house_type)
        if grid_space >= house_type[2]:
            valid_set = calc_all_coordinates (y_coordinate, x_coordinate, house_type)
            if len(valid_coordinates) > 0:
                if house_in_house(valid_set, valid_coordinates) == False:
                    valid_coordinates.append(valid_set)
                    counter += 1
                else:
                    mistakes +=1
            elif len(valid_coordinates) == 0:
                valid_coordinates.append(valid_set)
                counter += 1

def calc_min_grid_space (x_coordinate, y_coordinate, DIMENSIONS, house_type):
    """
    This function returns the shortes distance to the grid of a certain house with given coordinates
    """
    temp1 = x_coordinate - 0
    temp2 = DIMENSIONS[0] - house_type[0] - x_coordinate
    temp3 = y_coordinate - 0
    temp4 = DIMENSIONS[1] - house_type[1] - y_coordinate
    return min(temp1, temp2, temp3, temp4)

def calc_min_grid_space2 (valid_set, DIMENSIONS):
    """
    This function returns the shortes distance to the grid of a certain house with given coordinates
    """
    temp1 = valid_set["x1"] - 0
    temp2 = DIMENSIONS[0] - valid_set["x2"]
    temp3 = valid_set["y1"] - 0
    temp4 = DIMENSIONS[1] - valid_set["y2"]
    return min(temp1, temp2, temp3, temp4)

def calc_all_coordinates(y_coordinate, x_coordinate, house_type):
    return {"y1": y_coordinate, "x1": x_coordinate, "y2": y_coordinate + house_type[0], "x2": x_coordinate + house_type[1]}

def house_in_house (valid_set, valid_coordinates):
    for i in range(len(valid_coordinates)):
        test = valid_coordinates[i]
        x1 = test["x1"] <= valid_set["x1"] <= test["x2"]
        x2 = test["x1"] <= valid_set["x2"] <= test["x2"]
        y1 = test["y1"] <= valid_set["y1"] <= test["y2"]
        y2 = test["y1"] <= valid_set["y2"] <= test["y2"]
        if (x1 or x2) and (y1 or y2):
            return True
    return False

def calc_distance(valid_set, valid_coordinates, index):
    minimum_distance = 9999
    for i in range(len(valid_coordinates)):
        # Skip the comparison between the same data
        if i == index:
            continue
        selected = valid_coordinates[i]

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

        if dist < minimum_distance:
            minimum_distance = dist

    # Compare grid space and house space to find lowest
    grid_space = calc_min_grid_space2(valid_set, DIMENSIONS)
    return min(minimum_distance, grid_space)

def calc_score(distances):
    score = 0
    for i in range(int(len(distances) * 0.15)):
        if distances[i] < 6:
            return False
        factor = ((distances[i] - 6) * 6)/100 + 1
        price = 610000 * factor
        score += price
    for i in range(int(len(distances) * 0.15) , int(len(distances)* 0.40)):
        if distances[i] < 3:
            return False
        factor = ((distances[i] - 3) * 4)/100 + 1
        price = 399000 * factor
        score += price
    for i in range(int(len(distances) * 0.40), len(distances)):
        if distances[i] < 2:
            return False
        factor = ((distances[i] - 2) * 3)/100 + 1
        price = 285000 * factor
        score += price
    return score


valid_coordinates = []
create_valid_coordinates (LARGE, valid_coordinates, DIMENSIONS, NUM_HOUSES * 0.15)
create_valid_coordinates (MEDIUM, valid_coordinates, DIMENSIONS, NUM_HOUSES * 0.25)
create_valid_coordinates (SMALL, valid_coordinates, DIMENSIONS, NUM_HOUSES * 0.6)
print(valid_coordinates)

print('------------------------------------------------')

distances = []
for i in range(len(valid_coordinates)):
    valid_set = valid_coordinates[i]
    temp = calc_distance(valid_set, valid_coordinates, i)
    distances.append(temp)

print(distances)
print(calc_score(distances))
