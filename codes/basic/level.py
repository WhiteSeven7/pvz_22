import pygame
from pygame import Vector2

from .peashooter import PeaShooter

win_size = 800, 600


class Level:
    def __init__(self, game):
        self.__game = game
        self.__canvas = pygame.Surface(win_size)
        self.peashooter = PeaShooter()

    def __control(self):
        for event in self.__game.get_events():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(Vector2(event.pos))
                if pygame.rect.Rect(100, 100, 100, 100).collidepoint(event.pos):
                    print('hi')

    def get_canvas(self):
        return self.__canvas

    def one_frame(self):
        self.__control()
        self.peashooter.draw(self.__canvas)
