
$(document).ready(function setUpPage() {
	gamePlayDiv.style.display = "none"
	resultDiv.style.display = "none"
	choiceDiv.style.display = "none"
	pointsDiv.style.display = "none"
	currentScore.style.display = "none"
	continuePlayingDiv.style.display = "none"
	restartDiv.style.display = "none"
	getHighScore()
})

function playGame() {
	generateDeck()
	var playerName = playerNameField.value
	if (playerNameField.value === "") {
		playerName = "Player"
	}
	$.ajax({
		type: 'GET',
		url: `/game/playgame/${playerName}`,
		success: function (res) {

			globalPlayerName = res.name.charAt(0).toUpperCase() + res.name.slice(1);
			cards = shuffleDeck(res.cards)
			getNewCards()
			initialisation()
		}
	});

}

function initialisation() {
	getNewCards()
	gameSetup.style.display = "none"

	gamePlayDiv.style.display = ""
	choiceDiv.style.display = ""
	currentScore.style.display = ""

	currentPlayerScore.innerText = playerPoints
	playerNameElement.innerText = globalPlayerName + ":"
	playerPointsElement.innerText = playerPoints
	dealerPointsElement.innerText = dealerPoints


	showInitialCards(true)
	showInitialCards(false)
}

function showInitialCards(player) {
	getNewCards()
	var newCardOne = newDeck.pop()
	var newCardTwo = newDeck.pop()
	var cardOne = createCardToAdd(newCardOne.image)
	var cardTwo = createCardToAdd(newCardTwo.image)
	if (player) {
		addCardToPage(cardOne, true)
		addCardToPage(cardTwo, true)
		setPoints(calculatePoints([newCardOne, newCardTwo]), true)
	} else {
		addHiddenCard()
		addCardToPage(cardOne, false)
		secretCard = cardTwo
		setPoints(calculatePoints([newCardOne, newCardTwo]), false)
		setHiddenPoints()
	}
}

function generateDeck() {

	$.ajax({
		type: 'GET',
		url: '/deck/generateCards/',
		success: function (res) {

		}
	});
}