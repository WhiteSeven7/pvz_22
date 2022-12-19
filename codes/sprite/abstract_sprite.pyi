from ..assistance.drawing import AnimationComponent
from ..assistance.state_machine import StateMachine


class AbstractSprite:
    state_machine: StateMachine
    drawing: AnimationComponent
    containers:
    fixed_data:

    def __init__(
            self,
            state_machine: StateMachine,
            drawing: AnimationComponent,
            containers:,
            fixed_data:
    ): ...


class PeaShooter: