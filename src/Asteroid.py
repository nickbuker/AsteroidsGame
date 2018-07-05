from Sprite import Sprite
import random


class Asteroid(Sprite):

    def __init__(self, location, velocity, direction, size, color):
        Sprite.__init__(self, location, velocity, direction)
        self.direction = random.randint(0, 20)
        self.size = size
        self.color = color
