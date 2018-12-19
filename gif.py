import imageio
import os

def make_grid():
    images = []
    for count in range(20):
        print("house" + str(count))
        images.append(imageio.imread("house" + str(count) + ".png"))

    imageio.mimsave("file.gif", images, duration=0.75)

make_grid()
