import random

def main(dieSides):
	game = createGame()
	
	playGame(game, dieSides, 1000000)

def createGame():
	game = {"board": {}, "CH": [], "CC": [], "loc": 0}
	
	for x in range(40):
		if x == 2 or x== 17 or x== 33:
			game["board"][x] = ("CH")
		elif x == 7 or x == 22 or x == 36:
			game["board"][x] = ("CC")
		elif x == 30:
			game["board"][x] = ("GJ")
		else:
			game["board"][x] = ("NA")
	
	game["CH"] = ["GO", "GJ"]
	for x in range(14):
		game["CH"].append(0)
	random.shuffle(game["CH"])

	game["CC"] = ["GO", "GJ", "RR", "RR", "UT", 11, 24, 39 ,5, -3, 0 ,0, 0, 0 ,0,0]
	random.shuffle(game["CC"])

	return game

def playGame(game, dieSides, tries):
	gameStats = {}
	dieOne = 0
	dieTwo = 0
	doublesCounter = 0
	
	for x in range(40):
		gameStats[x] = 0
	
	for x in range(tries):
		gameStats[game["loc"]] += 1

		dieOne = random.randint(1, dieSides)
		dieTwo = random.randint(1, dieSides)

		if dieOne == dieTwo:
			doublesCounter += 1
		else:
			doublesCounter = 0

		game["loc"] += dieOne + dieTwo

		if doublesCounter == 3:
			game["loc"] = 10
			doublesCounter = 0

		if game["loc"] >= 40:
			game["loc"] = game["loc"] % 40

		if game["board"][game["loc"]] == "NA":
			pass
		elif game["board"][game["loc"]] == "GJ":
			game["loc"] = 10
		else:
			game = playCard(game)

	#How does this work?
	gameStats = sorted(gameStats.items(), key = lambda x: x[1],  reverse = True)

	print(gameStats[0][0], gameStats[1][0], gameStats[2][0])
	print(gameStats)
			
def playCard(game):
	card = None 
	if game["board"][game["loc"]] == "CH":
		card = game["CH"][0]
		game["CH"].pop(0)
		game["CH"].append(card)
	elif game["board"][game["loc"]] == "CC":
		card = game["CC"][0]
		game["CC"].pop(0)
		game["CC"].append(card)

	if card == "GO":
		game["loc"] = 0
	elif card == "GJ":
		game["loc"] = 10
	elif card == "RR":
		if game["loc"] < 5:
			game["loc"] = 5
		elif game["loc"] < 15:
			game["loc"] = 15
		elif game["loc"] < 25:
			game["loc"] = 25
		elif game["loc"] < 35:
			game["loc"] = 35
		else:
			game["loc"] = 5
	elif card == "UT":
		if game["loc"] < 12:
			game["loc"] = 12
		else:
			game["loc"] = 28
	elif card > 0:
		game["loc"] = card
	elif card == 0:
		pass
	else:
		if game["loc"] > 2:
			game["loc"] += card
			if game["board"][game["loc"]] == "GJ":
				game["loc"] = 10
		else:
			game["loc"] = 39

	return game

main(4)
