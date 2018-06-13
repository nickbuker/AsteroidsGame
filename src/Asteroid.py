from Sprite import Sprite
import random


class Asteroid(Sprite):

    def __init__(self, location, velocity, direction, size):
        Sprite.__init__(self, location, velocity, direction)
        self.size = size
        self.direction = random.randint(0, 20)
