class Card:
    def __init__(self, face, suit):
        self.suit = suit
        self.face = face

    def show_card(self):
        # print(self)
        print (f"{self.face} of {self.suit}")

    def __str__(self):
        # print (f"{self.face} of {self.suit}")
        return f"{self.face} of {self.suit}"
