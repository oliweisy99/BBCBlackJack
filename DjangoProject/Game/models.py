from django.db import models


class Game(models.Model):
    player = models.ForeignKey('Player.Player', on_delete=models.CASCADE, blank=True, null=True,
                               related_name='game_player')
    highScore = models.IntegerField(default=0, blank=True, null=True)
