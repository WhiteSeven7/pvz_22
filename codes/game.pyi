from typing import Union

import pygame
from pygame.event import Event

from basic.level import Level
from basic.mouse import Mouse

win_size: tuple[int, int]
FPS: int


class Game:
    mouse: Mouse
    __events: Union[list[Event], None]
    win: pygame.Surface
    clock: pygame.time.Clock
    level: Level

    def __init__(self): ...

    def __quit_determinate(self) -> None: ...

    def __events_update(self) -> None: ...

    def __draw(self, active) -> None: ...

    def get_events(self) -> list[Event]: ...

    def run(self) -> None: ...
