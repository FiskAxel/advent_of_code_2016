def main():
	with open('input15.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		discs = []
		num = 0
		for d in input:
			num += 1
			split = d.rsplit()
			pNum = int(split[3])
			pos = int(split[11][:-1]) + num
			disc = [pNum, pos]
			discs.append(disc)
		result = findButtonPressTiming(discs)
		print(f"Part 1: {result}")
		discs.append([11, len(discs) + 1])
		result = findButtonPressTiming(discs)
		# Takes about 5 seconds to run
		print(f"Part 2: {result}")

def findButtonPressTiming(discs):
	result = 0
	while(True):
		fits = 0
		result += 1
		for d in discs:
			if (d[1] + result) % d[0] == 0:
				fits += 1
			else:
				break
		if fits == len(discs):
			return result

main()