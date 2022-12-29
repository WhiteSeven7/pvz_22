class Parallelogram:
    pos_x: int
    pos_y: int
    ix: int
    iy: int
    jx: int
    jy: int

    @classmethod
    def create(
            cls,
            pos_x: int,
            pos_y: int,
            x1: int,
            y1: int,
            x2: int,
            y2: int
    ) -> 'Parallelogram': ...

    def __init__(
            self,
            pos_x: int,
            pos_y: int,
            ix: int,
            iy: int,
            jx: int,
            jy: int
    ) -> None: ...

    def area(self) -> int: ...

    def collide_point(
            self,
            x: int,
            y: int
    ) -> bool: ...
