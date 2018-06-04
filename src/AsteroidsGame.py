import sys
import pygame
from Ship import Ship
from pygame.locals import *

class AsteroidsGame:

    def __init__(self):
        pygame.init()
        self.CONST = {
            'WHITE': (255, 255, 255),
            'LIGHT_GRAY': (178, 178, 178),
            'BLACK': (0, 0, 0),
            'FPS': 60,
        }
        self.Display = pygame.display.set_mode((600, 600))
        self.Clock = pygame.time.Clock()
        pygame.display.set_caption('Asteroids')
        self.Ship = Ship()

    def start_game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        self.Ship.rotate(-90)
                        print('left')
                    elif event.key == pygame.K_d:
                        self.Ship.rotate(90)
                        print('right')
            self.Display.fill(self.CONST['BLACK'])
            pygame.draw.polygon(
                self.Display,
                self.CONST['LIGHT_GRAY'],
                self.Ship.pointlist
            )
            pygame.display.update()
            self.Clock.tick(self.CONST['FPS'])


if __name__ == '__main__':
    AG = AsteroidsGame()
    AG.start_game_loop()