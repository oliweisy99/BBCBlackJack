function setPoints(points, player) {
	if (player) {
		playerPoints += points
		playerPointsElement.innerText = playerPoints
	} else {

		dealerPoints += points
	}
}

function showHiddenPoints() {

	dealerPointsElement.innerText = dealerPoints
}

function setHiddenPoints() {
	dealerPointsElement.innerText = "?"
}


function calculatePoints(cards) {
	var sum = 0
	cards.forEach(card => {

		sum += card.number
	})

	if (checkAce(cards) === 21) {
		console.log(cards)
		console.log(sum)
		return 21
	} else {
		return sum
	}
}

function checkAce(cards) {
	var tempPoints = 0
	var aceCount = 0
	cards.forEach(card => {
		if (card.name === "ace") {
			aceCount += 1
			if (aceCount === 1) {
				tempPoints += 11
			} else {
				tempPoints += 1
			}
		} else {
			tempPoints += card.number
		}
	})
	return tempPoints
}

function displayPoints() {

	totalPoints += playerPoints
	currentPlayerScore.innerText = totalPoints
	if (parseInt(highScorePoints.innerText) < totalPoints) {
		setHighScore(globalPlayerName, totalPoints)
	}

}

function setHighScore(playerName, score) {
	console.log('setting higscore')
	$.ajax({
		type: 'GET',
		url: `/game/setHighScore/${score}/${playerName}/`,
		success: function (res) {
			console.log(res)
			highScorePoints.innerText = res.highScore
			highScorePlayerName.innerText = res.name
		}
	});
}


function getHighScore() {
	$.ajax({
		type: 'GET',
		url: `/game/getHighScore/`,
		success: function (res) {

			highScorePoints.innerText = res.highScore
			highScorePlayerName.innerText = res.name
		}
	});

}

function checkPointsAgainstDealer() {

	if (playerPoints > dealerPoints) {
		//win and add points
		resultDiv.style.display = ""
		resultText.innerText = "Win!"

		choiceDiv.style.display = "none"
		displayPoints()
		continuePlayingDiv.style.display = ""

	}

	if (playerPoints < dealerPoints) {
		//lose and end game.
		choiceDiv.style.display = "none"
		resultDiv.style.display = ''
		resultText.innerText = "Bust!"
		restartDiv.style.display = ""
		totalPoints = 0
	}

	if (playerPoints === dealerPoints) {
		resultDiv.style.display = ""
		resultText.innerText = "Push!"
		choiceDiv.style.display = "none"
		continuePlayingDiv.style.display = ""
	}
}

function checkPoints() {
	resultDiv.style.display = ""

	if (playerPoints < 21) {
		resultText.innerText = "Hit!"

	}
	if (playerPoints === 21) {
		resultText.innerText = "BlackJack!"
		continuePlayingDiv.style.display = ""
		restartDiv.style.display = "none"
		choiceDiv.style.display = 'none'
		displayPoints()
		showHiddenCard()
		showHiddenPoints()
	}

	if (playerPoints > 21) {
		resultText.innerText = "Bust!"
		restartDiv.style.display = ""
		choiceDiv.style.display = "none"
		totalPoints = 0
		showHiddenCard()
		showHiddenPoints()
	}

}