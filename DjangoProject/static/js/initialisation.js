
$(document).ready(function setUpPage() {
	gamePlayDiv.style.display = "none"
	resultDiv.style.display = "none"
	choiceDiv.style.display = "none"
	pointsDiv.style.display = "none"
	currentScore.style.display = "none"

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

	// take the user's Name
	// deal the dealers cards
	// get the cards!
	// deal the user their cards
	// display the hit / stand buttons
}

function initialisation() {
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
	var newCardOne = newDeck.pop()
	var newCardTwo = newDeck.pop()
	var cardOne = createCardToAdd(newCardOne.image)
	var cardTwo = createCardToAdd(newCardTwo.image)
	if (player) {
		addCardToPage(cardOne, true)
		addCardToPage(cardTwo, true)
		setPoints(calculatePoints([newCardOne, newCardTwo]), true)
	} else {
		addCardToPage(cardOne, false)
		addCardToPage(cardTwo, false)
		setPoints(calculatePoints([newCardOne, newCardTwo]), false)
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