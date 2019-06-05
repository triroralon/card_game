from deck import Deck
from player import Player

if __name__ == "__main__":
    print("Add Players")
    choice = input("enter name:")
# Players 1 - 4
    player1 = choice
    # dealer = Player("dealer")
    player1 = Player(player1)
    print(f"{player1} is Player 1")

    choice = input("Player 2 name is:")
    player2 = choice
    # dealer = Player("dealer")
    player2 = Player(player2)
    print(f"{player2} is Player 2")

    choice = input("Player 3 name is:")
    player3 = choice
    # dealer = Player("dealer")
    player3 = Player(player3)
    print(f"{player3} is Player 3")

    choice = input("Player 4 name is:")
    player4 = choice
    # dealer = Player("dealer")
    player4 = Player(player4)
    print(f"{player4} is Player 4")

    Dealer = Player("Dealer")

    print(f"{Dealer} \"Lets get ready to Rumble\"{player1}, {player2}, {player3}, {player4}.")
    print("\"Are you Ready?\"")
    print("[Dealer shuffles and deals cards]")
    Deck = Deck()
    Deck.shuffle()

    player1.draw(Deck)
    print(f"{player1} gets:")
    player1.showHand()

    player2.draw(Deck)
    print(f"{player2} gets:")
    player2.showHand()
    player3.draw(Deck)
    # print(f"{player1} gets:")
    # player3.showHand()
    # player4.draw(Deck)
    # player4.showHand()
    # Dealer.draw(Deck)
    # player1.draw(Deck)
    # player1.showHand()
    # player2.draw(Deck)
    # player2.showHand()
    # player3.draw(Deck)
    # player3.showHand()
    # player4.draw(Deck)
    # player4.showHand()
    # Dealer.draw(Deck)










# player2 = Player("rob")
# player3 = Player("cj")
# player4 = Player("me")

# # Players get dealt 2 cards
# # dealer gets 2 cards
# player1.draw(Deck)
# player2.draw(Deck)
# player3.draw(Deck)
# player4.draw(Deck)
# dealer.draw(Deck)

# player1.draw(Deck)
# player2.draw(Deck)
# player3.draw(Deck)
# player4.draw(Deck)
# dealer.draw(Deck)

# Player 1 ( ) reveals cards



#given choice, draw or stay



# dealer draws if value is under 16, draw card

#if dealer value > 21, dealer loses, all Players win