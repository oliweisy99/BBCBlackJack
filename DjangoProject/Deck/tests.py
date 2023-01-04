from django.test import TestCase

from .models import Card
from .views import generateCards


class DeckTestCase(TestCase):
    def setUp(self):
        json = generateCards("test")
        self.assertEqual(json.status_code, 200)

    def test_cards_generated(self):
        card = Card.objects.filter(number=8)
        suit = Card.objects.filter(suit='hearts')
        self.assertEqual(card.count(), 4)
        self.assertEqual(suit.count(), 13)
        self.assertEqual(Card.objects.all().count(), 52)
