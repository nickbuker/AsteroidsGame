import pygame
from math import pi, sin, sqrt


class Sprite(object, pygame.sprite.Sprite):

    def __init__(self, location, velocity, direction):
        # TODO sprite for collision detection
        # pygame.sprite.Sprite.__init__(self)
        self.location = location
        self.velocity = velocity
        self.direction = direction
        self.live = True

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

    def check_collision(self):
        pass
