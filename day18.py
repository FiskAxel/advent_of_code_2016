def main():
	input = ".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^"
	result = countDots(input)
	for i in range(1, 40):
		input = newLine(input)
		result += countDots(input)
	print(f"Part 1: {result}")

	# PART 2 takes about 2 minutes

	input = ".^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^"
	result = countDots(input)
	for i in range(1, 400000):
		input = newLine(input)
		result += countDots(input)
	print(f"Part 2: {result}")

def newLine(prev):
	newLine = ""
	for i in range(len(prev)):
		p = prev
		if i == len(prev) - 1:
			p = p + '.'
		
		if LC(p, i) or CR(p, i) or L(p, i) or R(p, i):
			newLine += '^'
		else:
			newLine += '.'
	return newLine
def LC(prev, i):
	if i == 0:
		return False
	if prev[i - 1] == '^' and prev[i] == '^' and prev[i + 1] == '.':
		return True
	return False
def CR(prev, i):
	if i == 0 and prev[i] == '^' and prev[i + 1] == '^':
		return True
	if prev[i - 1] == '.' and prev[i] == '^' and prev[i + 1] == '^':
		return True
	return False
def L(prev, i):
	if i == 0:
		return False
	if prev[i - 1] == '^' and prev[i] == '.' and prev[i + 1] == '.':
		return True
	return False
def R(prev, i):
	if i == 0 and prev[i] == '.' and prev[i + 1] == '^':
		return True
	if prev[i - 1] == '.' and prev[i] == '.' and prev[i + 1] == '^':
		return True
	return False
def countDots(input):
	output = 0
	for i in input:
		if i == '.':
			output += 1
	return output

main()