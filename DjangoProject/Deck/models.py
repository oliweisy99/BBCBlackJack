from django.db import models

# Create your models here.

class Deck(models.Model):
    cards = models.CharField("Card", blank=True, null=True, max_length=250)