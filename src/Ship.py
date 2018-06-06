from math import pi, sin, sqrt

class Ship(object):

    def __init__(self):
        self.location = [400, 400]
        # TODO rotation working, fix appearance
        self.rotation_dict = {
            0: [[0, -15], [-5, 10], [0, 5], [5, 10]],
            1: [[-5, -14], [-5, 2], [2, 5], [8, 8]],
            2: [[-9, -12], [-4, 3], [3, 4], [10, 5]],
            3: [[-14, -5], [-2, 5], [5, 2], [11, -2]],
            4: [[-15, 0], [0, 5], [5, 0], [10, -5]],
            5: [[-14, 5], [2, 5], [5, -2], [8, -8]],
            6: [[-12, 9], [3, 4], [4, -3], [5, -10]],
            7: [[-9, 12], [4, 3], [3, -4], [2, -11]],
            8: [[-5, 14], [5, 2], [2, -5], [-2, -11]],
            9: [[0, 15], [5, 0], [0, -5], [-5, -10]],
            10: [[5, 14], [5, -2], [-2, -5], [-8, -8]],
            11: [[9, 12], [4, -3], [-3, -4], [-10, -5]],
            12: [[12, 9], [3, -4], [-4, -3], [-11, -2]],
            13: [[14, 5], [2, -5], [-5, -2], [-11, 2]],
            14: [[15, 0], [0, -5], [-5, 0], [-10, 5]],
            15: [[14, -5], [-2, -5], [-5, 2], [-8, 8]],
            16: [[12, -9], [-3, -4], [-4, 3], [-5, 10]],
            17: [[9, -12], [-4, -3], [-3, 4], [-2, 11]],
            18: [[5, -14], [-5, -2], [-2, 5], [2, 11]],
            19: [[0, -15], [-5, 0], [0, 5], [5, 10]],
        }
        self.rotation = 0
        self.update_point_list()
        self.thruster = 0
        self.velocity = 0
        self.direction = 0

    def update_rotation(self, rot_inc):
        self.rotation += rot_inc
        if self.rotation > 19:
            self.rotation = 0
        if self.rotation < 0:
            self.rotation = 19
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
        if self.velocity == 0:
            self.direction = self.rotation
        elif (self.direction > self.rotation) and self.thruster:
            self.direction -= 1
        elif (self.direction < self.rotation) and self.thruster:
            self.direction += 1
        return

    def update_location(self):
        deg = self.direction * 18
        if deg > 90 and deg < 270:
            y_mod = 1
        else:
            y_mod = -1
        rad = deg * pi / 180.0
        delta_x = self.velocity * sin(rad)
        delta_y = sqrt((self.velocity ** 2) - (delta_x ** 2))
        new_x = self.location[0] - delta_x
        new_y = self.location[1] + delta_y * y_mod
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

    def update_point_list(self):
        tmp_points = []
        for vert in self.rotation_dict[self.rotation]:
            tmp_points.append([sum(p) for p in zip(self.location, vert)])
        self.point_list = tmp_points
        return
