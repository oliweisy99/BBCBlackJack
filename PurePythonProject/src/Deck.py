from random import shuffle

class Deck:

    def __init__(self):
        self.cards = [('Ace', 1), ('Two', 2), ('Three', 3), ('Four', 4), ('Five', 5),
                      ('Six', 6), ('Seven', 7), ('Eight', 8), ('Nine', 9), ('Ten', 10),
                      ('Jack', 10), ('Queen', 10), ('King', 10)] * 4
        self.shuffleDeck()

    def shuffleDeck(self):
        shuffle(self.cards)


    def resetDeck(self):
        deck = Deck()
        self.cards = deck.cards

