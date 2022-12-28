import pygame

from .peashooter import PeaShooter

win_size: tuple[int, int]


class Level:
    canvas: pygame.Surface
    peashooter: PeaShooter

    def __init__(self): ...

    def one_frame(self): ...
