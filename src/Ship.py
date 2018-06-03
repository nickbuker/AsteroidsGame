from math import pi, sin, cos

class Ship:

    def __init__(self):
        self.pointlist = [[300, 285],
                          [295, 310],
                          [300, 305],
                          [305, 310]]
        self.velocity = [0.0, 0.0]
        self.thruster = False
        self.fire = False

    def rotate(self, rot):
        rad = 2 * pi * rot / 360
        for p in self.pointlist:
            new_x = int((p[0] * cos(rad)) + (p[1] * sin(rad)))
            new_y = int((-p[0] * sin(rad)) + (p[1] * cos(rad)))
            p[0], p[1] = new_x, new_y



