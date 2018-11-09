from Opzet import Water, Bungalow, SingleHome, Maison

class Total_Water(object):
    def __init__(self, object):
        self.object_list = []
        self.object = object

    def create(self):
        length = self.object.length
        width = self.object.width
        surface = self.object.surface
        dictionary = {
        "length" : length,
        "width" : width,
        "surface" : surface
        }

        self.object_list.append(dictionary)

if __name__ == "__main__":
    x = Total_Water(Water(2, 20))
    x.create()
    print(x.object_list)
