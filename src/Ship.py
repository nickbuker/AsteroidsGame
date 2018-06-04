from math import pi, sin, cos

class Ship:

    def __init__(self):
        self.rotation_dict = {
            0: [[300, 285], [295, 310], [300, 305], [305, 310]],
            1: [[295, 286], [298, 311], [302, 305], [308, 308]],
            2: [[291, 288], [302, 311], [303, 304], [310, 305]],
            3: [[288, 291], [305, 310], [304, 303], [311, 302]],
            4: [[286, 295], [308, 308], [305, 302], [311, 298]],
            5: [[285, 300], [310, 305], [305, 300], [310, 295]],
            6: [],
            7: [],
            8: [],
            9: [],
            10: [],
            11: [],
            12: [],
            13: [],
            14: [],
            15: [],
            16: [],
            17: [],
            18: [],
            19: [],
        }
        self.velocity = [0.0, 0.0]
        self.thruster = False
        self.fire = False

    def rotate(self, rot):
        rad = 2 * pi * rot / 360
        new_points = []
        for p in [[300, 285], [295, 310], [300, 305], [305, 310]]:
            p_x, p_y = p[0] - 300, p[1] - 300
            new_x = round((p_x * cos(rad)) + (p_y * sin(rad)), 0)
            new_y = round((-p_x * sin(rad)) + (p_y * cos(rad)), 0)
            new_points.append([new_x + 300, new_y + 300])
        return new_points




