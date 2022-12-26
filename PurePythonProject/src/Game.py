from Deck import Deck
from Player import Player


class Game:

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.highScore = 0

    def playGame(self):
        self.initialisation()

        keepPlaying = self.player.playerChoice(self.deck)

        if (keepPlaying):
            self.playGame()
        else:
            print("Bust! Game Over!")
            print(f"Your points were: {self.player.score}")
            self.playAgain()

    def initialisation(self):
        print("Let's Play! \nHere is your hand:")
        self.deck.resetDeck()
        print(f'{self.deck.cards[0][0]} & {self.deck.cards[1][0]}')  # show the first two cards to the player

        # add cards to the hand
        self.player.updateHand(self.deck.cards[0])
        self.player.updateHand(self.deck.cards[1])

        self.player.setNumberOfCardsPlayed(2)  # update the deck for how many cards have so far been dealt.

    def playAgain(self):
        self.checkHighScore(self.player.score)
        playAgain = input("Would you like to play again? (TYPE: Y or N)")

        if playAgain == "y" or playAgain == "Y":
            self.player = Player()
            self.playGame()

        if playAgain == "n" or playAgain == "N":
            print("Thanks for playing, goodbye!")

        if playAgain not in ["y", "Y", "n", "N"]:
            print("Error, please type Y for Yes, or N for No")
            self.playAgain()

    def checkHighScore(self, points):
        if self.highScore < points:
            self.highScore = points
            print("New HighScore!")