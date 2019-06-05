from cards import Card
from random import randint

class Deck:
    def __init__(self):
        self.cards = []
        self.suits = ["Spades","Hearts","Clubs","Diamonds"]
        self.faces = ["Ace","King","Queen","Jack","10","9","8","7","6","5","4","3","2"]
        self.build()

    def build(self):
        for s in self.suits:
            for f in self.faces:
                self.cards.append(Card(f, s))

    def show_deck(self):
        for c in range (len(self.cards)):
            # print(self.cards[c])
            self.cards[c].show_card()
            # c.show_card()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()