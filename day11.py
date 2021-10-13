goalState = [ [], [], [], ["C1", "C2", "C3", "C4", "C5", 
							"G1", "G2", "G3", "G4", "G5"] ]
goalState2 = [ [], [], [], ["C1", "C2", "C3", "C4", "C5", "C6", "C7",
							 "G1", "G2", "G3", "G4", "G5", "G6", "G7"] ]
class node:
	def __init__(self, state, floor):
		self.state = state
		self.floor = floor
# Parsed input by hand.	
def main():
	input = [ 
		["C3", "C4", "C5", "G1", "G2", "G3", "G4", "G5"],
		["C1", "C2"],
		[],
		[] ]
	root = node(input, 0)
	prevStates = []
	prevStates.append(stateRep(input, 0))
	result = findShortestLenght(root, prevStates)
	print(f"Part 1: {result}")
	# Part 1 runs in about 3 seconds
	# Part 2 runs in about 40 seconds
	input = [ 
		["C3", "C4", "C5", "C6", "C7", "G1", "G2", "G3", "G4", "G5", "G6", "G7"],
		["C1", "C2"],
		[],
		[] ]
	root = node(input, 0)
	prevStates = []
	prevStates.append(stateRep(input, 0))
	result = findShortestLenght(root, prevStates)
	print(f"Part 2: {result}")

def findShortestLenght(root, prevs):
	queue = []
	queue.append(root)
	steps = 1
	while True:
		newQueue = []
		for n in queue:		
			if n.floor < 3:
				for a in n.state[n.floor]:
					if pairMove(a, n, n.floor + 1, prevs, newQueue) or singleMove(a, n, n.floor + 1, prevs, newQueue):
						return steps
			if n.floor > 0:
				for a in n.state[n.floor]:
					singleMove(a, n, n.floor - 1, prevs, newQueue)
					pairMove(a, n, n.floor - 1, prevs, newQueue)
		queue = newQueue.copy()
		steps += 1
def pairMove(a, n, d, p, q):
	for b in n.state[n.floor]:
		if a == b:
			continue
		if validPairMove(a, b, n, d):
			nState = movePair(a, b, n, d)
			if nState == goalState or nState == goalState2:
				return True
			sr = stateRep(nState, d)
			if sr not in p:
				p.append(sr)
				q.append(node(nState, d))
	return False
def singleMove(a, n, d, p, q):
	if validSingleMove(a, n, d):
		nState = moveSingle(a, n, d)
		if nState == goalState or nState == goalState2:
			return True
		sr = stateRep(nState, d)
		if sr not in p:
			p.append(sr)
			q.append(node(nState, d))
	return False
def validPairMove(a, b, n, d):
	# Missmatched chip and generator
	if a[0] != b[0] and a[1] != b[1]:
		return False
	# Matched chip and generator
	elif a[0] != b[0] and a[1] == b[1]:
		if len(n.state[d]) > 0:
			for i in n.state[d]:
				if i[0] == 'C':
					gm = 'G' + i[1]
					if gm not in n.state[d]:
					# destination contains unpaired chip
						return False
	# 2 generators					
	elif a[0] == 'G' and b[0] == 'G':
		ac = 'C' + a[1]
		bc = 'C' + b[1]
		# if current floor contains a, b or both chip and other generator
		f = n.state[n.floor]
		if ac in f and bc in f and len(f) > 4:
			return False
		if ac in f and bc not in f and len(f) > 3:
			return False
		if ac not in f and bc in f and len(f) > 3: 
			return False
		chips = []
		for i in n.state[d]:
			if i == ac or i == bc:
				continue
			if i[0] == 'C':
				mg = 'G' + i[1]
				if mg not in n.state[d]:
				# destination floor contains unpaird non-compatible chip
					return False
	# 2 chips
	else:
		gens = []
		for i in n.state[d]:
			if i[0] == 'G':
				gens.append(i)
		if len(gens) > 0:
			ag = 'G' + a[1]
			bg = 'G' + b[1]
			if not (ag in gens and bg in gens):
			# destination floor contains generator and not compatible for both
				return False
	return True
def validSingleMove(a, n, d):
	if a[0] == 'G': # Generator
		mc = 'C' + a[1]
		if mc in n.state[n.floor] and len(n.state[n.floor]) > 2:
		# matching chip on same floor with other items (generators)
			return False
		for i in n.state[d]:
			if i[0] == 'C' and i[1] != a[1]:
				mg = 'G' + i[1]
				if mg not in n.state[d]:
				# the destination floor contains unpaired chip not matching the moving generator
					return False
	else: # Chip
		chipFry = False
		for i in n.state[d]:
			if i[0] == 'G' and i[1] == a[1]:
				chipFry = False
				break
			if i[0] == 'G':
				chipFry = True
		if chipFry:
		# if the destination floor contains a non-compatable generator
			return False
			
	return True
def movePair(a, b, n, d):
	nState = [[],[],[],[]]
	nState[d].append(a)
	nState[d].append(b)
	for f in range(4):
		for i in n.state[f]:
			if i == a or i == b:
				continue
			nState[f].append(i)
		nState[f].sort()
	return nState
def moveSingle(a, n, d):
	nState = [[],[],[],[]]
	nState[d].append(a)
	for f in range(4):
		for i in n.state[f]:
			if i == a:
				continue
			nState[f].append(i)
		nState[f].sort()
	return nState
# Returns a state representation without chip- and generator-numbers and with added floor number
def stateRep(state, fNum):
	representation = []
	for s in state:
		floor = []
		for i in s:
			floor.append(i[0])
		floor.sort()
		representation.append(floor)
	representation.append(fNum)
	return representation

main()