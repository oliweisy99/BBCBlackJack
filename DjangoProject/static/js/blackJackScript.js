

function playGame() {

	var playerName = playerNameField.value
	$.ajax({
			type: 'POST',
			url: '/game/playgame/',
			data: {
				name: playerName,
				csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
			},
			success: function (res) {
				console.log(res)
			}
		});

	// take the user's Name
	// deal the dealers cards
	// deal the user their cards
	// display the hit / stand buttons

}
