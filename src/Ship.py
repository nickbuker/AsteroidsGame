from math import pi, sin, cos

class Ship:

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
        self.velocity = [0, 0]
        self.thruster = False
        self.fire = False

    def update_rotation(self, rot_inc):
        self.rotation += rot_inc
        if self.rotation > 19:
            self.rotation = 0
        if self.rotation < 0:
            self.rotation = 19
        self.update_point_list()
        return

    def update_point_list(self):
        tmp_points = []
        for vert in self.rotation_dict[self.rotation]:
            tmp_points.append([sum(p) for p in zip(self.location, vert)])
        self.point_list = tmp_points
