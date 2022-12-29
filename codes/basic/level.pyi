import pygame

from .peashooter import PeaShooter
from ..game import Game

win_size: tuple[int, int]


class Level:
    __game: Game
    __canvas: pygame.Surface
    peashooter: PeaShooter

    def __init__(
            self,
            game: Game
    ): ...

    def __control(self) -> None: ...

    def get_canvas(self) -> None: ...

    def one_frame(self) -> None: ...
