class Bullet(object):

    def __init__(self, location, direction):
        self.location = location
        self.velocity = 20
        self.direction = direction
        self.lifetime = 20

    def update_position(self):
        pass
