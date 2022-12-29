import sys

import pygame

from .basic.level import Level
from .basic.mouse import Mouse

FPS = 60
win_size = (800, 600)


class Game:

    def __init__(self):
        pygame.init()
        self.__events = pygame.event.get()
        self.win = pygame.display.set_mode(win_size)
        self.mouse = Mouse(self)
        self.clock = pygame.time.Clock()
        self.level = Level(self)

    def __events_update(self):
        self.__events = pygame.event.get()

    def __quit_determinate(self):
        for event in self.__events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def __draw(self, active):
        self.win.fill('black')
        self.win.blit(active, (0, 0))

    def get_events(self):
        return self.__events

    def run(self):
        while True:
            self.mouse.get_pos()
            self.__events_update()
            self.__quit_determinate()
            self.level.one_frame()
            self.__draw(self.level.get_canvas())
            pygame.display.update()
            self.clock.tick(FPS)
