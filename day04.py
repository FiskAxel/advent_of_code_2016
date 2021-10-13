def main():
	with open('input04.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()	
		validIDs = []
		for i in input:
			parse = i.split('-')
			parse2 = parse.pop()
			parse2s = parse2.split('[')
			id = parse2s[0]
			checksum = parse2s[1][:-2]
			chars = "".join(parse)
			alphDict = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0, "i": 0, "j": 0, "k": 0, "l": 0, "m": 0, "n": 0, "o": 0, "p": 0, "q": 0, "r": 0, "s": 0, "t": 0, "u": 0, "v": 0, "w": 0, "x": 0, "y": 0, "z": 0,}
			for x in chars:
				alphDict[x] += 1
			alphDict = sorted(alphDict.items(), key=lambda x: x[1], reverse=True)
			control = ""
			for j in range(5):
				control += alphDict[j][0]
			if control == checksum:
				validIDs.append(id)
				if decrypt(chars, id) == "northpoleobjectstorage":
					print(f"Part 2: {id}")
		result = 0
		for x in validIDs:
			result += int(x)
		print(f"Part 1: {result}")
		# Takes about 10 seconds to run

def decrypt(name, id):
	for _ in range(int(id)):
		newName = ""
		for x in name:
			c = (ord(x) + 1)
			if c == 123:
				c = 97
			newName += chr(c)
		name = newName
	return name

main()