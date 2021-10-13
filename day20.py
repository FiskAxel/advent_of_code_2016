with open('input20.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	blackList = []
	for i in input:
		li = i.split('-')
		li = [int(li[0]), int(li[1].rstrip())]
		blackList.append(li)
	blackList.sort()
	prev = 0
	for i in blackList:
		if prev < i[0]:
			break
		prev = i[1] + 1
	result = prev
	print(f"Part 1: {result}")

	# PART 2

	result = 0
	prev = 0
	large = 0
	for i in blackList:
		if large < i[0] and i[0] <= 4294967296:
			result += i[0] - large
		if (i[1] + 1) > large:
			large = i[1] + 1
	if large < 4294967295:
		result += 4294967295 - large
	print(f"Part 2: {result}")