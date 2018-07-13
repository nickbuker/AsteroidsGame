import sys
import pygame
from pygame.locals import *
from math import pi, sin, cos
from Asteroid import Asteroid


class GameUtils(object):

    def __init__(self):
        self.key_states = {
            'l': 0,
            'r': 0,
            'f': 0,
            't': 0,
        }

    def check_events(self, events):
        for event in events:
            # check for quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # poll keys for keys down and keys up
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.key_states['l'] = 1
                if event.key == pygame.K_d:
                    self.key_states['r'] = 1
                if event.key == pygame.K_SPACE:
                    self.key_states['f'] = 1
                if event.key == pygame.K_w:
                    self.key_states['t'] = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.key_states['l'] = 0
                if event.key == pygame.K_d:
                    self.key_states['r'] = 0
                if event.key == pygame.K_SPACE:
                    self.key_states['f'] = 0
                if event.key == pygame.K_w:
                    self.key_states['t'] = 0
        return

    def split_asteroids(self):
        temp_asteroids = []
        for asteroid in self.asteroids:
            if not asteroid.live and asteroid.size == 60:
                temp_asteroids.append((Asteroid(location=asteroid.location,
                                                velocity=6,
                                                direction=(asteroid.direction + 1) % 20,
                                                size=30,
                                                color=asteroid.color)))
                temp_asteroids.append((Asteroid(location=asteroid.location,
                                                velocity=6,
                                                direction=(asteroid.direction - 1) % 20,
                                                size=30,
                                                color=asteroid.color)))
            if not asteroid.live and asteroid.size == 30:
                temp_asteroids.append((Asteroid(location=asteroid.location,
                                                velocity=12,
                                                direction=(asteroid.direction + 1) % 20,
                                                size=15,
                                                color=asteroid.color)))
                temp_asteroids.append((Asteroid(location=asteroid.location,
                                                velocity=12,
                                                direction=(asteroid.direction - 1) % 20,
                                                size=15,
                                                color=asteroid.color)))
        return self.asteroids.extend(temp_asteroids)


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
        print str(i) + ': ' + str(tmp_points_list) + ','
