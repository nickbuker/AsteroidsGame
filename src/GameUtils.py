from math import pi, sin, cos

def rotation():
    initial = [[0, -15], [-5, 10], [0, 5], [5, 10]]
    for i in range(1, 20):
        tmp_points_list = []
        deg = 18 * i
        rad = -deg * pi / 180
        for point in initial:
            new_x = int(round((point[0] * cos(rad) - point[1] * sin(rad)), 0))
            new_y = int(round((point[1] * cos(rad) + point[0] * sin(rad)), 0))
            tmp_points_list.append([new_x, new_y])
        print str(i) + ': ' +str(tmp_points_list) + ','

if __name__ == '__main__':
    rotation()