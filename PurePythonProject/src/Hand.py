from functools import reduce


class Hand:
    def __init__(self):
        self.cards = []
        self.points = 0

    def addCard(self, card):
        self.cards.append(card)
        self.calculatePoints()

    def aceCheck(self):
        tempPoints = 0
        aceCount = 0
        for card in self.cards:
            if card[0] == "Ace":
                aceCount += 1
                if aceCount == 1:
                    tempPoints += 11
                else:
                    tempPoints += 1
            else:
                tempPoints += card[1]
        if tempPoints == 21:
            return True
        else:
            return False

    def calculatePoints(self):
        self.points = 0
        for card in self.cards:
            self.points += card[1]

    def checkPoints(self):

        if self.points == 21:
            return 21
        if self.points < 21:
            return True
        else:
            return False
