with open('input06.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	result = ""
	result2 = ""
	for	i in range(len(input[0]) - 1):
		alphDict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0,}
		for j in range(len(input)):
			alphDict[input[j][i]] += 1
		alphDict = sorted(alphDict.items(), key=lambda x: x[1], reverse=True)
		result += alphDict[0][0]
		for j in range(len(alphDict)):
			if j == 25 or alphDict[j + 1][1] == 0:
				result2 += alphDict[j][0]
				break
	print(f"Part 1: {result}")
	print(f"Part 2: {result2}")