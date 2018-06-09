from BaseObject import BaseObject


class Bullet(BaseObject):

    def __init__(self, location, velocity, direction):
        BaseObject.__init__(self, location, velocity, direction)
        self.lifetime = 20

    def update_lifetime(self):
        self.lifetime -= 1
