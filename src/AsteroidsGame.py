import pygame
import random
from GameUtils import GameUtils
from Ship import Ship
from Asteroid import Asteroid
from Bullet import Bullet


class AsteroidsGame(GameUtils):

    def __init__(self):
        GameUtils.__init__(self)
        pygame.init()
        self.CONST = {
            'WHITE': (255, 255, 255),
            'GRAY': (120, 120, 120),
            'BLACK': (0, 0, 0),
            'BLUE': (153, 255, 255),
            'PINK': (255, 153, 153),
            'GREEN': (229, 255, 204),
            'PURPLE': (255, 153, 255),
            'FPS': 30,
        }
        self.display = pygame.display.set_mode((800, 800))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('../assets/arial-bold.ttf', 24)
        pygame.display.set_caption('Asteroids')
        self.score = 0
        self.bullet_count_down = 0
        self.rotation_count_down = 0
        self.ship = Ship(
            location=[400, 400],
            velocity=0,
            direction=0
        )
        # instantiate lists
        self.bullets = []
        self.asteroids = []
        for color, location in {
            'BLUE': [random.randint(75, 125), random.randint(75, 125)],
            'PINK': [random.randint(675, 725), random.randint(75, 125)],
            'GREEN': [random.randint(75, 125), random.randint(675, 725)],
            'PURPLE': [random.randint(675, 725), random.randint(675, 725)],
        }.items():
            self.asteroids.append(Asteroid(
                location=location,
                velocity=3,
                direction=random.randint(0, 20),
                size=60,
                color=self.CONST[color])
            )

    def start_game_loop(self):
        while self.ship.live:
            self.check_events(pygame.event.get())

            # use key_states
            if self.key_states['l'] and not self.rotation_count_down:
                self.ship.update_rotation(1)
                self.rotation_count_down += 1
            if self.key_states['r'] and not self.rotation_count_down:
                self.ship.update_rotation(-1)
                self.rotation_count_down += 1
            if self.key_states['f'] and not self.bullet_count_down:
                self.bullets.append(Bullet(
                    location=self.ship.point_list[0],
                    velocity=30,
                    direction=self.ship.rotation)
                )
                self.bullet_count_down += 10
            if self.key_states['t']:
                self.ship.update_velocity(5)
            else:
                self.ship.update_velocity(-1)
            self.ship.update_direction()
            self.ship.update_location()
            self.ship.update_point_list()

            for asteroid in self.asteroids:
                asteroid.update_location()

            for bullet in self.bullets:
                bullet.update_location()
                bullet.update_lifetime()

            for asteroid in self.asteroids:
                if asteroid.size >= asteroid.check_distance(self.ship):
                    self.ship.live = False
                for bullet in self.bullets:
                    if asteroid.size >= asteroid.check_distance(bullet):
                        asteroid.live, bullet.live = False, False
                        self.score += 1

            self.split_asteroids()
            self.asteroids = [asteroid for asteroid in self.asteroids if asteroid.live]
            self.bullets = [bullet for bullet in self.bullets if bullet.lifetime and bullet.live]

            # render
            self.display.fill(self.CONST['BLACK'])

            for asteroid in self.asteroids:
                pygame.draw.circle(
                    self.display,
                    asteroid.color,
                    asteroid.location,
                    asteroid.size,
                    2,
                )

            for bullet in self.bullets:
                pygame.draw.circle(
                    self.display,
                    self.CONST['WHITE'],
                    bullet.location,
                    2,
                )

            pygame.draw.polygon(
                self.display,
                self.CONST['WHITE'],
                self.ship.point_list,
                2,
            )

            self.display.blit(self.font.render('Score: ' + str(self.score), True, self.CONST['WHITE']), (40, 40))

            pygame.display.update()

            if self.bullet_count_down:
                self.bullet_count_down -= 1
            if self.rotation_count_down:
                self.rotation_count_down -= 1

            self.clock.tick(self.CONST['FPS'])


if __name__ == '__main__':
    game = AsteroidsGame()
    game.start_game_loop()
