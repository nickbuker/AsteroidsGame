from Sprite import Sprite
import random


class Asteroid(Sprite):

    def __init__(self, location, velocity, direction, size, color):
        """ Asteroid class for Asteroids game

        Parameters
        ----------
        location : list of ints
            x, y pixel position of center of bullet
        velocity : int
            velocity of the asteroid (possible values 3, 6, 12)
        direction : int
            0-19 direction of the asteroid
        size : int
            size of the asteroid (possible values 60, 30, 15)
        color : tuple of ints
            RGB values for asteroid color
        """
        Sprite.__init__(self, location, velocity, direction)
        self.direction = random.randint(0, 20)
        self.size = size
        self.color = color
