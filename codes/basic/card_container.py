class CardContainer:
    ...


class SunSlot(CardContainer):
    def __init__(self, cardnumber):
        super().__init__()
        self.card_number = cardnumber
        self.selected_cards = []
        self.sun_collection = None
        self.cards = None

    def loadcard(self, card):
        if len(self.selected_cards) >= self.card_number:
            self.selected_cards.append(card)

    def unloadcard(self, card):
        self.selected_cards.remove(card)

    def update(self):
        ...
