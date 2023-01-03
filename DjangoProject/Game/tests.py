from django.test import TestCase

# Create your tests here.
from Game.views import playGame

from Game.models import Game

from Player.models import Player


class GameTestCase(TestCase):

    def setUp(self):
        cards = playGame("test", "name")
        self.assertTrue(cards.status_code, 200)


    def test_get_highscore(self):

        gameObj = Game.objects.first()
        self.assertFalse(gameObj)

        newPlayer = Player.objects.create(name="Test", score=1)
        self.assertEqual(newPlayer.name, "Test")

        newGameObj = Game.objects.create(player=newPlayer, highScore=20)
        self.assertTrue(newGameObj)
        self.assertEqual(newGameObj.player.name, "Test")
        self.assertEqual(newGameObj.highScore, 20)

        newGameObj.highScore = 21
        newGameObj.save()
        self.assertEqual(newGameObj.highScore, 21)


    def test_set_highscore(self):

        gameObj = Game.objects.first()
        self.assertFalse(gameObj)

        newPlayer = Player.objects.create(name="Test", score=1)
        self.assertEqual(newPlayer.name, "Test")

        newGameObj = Game.objects.create(player=newPlayer, highScore=20)

        newGameObj.highScore = 21
        newGameObj.save()
        self.assertEqual(newGameObj.highScore, 21)

