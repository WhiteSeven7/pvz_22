import sys

import pygame
from .basic import level


FPS = 60
screen_size = (800, 600)


class Game:
    events: list[pygame.event.Event] = None

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        self.canvas = pygame.Surface(screen_size)
        self.level = level.Level()

    def _control(self):
        self.events = pygame.event.get()
        for event in self.events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self._control()
            self.level.run()
            self.screen.blit(self.canvas, (0, 0))
            pygame.display.update()
            self.clock.tick(FPS)
