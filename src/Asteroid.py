import random
from math import pi, sin, sqrt


class Asteroid(object):

    def __init__(self, location, size):
        self.location = location
        self.size = size
        size_dict = {
            3: [60, 3],
            2: [30, 6],
            1: [10, 12],
        }
        self.radius = size_dict[self.size][0]
        self.velocity = size_dict[self.size][1]
        self.direction = random.randint(0,20)
        self.is_split = False

    def update_location(self):
        deg = self.direction * 18
        if deg > 90 and deg < 270:
            y_mod = 1
        else:
            y_mod = -1
        rad = deg * pi / 180.0
        delta_x = self.velocity * sin(rad)
        delta_y = sqrt((self.velocity ** 2) - (delta_x ** 2))
        new_x = int(self.location[0] - delta_x)
        new_y = int(self.location[1] + delta_y * y_mod)
        if new_y > 800:
            new_y -= 800
        if new_y < 0:
            new_y += 800
        if new_x > 800:
            new_x -= 800
        if new_x < 0:
            new_x += 800
        self.location = [new_x, new_y]
        return

