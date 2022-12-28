import pygame

from .peashooter import PeaShooter

win_size = 800, 600


class Level:
    def __init__(self):
        self.canvas = pygame.Surface(win_size)
        self.peashooter = PeaShooter()

    def one_frame(self):
        self.peashooter.draw(self.canvas)
