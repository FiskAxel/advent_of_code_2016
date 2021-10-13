VAL1 = 61
VAL2 = 17
result = -1
OUTPUT = [-1, -1, -1]
class bot:
	def __init__(self, lowNum, lowToBot, highNum, highToBot, value1, value2):
		self.lowNum = lowNum
		self.lowToBot = lowToBot
		self.highNum = highNum
		self.highToBot = highToBot
		self.value1 = value1
		self.value2 = value2
with open('input10.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	sortedBots = []
	for i in input:
		for j in input:
			if j[0] == 'b':
				split = j.split(' ')
				if int(split[1]) == len(sortedBots):
					sortedBots.append(j)
					continue
	bots = []
	for	i in sortedBots:
		l = i.split(' ')
		lowBot = False
		if l[5] == 'bot':
			lowBot = True
		highBot = False
		if l[10] == 'bot':
			highBot = True
		newBot = bot(int(l[6]), lowBot, int(l[11].rstrip()), highBot, 0, 0)
		bots.append(newBot)

	for i in input:
		if i[0] == 'v':
			l = i.split(' ')
			index = int(l[5])
			if bots[index].value1 == 0:
				bots[index].value1 = int(l[1])
			elif bots[index].value2 == 0:
				bots[index].value2 = int(l[1])
	
	notDone = True
	while notDone:
		notDone = False
		for i in range(len(bots)):
			if bots[i].value1 != 0 and bots[i].value2 != 0:
				notDone = True
				
				if bots[i].value1 == VAL1 and bots[i].value2 == VAL2  or  bots[i].value1 == VAL2 and bots[i].value2 == VAL1:
					result = i
				
				if bots[i].value1 < bots[i].value2:
					low = bots[i].value1
					high = bots[i].value2
				else:
					low = bots[i].value2
					high = bots[i].value1
				
				d = bots[i].lowNum
				if bots[i].lowToBot:
					if bots[d].value1 == 0: 
						bots[d].value1 = low
					elif bots[d].value2 == 0:
						bots[d].value2 = low
				elif d == 1 or d == 2 or d == 0:
					OUTPUT[d] = low
				
				d = bots[i].highNum
				if bots[i].highToBot:
					if bots[d].value1 == 0:
						bots[d].value1 = high
					elif bots[d].value2 == 0:
						bots[d].value2 = high
				elif d == 1 or d == 2 or d == 0:
					OUTPUT[d] = high
				
				bots[i].value1 = 0
				bots[i].value2 = 0

	print(f"Part 1: {result}")
	result = OUTPUT[0] * OUTPUT[1] * OUTPUT[2]
	print(f"Part 2: {result}")