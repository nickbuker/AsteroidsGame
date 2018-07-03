from math import pi, cos, sin
from Sprite import Sprite


class Ship(Sprite):

    def __init__(self, location, velocity, direction):
        Sprite.__init__(self, location, velocity, direction)
        self.rotation_map = [[[0, -15], [-5, 10], [0, 5], [5, 10]]]
        self.rotation_map_constructor()
        self.rotation = 0
        self.update_point_list()
        self.thruster = 0

    def rotation_map_constructor(self):
        for i in range(1, 20):
            tmp_points_list = []
            deg = 18 * i
            rad = -deg * pi / 180
            for point in self.rotation_map[0]:
                new_x = int(round((point[0] * cos(rad) - point[1] * sin(rad)), 0))
                new_y = int(round((point[1] * cos(rad) + point[0] * sin(rad)), 0))
                tmp_points_list.append([new_x, new_y])
            self.rotation_map.append(tmp_points_list)

    def update_rotation(self, rot_inc):
        self.rotation = (self.rotation + rot_inc) % 20
        return

    def update_velocity(self, vel_inc):
        if vel_inc > 0:
            self.thruster = 1
        else:
            self.thruster = 0
        if (self.velocity == 0 and vel_inc < 0) or (self.velocity > 10 and vel_inc > 0):
            return
        else:
            self.velocity += vel_inc
            return

    def update_direction(self):
        # self.direction = self.rotation
        # TODO fix rotation fluke
        if self.velocity == 0:
            self.direction = self.rotation
        elif (self.direction > self.rotation) and self.thruster:
            self.direction = (self.direction - 1) % 20
        elif (self.direction < self.rotation) and self.thruster:
            self.direction = (self.direction + 1) % 20
        return

    def update_point_list(self):
        tmp_points = []
        for points in self.rotation_map[self.rotation]:
            tmp_points.append([sum(p) for p in zip(self.location, points)])
        self.point_list = tmp_points
        return
