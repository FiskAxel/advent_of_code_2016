import math
class node:
	def __init__(self, x, y, s, u):
		self.x = x
		self.y = y
		self.s = s
		self.u = u
with open('input22.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	input.pop(0) 
	input.pop(0)
	result = 0
	for n1 in input:
		no1 = n1.rsplit()
		for n2 in input:
			if n1 != n2:
				if no1[4] != "0%":
					no2 = n2.rsplit()
					if  int(no1[2][:len(no1[2]) - 1]) <= int(no2[3][:len(no2[3]) - 1]):
						result += 1
	print(f"Part 1: {result}") # PART 1 is pretty slow but ok

	# PART 2

	nodes = []
	for i in range(len(input)):
		n = input[i].rsplit()
		s = int(n[1][:len(n[1]) - 1])
		u = int(n[2][:len(n[2]) - 1])
		x = math.floor(i / 30)
		y = i % 30
		nodes.append(node(x, y, s, u))
	
	firstBiggieX = -1
	x = 0
	# Prints a map
	for n in nodes:
		if n.x > x:
			print()
			x += 1
		if n.u > 200: # Biggies
			print("!", end=" ")
			if firstBiggieX == -1:
				firstBiggieX = n.x
		elif n.u == 0: # Empty
			print("0", end=" ")
			empty = n
		elif n.x == 31 and n.y == 0: # Wanted
			print("W", end=" ")
		else:
			print("N", end=" ")
	# Shortest path to get Emtpy to 31, 0
	result = (empty.x - firstBiggieX + 1) + empty.y + (31 - firstBiggieX + 1) 
	# When Empty is at 31,0 (and Wanted is at 30,0)
	# It takes 30 * 5 moves to get Wanted to 0,0
	result += 30 * 5
	print(f"\nPart 2: {result}")