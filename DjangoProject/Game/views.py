from django.http import JsonResponse


from Deck.models import Card

from Player.models import Player
from .models import Game


def playGame(request,name):

    cards = Card.objects.all()
    return JsonResponse({"name":name, "cards": list(cards.values())})

def getHighScore(request):
    gameObj = Game.objects.first()

    if (gameObj):
        player = gameObj.player
        return JsonResponse({"highScore":gameObj.highScore, "name": player.name})
    else:
        return JsonResponse({"highScore": "0", "name": ""})

def setHighScore(request, score, name):

    if (Game.objects.all()).exists():

        gameObj = Game.objects.first()

        gameObj.highScore = score
        gameObj.player.name = name
        gameObj.player.save()
        gameObj.save()

        return JsonResponse({"highScore": gameObj.highScore, "name": gameObj.player.name})

    else:

        player = Player.objects.create(name=name, score=score)
        gameObj = Game.objects.create(highScore=score, player=player)

        return JsonResponse({"highScore": gameObj.highScore, "name": player.name})
