function addCardToPage(card, player) {
	if (player) {
		playerCards.appendChild(card)
	} else {
		dealerCards.appendChild(card)
	}
}

function showHiddenCard() {
	const hiddenCard = document.getElementById('hiddenCard')
	hiddenCard.remove()
	dealerCards.prepend(secretCard)

}


function addHiddenCard() {
	const el = document.createElement('img');
	el.id = "hiddenCard"
	el.classList.add("img-fluid")
	el.style.marginRight = "15px"
	el.style.marginTop = "10px"
	el.style.maxWidth = "150px"
	el.src = "/media/card_back.png/"
	dealerCards.appendChild(el)
}


function createCardToAdd(url) {

	const el = document.createElement('img');
	el.classList.add("img-fluid")
	el.style.marginRight = "15px"
	el.style.marginTop = "10px"
	el.style.maxWidth = "150px"
	el.src = "/media" + url

	return el
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

function getNewCards() {
	newDeck = cards

	return shuffleDeck(newDeck)
}

// end card function