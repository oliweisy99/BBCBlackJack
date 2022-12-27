from django.http import JsonResponse


from Deck.models import Card


def playGame(request,name):

    cards = Card.objects.all()
    return JsonResponse({"name":name, "cards": list(cards.values())})
