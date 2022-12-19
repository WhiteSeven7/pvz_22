from typing import Dict

from .timing import LoopTiming
from .fpn import FPN3

class StateMachine:
    master:
    state_timing: Dict[str, LoopTiming]
    state: str

    def __init__(
            self,
            master:  ,
            state_timing: Dict[str, LoopTiming],
            state
    ): ...

    def __getitem__(self, item: str)->LoopTiming: ...

    def __setitem__(self, key: str, value: LoopTiming)-> None: ...

    def __delitem__(self, key: str)->None: ...

    def change_state(self, state: str) -> None:...

    def update(self, time_speed:FPN3)-> None:...
