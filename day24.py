class node:
		def __init__(self, x, y, lastM):
			self.x = x
			self.y = y
			self.lastM = lastM
def main():
	with open('input24.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		# Gets all numbers from map(input)
		nums = []
		positions = {}
		for y in range(len(input)):
			for x in range(len(input[y])):
				if input[y][x].isdigit():
					nums.append(input[y][x])
					pos = [x, y]
					positions[input[y][x]] = pos		
		nums.sort()

		# Gets shortest distance between each number (takes about 4 seconds)
		pairDistances = {}
		for i in range(len(nums)):
			x = positions[str(i)][0]
			y = positions[str(i)][1]
			for j in range(i + 1, len(nums)):
				root = node(x, y, '') 
				pairDistances[f"{i} {j}"] = shortestAtoB(root, nums[j], input)
		
		nums.remove('0')
		result = lengthOfShortestPath(pairDistances, nums, False)
		print(f"Part 1: {result}")
		result = lengthOfShortestPath(pairDistances, nums, True)
		print(f"Part 2: {result}")

def shortestAtoB(root, d, input):
	queue = [root]
	path = []
	steps = 0
	while True:
		newQueue = []
		for n in queue:
			if input[n.y][n.x] == d:
				return steps
			pos = f"{n.x},{n.y}"
			if pos in path:
				continue
			path.append(f"{n.x},{n.y}")
			# DOWN
			if n.lastM != 'U' and n.y != len(input) and input[n.y + 1][n.x] != '#':
				newQueue.append(node(n.x, n.y + 1, 'D'))
			# RIGHT
			if n.lastM != 'L' and n.x != len(input[n.y]) and input[n.y][n.x + 1] != '#':
				newQueue.append(node(n.x + 1, n.y, 'R'))
			# LEFT
			if n.lastM != 'R' and n.x != 0 and input[n.y][n.x - 1] != '#':
				newQueue.append(node(n.x - 1, n.y, 'L'))
			# UP
			if n.lastM != 'D' and n.y != 0 and input[n.y - 1][n.x] != '#':
				newQueue.append(node(n.x, n.y - 1, 'U'))
		queue = newQueue.copy()
		steps += 1
def lengthOfShortestPath(pairs, nodes, part2):
	min = 9999
	perms = []
	permutations(['0'], nodes, perms)
	for i in perms:
		pathLen = 0
		for j in range(len(i) - 1):
			pathLen += pairs[getKey(i, j)]
		if part2:
			pathLen += pairs[f"0 {i[len(i) - 1]}"]
		if pathLen < min:
			min = pathLen
	return min
def permutations(path, nodes, perms):
	if len(nodes) == 0:
		perms.append(path)
	for i in nodes:
		p = path.copy()
		p.append(i)
		n = nodes.copy()
		n.remove(i)
		permutations(p, n, perms)
def getKey(i, j):
	if int(i[j]) < int(i[j + 1]):
		return f"{i[j]} {i[j + 1]}"
	else:
		return f"{i[j + 1]} {i[j]}"

main()