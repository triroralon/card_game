class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, Deck):
        self.hand.append(Deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            # print(card)
            card.show_card()

