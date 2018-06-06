import sys
import pygame
import random
from Ship import Ship
from Asteroid import Asteroid
from Bullet import Bullet
from pygame.locals import *

class AsteroidsGame(object):

    def __init__(self):
        pygame.init()
        self.CONST = {
            'WHITE': (255, 255, 255),
            'GRAY': (120, 120, 120),
            'BLACK': (0, 0, 0),
            'FPS': 30,
        }
        self.key_states = {
            'l': 0,
            'r': 0,
            'f': 0,
            't': 0,
        }
        self.Display = pygame.display.set_mode((800, 800))
        self.Clock = pygame.time.Clock()
        pygame.display.set_caption('Asteroids')
        self.score = 0
        self.bullet_count_down = 0
        self.rotation_count_down = 0
        self.Ship = Ship()
        # instantiate lists
        self.bullets = []
        self.asteroids = []
        for _ in range(4):
            self.asteroids.append(Asteroid(location=[random.randint(0, 801), random.randint(0,801)], size=3))

    def start_game_loop(self):
        while True:
            for event in pygame.event.get():
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

            # use key_states
            if self.key_states['l'] and not self.rotation_count_down:
                self.Ship.update_rotation(1)
                self.rotation_count_down += 2
            if self.key_states['r'] and not self.rotation_count_down:
                self.Ship.update_rotation(-1)
                self.rotation_count_down += 2
            if self.key_states['f'] and not self.bullet_count_down:
                self.bullets.append(Bullet(location=self.Ship.point_list[0],
                                           direction=self.Ship.rotation))
                self.bullet_count_down += 15
            if self.key_states['t']:
                self.Ship.update_velocity(5)
            else:
                self.Ship.update_velocity(-1)
            self.Ship.update_direction()
            self.Ship.update_location()
            self.Ship.update_point_list()

            for asteroid in self.asteroids:
                asteroid.update_location()

            for bullet in self.bullets:
                bullet.update_location()

            # render
            self.Display.fill(self.CONST['BLACK'])

            for asteroid in self.asteroids:
                pygame.draw.circle(
                    self.Display,
                    self.CONST['GRAY'],
                    asteroid.location,
                    asteroid.radius,
                    2,
                )

            for bullet in self.bullets:
                pygame.draw.circle(
                    self.Display,
                    self.CONST['WHITE'],
                    bullet.location,
                    2,
                )

            pygame.draw.polygon(
                self.Display,
                self.CONST['WHITE'],
                self.Ship.point_list,
                2,
            )
            pygame.display.update()

            if self.bullet_count_down:
                self.bullet_count_down -= 1
            if self.rotation_count_down:
                self.rotation_count_down -= 1

            self.Clock.tick(self.CONST['FPS'])


if __name__ == '__main__':
    game = AsteroidsGame()
    game.start_game_loop()