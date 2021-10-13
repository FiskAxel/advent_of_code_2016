with open('input02.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()

	bCode = ""
	position = 5
	for i in range(len(input)):
		for j in range(len(input[i])):
			if input[i][j] == 'U' and position > 3:
				position -= 3
			elif input[i][j] == 'D' and position < 7:
				position += 3 
			elif input[i][j] == 'R' and position % 3 != 0:
				position += 1
			elif input[i][j] == 'L' and position % 3 != 1:
				position -= 1
		bCode += str(position)
	print(f"Part 1: {bCode}")

	# PART 2

	bCode = ""
	position = 5
	for i in range(len(input)):
		for j in range(len(input[i])):
			if input[i][j] == 'U' and position not in [1, 2, 4, 5, 9]:
				if position in [3, 13]:
					position -= 2
				else:
					position -= 4
			elif input[i][j] == 'D' and position not in [5, 9, 10, 12, 13]:
				if position in [1, 11]:
					position += 2
				else:
					position += 4
			elif input[i][j] == 'R' and position not in [1, 4, 9, 12, 13]:
				position += 1
			elif input[i][j] == 'L' and position not in [1, 2, 5, 10, 13]:
				position -= 1
		if position > 9:
			ABCD = "ABCD"
			bCode += ABCD[position % 10]
		else:
			bCode += str(position)
	print(f"Part 2: {bCode}")