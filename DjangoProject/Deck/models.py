from django.db import models


# Create your models here.
class Card(models.Model):
    suit = models.CharField("Suit", blank=True, null=True, max_length=250)
    name = models.CharField("Name", blank=True, null=True, max_length=250)
    number = models.IntegerField("Number", blank=True, null=True, default=0)
    image = models.ImageField()

    def __str__(self):
        return str(self.name + " of " + self.suit)
