from Sprite import Sprite


class Asteroid(Sprite):

    def __init__(self, location, velocity, direction, size, color):
        """ Asteroid class for Asteroids game

        Parameters
        ----------
        location : list of ints
            x, y pixel position of center of the asteroid
        velocity : int
            velocity of the asteroid (possible values 3, 6, 12)
        direction : int
            0-19 direction of travel of the asteroid
        size : int
            size of the asteroid (possible values 60, 30, 15)
        color : tuple of ints
            RGB values for asteroid color
        """
        Sprite.__init__(self, location, velocity, direction)
        self.size = size
        self.color = color
