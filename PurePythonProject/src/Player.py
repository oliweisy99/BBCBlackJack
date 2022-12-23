from Deck import Deck
from Hand import Hand


class Player:

    def __init__(self):
        self.name = ""
        self.score = 0
        self.numberOfCardsPlayed = 0
        self.hand = Hand()

    def playerChoice(self, deck):

        choice = input("Would you like to hit or stand? (TYPE: H or S)")

        if choice == "h" or choice == "H":
            indexInDeck = self.numberOfCardsPlayed

            # check if end of deck reached
            try:
                newCardToDeal = deck.cards[indexInDeck]  # get the next card in the (shuffled) deck
            except:
                deck = Deck()  # when we run out of cards in the deck, make a new one!
                self.numberOfCardsPlayed = 0  # reset the number of cards played in the deck back to 0 for new deck
                indexInDeck = self.numberOfCardsPlayed
                newCardToDeal = deck.cards[indexInDeck]

            print(f'You Hit! Your new card is: {newCardToDeal[0]}')
            self.setNumberOfCardsPlayed(1)
            self.updateHand(newCardToDeal)

            points = self.hand.checkPoints()
            # check what points are in respect to 21.

            if (self.hand.aceCheck()):
                points = 21

            if points == 21:
                print("You got 21! Next Round we go!")
                self.stand(self.hand.points)
                self.resetHand()
                print(f'Your total points are now : {self.score}')
                return True
            else:
                if points:  # if we did not exceed 21
                    return self.playerChoice(deck)
                else:
                    print(f"Uh oh, your hands points are {self.hand.points}")
                    return False

        if choice == "S" or choice == "s":
            self.stand(self.hand.points)
            self.resetHand()
            print(f'Stand! Your total points are now : {self.score}')
            return True

        if choice not in ["S", "s", "h", "H"]:
            print("Error. Please type either 'H' for Hit, or 'S' for Stand")
            return self.playerChoice(deck)

    def setNumberOfCardsPlayed(self, numberOfCardsPlayed):
        self.numberOfCardsPlayed += numberOfCardsPlayed

    def resetHand(self):
        self.hand = Hand()

    def stand(self, standPoints):
        self.score += standPoints

    def updateHand(self, card):
        self.hand.addCard(card)
