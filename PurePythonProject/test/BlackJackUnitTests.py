import unittest

from Deck import Deck
from Game import Game

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
        self.assertEqual(self.game.player.hand.points, 13)
        self.assertTrue(self.game.player.hand.checkPoints())

    def testHandAbove21(self):
        self.game.player.hand.addCard(('Three', 3))
        self.game.player.hand.addCard(('King', 10))
        self.game.player.hand.addCard(('Nine', 9))
        self.assertEqual(self.game.player.hand.points, 22)
        self.assertFalse(self.game.player.hand.checkPoints())

    def testHandEqualTo21(self):
        self.game.player.hand.addCard(('King', 10))
        self.game.player.hand.addCard(('Ace', 1))
        self.game.player.hand.addCard(('Queen', 10))
        self.assertEqual(self.game.player.hand.points, 21)
        self.assertEqual(self.game.player.hand.checkPoints(), 21)

    def testOneAceAnd10Card(self):
        self.game.player.hand.addCard(('King', 10))
        self.game.player.hand.addCard(('Ace', 1))
        self.assertTrue(self.game.player.hand.aceCheck())

    def testTwoAcesAnd10Card(self):
        self.game.player.hand.addCard(('King', 10))
        self.game.player.hand.addCard(('Ace', 1))
        self.game.player.hand.addCard(('Ace', 1))
        self.assertEqual(self.game.player.hand.points, 12)
        self.assertFalse(self.game.player.hand.aceCheck())

    def testTwoAcesAndNine(self):
        self.game.player.hand.addCard(('Nine', 9))
        self.game.player.hand.addCard(('Ace', 1))
        self.game.player.hand.addCard(('Ace', 1))
        self.assertTrue(self.game.player.hand.aceCheck())

    def testOneAceAndTwo10Cards(self):
        self.game.player.hand.addCard(('King', 10))
        self.game.player.hand.addCard(('Queen', 10))
        self.game.player.hand.addCard(('Ace', 1))
        self.assertEqual(self.game.player.hand.points, 21)
        self.assertEqual(self.game.player.hand.checkPoints(), 21)


if __name__ == '__main__':
    unittest.main()
