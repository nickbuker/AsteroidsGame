from Sprite import Sprite


class Bullet(Sprite):

    def __init__(self, location, velocity, direction):
        Sprite.__init__(self, location, velocity, direction)
        self.lifetime = 20

    def update_lifetime(self):
        self.lifetime -= 1
