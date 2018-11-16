class CheckHouse(object):
    def __init__(self, grid):
        self.grid = grid


    def check_coordinates(self, coordinates):
        for house in coordinates:
            if self.grid[house["y"]][house["x"]] in range(1, 4):
                place = coordinates.index(house)
                return False, place
        return True, None
