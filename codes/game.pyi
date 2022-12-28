from typing import Union

import pygame

from basic.level import Level

win_size: tuple[int, int]
FPS: int


class Game:
    events: Union[list[pygame.event.Event], None]
    win: pygame.Surface
    clock: pygame.time.Clock
    level: Level

    def __init__(self): ...

    def __control(self): ...

    def __draw(self, active): ...

    def run(self): ...
