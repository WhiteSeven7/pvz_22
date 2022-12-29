import pygame


class Mouse:
    def __init__(self, game):
        self.__game = game
        self.__pos = 0, 0

    def get_pos(self):
        self.__pos = pygame.mouse.get_pos()

    def read_pos(self):
        return self.__pos
