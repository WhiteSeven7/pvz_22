from typing import Any,Callable

from .fpn import FPN3


class AbstractTiming:
    master: None
    __value: FPN3
    __pause_status: bool
    speed: FPN3

    def __init__(
            self,
            master: Any,
            value: FPN3 = FPN3(0, 0),
            pause_status: bool = False,
            speed: FPN3 = FPN3(1)
    ): ...

    def tick(self, speed: FPN3) -> None: ...

    def realvalue(self) -> FPN3: ...

    def value(self) -> int: ...

    def pause(self) -> None: ...

    def unpause(self) -> None: ...

    def changepause(self) -> None: ...


class InfiniteTiming(AbstractTiming): ...


class FiniteTiming(AbstractTiming):
    maxvalue: FPN3
    user_end: Callable

    def __init__(
            self,
            master: Any,
            maxvalue: FPN3,
            value: FPN3 = None,
            pause: bool = False,
            speed: FPN3 = None,
    ): ...

    def tick(self, speed: FPN3): ...

    @classmethod
    def user_end(cls) -> None: ...


class LoopTiming(FiniteTiming):
    def __init__(
            self,
            master: Any,
            maxvalue: FPN3,
            value: FPN3 = None,
            pause: bool = False,
            speed: FPN3 = None,
    ):...

    def tick(self, speed: FPN3): ...
