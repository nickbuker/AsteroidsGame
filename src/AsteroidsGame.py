import sys
import pygame
import random
from GameUtils import GameUtils
from Ship import Ship
from Asteroid import Asteroid
from Bullet import Bullet
from pygame.locals import *

class AsteroidsGame(GameUtils):

    def __init__(self):
        GameUtils.__init__(self)
        pygame.init()
        self.CONST = {
            'WHITE': (255, 255, 255),
            'GRAY': (120, 120, 120),
            'BLACK': (0, 0, 0),
            'FPS': 30,
        }
        self.Display = pygame.display.set_mode((800, 800))
        self.Clock = pygame.time.Clock()
        pygame.display.set_caption('Asteroids')
        self.score = 0
        self.bullet_count_down = 0
        self.rotation_count_down = 0
        self.Ship = Ship(location=[400,400],
                         velocity=0,
                         direction=0)
        # instantiate lists
        self.bullets = []
        self.asteroids = []
        for _ in range(4):
            self.asteroids.append(Asteroid(location=[random.randint(0, 801), random.randint(0,801)],
                                           velocity=3,
                                           direction=random.randint(0, 20),
                                           size=60))

    def start_game_loop(self):
        while True:
            self.check_events(pygame.event.get())

            # use key_states
            if self.key_states['l'] and not self.rotation_count_down:
                self.Ship.update_rotation(1)
                self.rotation_count_down += 2
            if self.key_states['r'] and not self.rotation_count_down:
                self.Ship.update_rotation(-1)
                self.rotation_count_down += 2
            if self.key_states['f'] and not self.bullet_count_down:
                self.bullets.append(Bullet(location=self.Ship.point_list[0],
                                           velocity=30,
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
                bullet.update_lifetime()

            for bullet in self.bullets:
                for asteroid in self.asteroids:
                    if asteroid.size >= asteroid.check_distance(bullet):
                        asteroid.live, bullet.live = False, False

            self.bullets = [bullet for bullet in self.bullets if bullet.lifetime and bullet.live]

            temp_asteroids = []
            for asteroid in self.asteroids:
                if not asteroid.live and asteroid.size == 60:
                    temp_asteroids.append((Asteroid(location=asteroid.location,
                                                    velocity=6,
                                                    direction=(asteroid.direction + 1) % 19,
                                                    size=30)))
                    temp_asteroids.append((Asteroid(location=asteroid.location,
                                                    velocity=6,
                                                    direction=(asteroid.direction - 1) % 19,
                                                    size=30)))
                if not asteroid.live and asteroid.size == 30:
                    temp_asteroids.append((Asteroid(location=asteroid.location,
                                                    velocity=12,
                                                    direction=(asteroid.direction + 1) % 19,
                                                    size=15)))
                    temp_asteroids.append((Asteroid(location=asteroid.location,
                                                    velocity=12,
                                                    direction=(asteroid.direction - 1) % 19,
                                                    size=15)))
            self.asteroids.extend(temp_asteroids)

            self.asteroids = [asteroid for asteroid in self.asteroids if asteroid.live]

            # render
            self.Display.fill(self.CONST['BLACK'])

            for asteroid in self.asteroids:
                pygame.draw.circle(
                    self.Display,
                    self.CONST['GRAY'],
                    asteroid.location,
                    asteroid.size,
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