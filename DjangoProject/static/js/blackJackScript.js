var playerName = ""
var cards = []

$(document).ready(function setUpPage() {
	gamePlayDiv.style.display = "none"
	resultDiv.style.display = "none"
	choiceDiv.style.display = "none"
	pointsDiv.style.display = "none"
})


function playGame() {
	//already called! - generateDeck()
	var playerName = playerNameField.value
	if (playerNameField.value === "") {
		playerName = "Player"
	}
	$.ajax({
		type: 'GET',
		url: `/game/playgame/${playerName}`,
		success: function (res) {
			playerName = res.name
			cards = shuffleDeck(res.cards)

		}
	});

	// take the user's Name
	// deal the dealers cards
	// get the cards!
	// deal the user their cards
	// display the hit / stand buttons
}

function setHighScore(){
	console.log('setting highscore')
}


function shuffleDeck(cards) {
	let tempIndex = cards.length, randomisedIndex;
	// While there remain elements to shuffle.
	while (tempIndex !== 0) {

		// Pick a remaining element.
		randomisedIndex = Math.floor(tempIndex * Math.random());
		tempIndex--;

		// And swap it with the current element.
		[cards[tempIndex], cards[randomisedIndex]] = [
			cards[randomisedIndex], cards[tempIndex]];
	}
	return cards

}

function generateDeck() {

	$.ajax({
		type: 'GET',
		url: '/deck/generateCards/',
		success: function (res) {
			console.log(res)
		}
	});
}
