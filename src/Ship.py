from BaseObject import BaseObject


class Ship(BaseObject):

    def __init__(self, location, velocity, direction):
        BaseObject.__init__(self, location, velocity, direction)
        # TODO rotation working, fix appearance
        self.rotation_dict = {
            0: [[0, -15], [-5, 10], [0, 5], [5, 10]],
            1: [[-5, -14], [-2, 11], [2, 5], [8, 8]],
            2: [[-9, -12], [2, 11], [3, 4], [10, 5]],
            3: [[-12, -9], [5, 10], [4, 3], [11, 2]],
            4: [[-14, -5], [8, 8], [5, 2], [11, -2]],
            5: [[-15, 0], [10, 5], [5, 0], [10, -5]],
            6: [[-14, 5], [11, 2], [5, -2], [8, -8]],
            7: [[-12, 9], [11, -2], [4, -3], [5, -10]],
            8: [[-9, 12], [10, -5], [3, -4], [2, -11]],
            9: [[-5, 14], [8, -8], [2, -5], [-2, -11]],
            10: [[0, 15], [5, -10], [0, -5], [-5, -10]],
            11: [[5, 14], [2, -11], [-2, -5], [-8, -8]],
            12: [[9, 12], [-2, -11], [-3, -4], [-10, -5]],
            13: [[12, 9], [-5, -10], [-4, -3], [-11, -2]],
            14: [[14, 5], [-8, -8], [-5, -2], [-11, 2]],
            15: [[15, 0], [-10, -5], [-5, 0], [-10, 5]],
            16: [[14, -5], [-11, -2], [-5, 2], [-8, 8]],
            17: [[12, -9], [-11, 2], [-4, 3], [-5, 10]],
            18: [[9, -12], [-10, 5], [-3, 4], [-2, 11]],
            19: [[5, -14], [-8, 8], [-2, 5], [2, 11]],
        }
        self.rotation = 0
        self.update_point_list()
        self.thruster = 0

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
        for vert in self.rotation_dict[self.rotation]:
            tmp_points.append([sum(p) for p in zip(self.location, vert)])
        self.point_list = tmp_points
        return
