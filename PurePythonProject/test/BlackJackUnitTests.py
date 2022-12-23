import unittest
from unittest import mock

from Deck import Deck
from Game import Game

def hitOrStand(hitOrStand):
    return input(hitOrStand)

class GameTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()
        self.game = Game()

    def tearDown(self):  # this method will be run after each test
        self.deck = Deck()
        self.game = Game()


    def testNumberOfCards(self):  # any method beginning with 'test' will be run by unittest
        numberOfCards = len(self.deck.cards)
        self.assertEqual(numberOfCards, 52)

    def testNoTwoDecksTheSame(self):
        cardGame = self.game.deck
        self.assertNotEqual(cardGame, self.deck)

    def testHandIsValid(self):
        playerHand = self.game.player.hand
        self.game.initialisation()
        self.assertTrue(playerHand.cards[0] in self.deck.cards)
        self.assertTrue(playerHand.cards[1] in self.deck.cards)

    def testOpeningHandHasTwoCards(self):
        playerHand = self.game.player.hand
        self.game.initialisation()
        self.assertEqual(len(playerHand.cards), 2)


    def testHitScoreUpdate(self):
        # set up Hand manually.
        self.game.player.hand.addCard( ('Three', 3))
        self.game.player.hand.addCard( ('King', 10))

        #check hand score
        self.assertEqual(self.game.player.hand.points, 13)

        # hit simulated
        self.game.player.hand.addCard(('Nine', 9))

        #check hand score
        self.assertEqual(self.game.player.hand.points, 22)


    def testStandScoreUpdate(self):
        # set up Hand manually.
        self.game.player.hand.addCard(('Three', 3))
        self.game.player.hand.addCard(('King', 10))

        # check hand score
        self.assertEqual(self.game.player.hand.points, 13)

        # simluate stand
        self.game.player.stand(self.game.player.hand.points)

        self.assertEqual(self.game.player.score, 13)

    def testHandBelow21(self):
        self.game.player.hand.addCard(('Three', 3))
        self.game.player.hand.addCard(('King', 10))

        self.assertTrue(self.game.player.hand.checkPoints)

if __name__ == '__main__':
    unittest.main()

#
# Given my score is updated or evaluated
# When it is 21 or less
# Then I have a valid hand
#
# Given my score is updated
# When it is 22 or more
# Then I am ‘bust’ and do not have a valid hand
#
# Given I have a king and an ace
# When my score is evaluated
# Then my score is 21
#
# Given I have a king, a queen, and an ace
# When my score is evaluated
# Then my score is 21
#
# Given that I have a nine, an ace, and another ace
# When my score is evaluated
# Then my score is 21
