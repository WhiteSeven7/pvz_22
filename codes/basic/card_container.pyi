Card = None
SunCollection = None
from ..assistance.fpn import FPN3
from ..assistance.timing import FiniteTiming


class CardContainer:
    clock: FiniteTiming

    def __init__(self): ...

    def update(self): ...


class SunSlot(CardContainer):
    card_number: int
    selected_cards: list[Card]
    sun_collection: SunCollection
    cards: dict[int, Card]

    def __init__(self, card_number: int): ...

    def loadcard(self, card: Card) -> None: ...

    def unloadcard(self, card: Card) -> None: ...

    def update(self): ...


class ConveyorSlot(CardContainer):
    cards: dict[FPN3, Card]

    def __init__(self): ...

    def update(self): ...


class TigerSlot(CardContainer):
    slot0: list
    slot1: list
    slot2: list

    def __init__(
            self,
            cardgroup: dict[Card, int]
    ): ...

    def run(self): ...

    def update(self): ...
