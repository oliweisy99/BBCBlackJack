function setPoints(points, player) {
	if (player) {
		playerPoints += points
		playerPointsElement.innerText = playerPoints
	} else {
		dealerPoints += points
		dealerPointsElement.innerText = dealerPoints
	}
}

function calculatePoints(cards) {
	var sum = 0
	cards.forEach(card => {
		console.log(card)
		sum += card.number
	})
	return sum
}

function displayPoints(){

}

function setHighScore() {
	console.log('setting highscore')
}

function checkPointsAgainstDealer() {

	if (playerPoints > dealerPoints) {
		//win and add points
	}

	if (playerPoints < dealerPoints) {
		//lose and end game.
	}

	if (playerPoints === dealerPoints) {
		//push!
	}
}

function checkPoints() {
	resultDiv.style.display = ""

	if (playerPoints < 21) {
		resultText.innerText = "Hit!"
		//hit
	}
	if (playerPoints === 21) {
		resultText.innerText = "BlackJack!"
		checkPointsAgainstDealer()

	}

	if (playerPoints > 21) {
		resultText.innerText = "Bust!"

	}

}