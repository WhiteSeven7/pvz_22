import pygame


class PeaShooter:
    image: pygame.Surface
    pos: tuple[int, int]

    def __init__(self): ...

    def draw(
            self,
            surf: pygame.Surface
    ): ...
