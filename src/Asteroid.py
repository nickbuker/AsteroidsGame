from BaseObject import BaseObject
import random


class Asteroid(BaseObject):

    def __init__(self, location, velocity, direction, size):
        BaseObject.__init__(self, location, velocity, direction)
        self.size = size
        self.direction = random.randint(0, 20)
