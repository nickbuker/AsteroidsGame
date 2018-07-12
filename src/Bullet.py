from Sprite import Sprite


class Bullet(Sprite):

    def __init__(self, location, velocity, direction):
        """ Bullet class for the Asteroids game

        Parameters
        ----------
        location : list of ints
            x, y pixel position of the center of the bullet
        velocity : int
            velocity of the bullet (always 30)
        direction : int
            0-19 direction of thevbullet
        """
        Sprite.__init__(self, location, velocity, direction)
        self.lifetime = 20

    def update_lifetime(self):
        """ Decays lifetime of the bullet

        Returns
        -------
        None
        """
        self.lifetime -= 1
        return
