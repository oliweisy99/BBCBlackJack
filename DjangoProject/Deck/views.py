from django.http import JsonResponse
from django.shortcuts import render
import os
from django.templatetags.static import static

# Create your views here.
from BBCBlackJack import settings
from .models import Card


def generateCards(request):
    cards = [('ace', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5),
             ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
             ('jack', 10), ('queen', 10), ('king', 10)]
    cardDict = dict(cards)


    files = os.listdir(os.path.join(settings.MEDIA_ROOT, "../media/cardPNGs/"))
    cards = []
    for file in files:
        splitArray = file.split("_")
        try:
            cards.append(splitArray)
            if not Card.objects.filter(suit=splitArray[2].replace(".png", ""),
                                       number=cardDict[splitArray[0]],
                                       name=splitArray[0]).exists():
                Card.objects.create(suit=splitArray[2].replace(".png", ""),
                                    number=cardDict[splitArray[0]],
                                    name=splitArray[0],
                                    image="/cardPNGs/" + file)

        except:
            continue

    return JsonResponse({})
