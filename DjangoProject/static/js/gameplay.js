function hit(){
	var cardFromDeck = newDeck.pop()
	var cardToAdd = createCardToAdd(cardFromDeck.image)
	addCardToPage(cardToAdd, true)
	setPoints(calculatePoints([cardFromDeck]), true)
	checkPoints()

}

function stand(){
	getNewCards()
	//check dealers hand.

	//show other dealer card.

	//calculate points
	//deal new hand

}