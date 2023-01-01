const playerNameField = document.getElementById('playerNameField')
const gamePlayDiv = document.getElementById('gamePlayDiv')
const gameSetup = document.getElementById('gameSetup')
const resultDiv = document.getElementById('resultDiv')
const choiceDiv = document.getElementById('choiceDiv')
const pointsDiv = document.getElementById('pointsDiv')
const highScorePlayerName = document.getElementById('highScorePlayerName')
const highScorePoints = document.getElementById('highScorePoints')
const currentScore = document.getElementById('currentScore')
const currentPlayerScore = document.getElementById('currentPlayerScore')
const playerNameElement = document.getElementById('playerName')
const dealerPointsElement = document.getElementById('dealerPoints')
const playerPointsElement = document.getElementById('playerPoints')
const dealerCards = document.getElementById('dealerCards')
const playerCards = document.getElementById('playerCards')
const resultText = document.getElementById('resultText')
const continuePlayingDiv = document.getElementById('continuePlayingDiv')
const dealerFlipCardFront = document.getElementById('dealerFlipCardFront')
const dealerFlipCardBack = document.getElementById('dealerFlipCardBack')

var globalPlayerName = ""
var secretCard
var cards = []
var newDeck = []
var totalPoints = 0
var playerPoints = 0
var dealerPoints = 0
var highScore = 0