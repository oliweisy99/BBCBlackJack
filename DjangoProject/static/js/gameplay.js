function hit() {
	var cardFromDeck = newDeck.pop()
	var cardToAdd = createCardToAdd(cardFromDeck.image)
	addCardToPage(cardToAdd, true)
	setPoints(calculatePoints([cardFromDeck]), true)
	checkPoints()

}

function stand() {
	showHiddenCard()
	showHiddenPoints()
	checkPointsAgainstDealer()

}

function playAgain() {

	playerPoints = 0
	dealerPoints = 0

	restartDiv.style.display = 'none'
	resultDiv.style.display = 'none'

	dealerCards.innerHTML = ''
	playerCards.innerHTML = ''

	playGame()

}

function continuePlaying() {
	getNewCards()

	dealerPoints = 0
	playerPoints = 0
	dealerCards.innerHTML = ''
	playerCards.innerHTML = ''
	showInitialCards(true)
	showInitialCards(false)

	resultDiv.style.display = 'none'
	continuePlayingDiv.style.display = 'none'

	choiceDiv.style.display = ''

}