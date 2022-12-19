from typing import Tuple,Union, NewType

from pygame.rect import Rect
from pygame.surface import Surface

Pos = NewType("Pos", Tuple[int, int])


class DrawComponent:
    image: Surface
    rect: Rect

    def __init__(
            self,
            image: Surface,
            pos: Pos
    ): ...

    def move(self, new_pos: Pos) -> None: ...

    def update(self, surface: Surface) -> None: ...


class AnimationComponent:
    images: dict[int, Surface]
    image: Union[Surface,None]
    rect: Rect

    def __init__(
            self,
            images: dict[int, Surface],
            pos: Pos
    ): ...

    def move(self, new_pos: Pos) -> None: ...

    def update(self,surface:Surface, index: int): ...
