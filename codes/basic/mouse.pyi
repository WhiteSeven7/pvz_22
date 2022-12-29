from ..game import Game


class Mouse:
    __game: Game
    __pos: tuple[int, int]

    def __init__(
            self,
            game: Game
    ): ...

    def get_pos(self) -> None: ...

    def read_pos(self) -> tuple[int, int]: ...
