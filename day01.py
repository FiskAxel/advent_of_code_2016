with open('input01.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	instructions = input[0].split(", ")

	direction = 0	# 0North 1East 2South 3West
	x = 0
	y = 0

	for i in range(len(instructions)):
		LR = instructions[i][:1]
		if LR == 'L':
			direction = (direction - 1) % 4
		else:
			direction = (direction + 1) % 4

		distance = int(instructions[i][1:])
		if direction == 0:
			y += distance
		elif direction == 1:
			x += distance
		elif direction == 2:
			y -= distance
		elif direction == 3:
			x -= distance

	print(f"Part 1: {abs(x) + abs(y)}")

	# PART 2

	direction = 0	# 0North 1East 2South 3West
	x = 0
	y = 0
	visited = [f'{x},{y}']
	found = False
	for i in range(len(instructions)):
		LR = instructions[i][:1]
		if LR == 'L':
			direction = (direction - 1) % 4
		else:
			direction = (direction + 1) % 4

		distance = int(instructions[i][1:])
		
		for j in range(distance):
			if direction == 0:
				y += 1
			elif direction == 1:
				x += 1
			elif direction == 2:
				y -= 1
			elif direction == 3:
				x -= 1
			
			newLocation = str(x) + ',' + str(y)
			if newLocation in visited and found == False:
				print(f"part 2: {abs(x) + abs(y)}")
				found = True
				break
			else:
				visited.append(newLocation)
		if found:
			break