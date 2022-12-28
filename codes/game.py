import sys

import pygame
from .basic import level


FPS = 60
win_size = (800, 600)


class Game:

    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode(win_size)
        self.clock = pygame.time.Clock()
        self.level = level.Level()

    def __control(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def __draw(self, active):
        self.win.fill('black')
        self.win.blit(active, (0, 0))

    def run(self):
        while True:
            self.__control()
            self.level.one_frame()
            self.__draw(self.level.canvas)
            pygame.display.update()
            self.clock.tick(FPS)
