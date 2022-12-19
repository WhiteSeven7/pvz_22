from ..assistance.fpn import FPN3
from ..assistance.timing import FiniteTiming

Zombie = None


class Buff:
    name: str
    master: None
    timing: FiniteTiming

    def __init__(
            self,
            keeping_time: FPN3,
            master: None = None
    ): ...


class IceSlow(Buff):
    def __init__(self, master: Zombie): ...

    def begin(self) -> None: ...
    
    def end(self)-> None:...

    def update(self, time_sped: FPN3) -> None: ...
