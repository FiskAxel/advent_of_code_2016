with open('input03.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()

	result = 0
	for i in range(len(input)):
		numbers = input[i].split()
		nums = [int(x) for x in numbers]
		if sum(nums) - max(nums) > max(nums):
			result += 1
	print(f"Part 1: {result}")

	result = 0
	for h in range(3):
		for i in range(0, len(input) - 1, 3):
			nums = []
			for	j in range(3):
				num = input[i + j].split()
				nums.append(int(num[h]))
			if sum(nums) - max(nums) > max(nums):
				result += 1
	print(f"Part 2: {result}")