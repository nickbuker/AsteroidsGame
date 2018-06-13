from Sprite import Sprite


class Ship(Sprite):

    def __init__(self, location, velocity, direction):
        Sprite.__init__(self, location, velocity, direction)
        # TODO rotation working, fix appearance
        self.rotation_map = [
            [[0, -15], [-5, 10], [0, 5], [5, 10]],
            [[-5, -14], [-2, 11], [2, 5], [8, 8]],
            [[-9, -12], [2, 11], [3, 4], [10, 5]],
            [[-12, -9], [5, 10], [4, 3], [11, 2]],
            [[-14, -5], [8, 8], [5, 2], [11, -2]],
            [[-15, 0], [10, 5], [5, 0], [10, -5]],
            [[-14, 5], [11, 2], [5, -2], [8, -8]],
            [[-12, 9], [11, -2], [4, -3], [5, -10]],
            [[-9, 12], [10, -5], [3, -4], [2, -11]],
            [[-5, 14], [8, -8], [2, -5], [-2, -11]],
            [[0, 15], [5, -10], [0, -5], [-5, -10]],
            [[5, 14], [2, -11], [-2, -5], [-8, -8]],
            [[9, 12], [-2, -11], [-3, -4], [-10, -5]],
            [[12, 9], [-5, -10], [-4, -3], [-11, -2]],
            [[14, 5], [-8, -8], [-5, -2], [-11, 2]],
            [[15, 0], [-10, -5], [-5, 0], [-10, 5]],
            [[14, -5], [-11, -2], [-5, 2], [-8, 8]],
            [[12, -9], [-11, 2], [-4, 3], [-5, 10]],
            [[9, -12], [-10, 5], [-3, 4], [-2, 11]],
            [[5, -14], [-8, 8], [-2, 5], [2, 11]],
        ]
        self.rotation = 0
        self.update_point_list()
        self.thruster = 0

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
        self.direction = self.rotation
        # TODO fix rotation fluke
        # if self.velocity == 0:
        #     self.direction = self.rotation
        # elif (self.direction > self.rotation) and self.thruster:
        #     self.direction -= 1
        #     if self.direction < 0:
        #         self.direction = 19
        # elif (self.direction < self.rotation) and self.thruster:
        #     self.direction += 1
        #     if self.direction > 19:
        #         self.direction = 0
        return

    def update_point_list(self):
        tmp_points = []
        for points in self.rotation_map[self.rotation]:
            tmp_points.append([sum(p) for p in zip(self.location, points)])
        self.point_list = tmp_points
        return
