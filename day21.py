def main():
	with open('input21.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		result = part1("abcdefgh", input)
		print(f"Part 1: {result}")

		input.reverse()
		result = part2("fbgdceah", input)
		print(f"Part 2: {result}")

def part1(s, input):
	for i in input:
			l = i.split(' ')
			l[len(l) - 1] = l[len(l) - 1].rstrip()
			if l[0] == 'swap':
				if l[1] == 'position':
					s = swapPosition(s, int(l[2]), int(l[5]))
				if l[1] == 'letter':
					s = swapLetter(s, l[2], l[5])
			elif l[0] == 'rotate':
				if l[1] == 'based':
					s = rotateBased(s, l[6])
				else:
					s = rotateLR(s, l[1], int(l[2]))
			elif l[0] == 'reverse':
				s = reverse(s, int(l[2]), int(l[4]))
			elif l[0] == 'move':
				s = move(s, int(l[2]), int(l[5]))
	return s
def part2(s, input):
	for i in input:
			l = i.split(' ')
			l[len(l) - 1] = l[len(l) - 1].rstrip()
			if l[0] == 'swap':
				if l[1] == 'position':
					s = swapPosition(s, int(l[2]), int(l[5]))
				if l[1] == 'letter':
					s = swapLetter(s, l[2], l[5])
			elif l[0] == 'rotate':
				if l[1] == 'based':
					s = rotateBasedRev(s, l[6])
				else:
					if l[1] == "right": #LEFT GOES RIGHT AND VICE VERSA
						l[1] = "left"
					else:
						l[1] = "right" 
					s = rotateLR(s, l[1], int(l[2]))
			elif l[0] == 'reverse':
				s = reverse(s, int(l[2]), int(l[4]))
			elif l[0] == 'move':
				s = move(s, int(l[5]), int(l[2])) #SWAPPED
	return s
def swapPosition(s, x, y):
	newS = ""
	for i in range(len(s)):
		if i == x:
			newS += s[y]
		elif i == y:
			newS += s[x]
		else:
			newS += s[i]
	return newS
def swapLetter(s, a, b):
	newS = ""
	for c in s:
		if c == a:
			newS += b
		elif c == b:
			newS += a
		else:
			newS += c
	return newS
def rotateBased(s, a):
	n = s.index(a)
	if n >= 4:
		n += 1
	n += 1
	return rotateLR(s, "right", n)
def rotateBasedRev(s, a):
	n = 0
	while True:
		n += 1
		t = rotateLR(s, "left", n)
		if rotateBased(t, a) == s:
			return t 
def rotateLR(s, lr, n):
	newS = ""
	if lr == "right":
		for i in range(len(s)):
			newS += s[(i - n) % len(s)]
	else:
		for i in range(len(s)):
			newS += s[(i + n) % len(s)]
	return newS
def reverse(s, x, y):
	y += 1 #includes y index
	return s[:x] + s[x:y][::-1] + s[y:]
def move(s, a, b):
	newS = ""
	c = s[a]
	for i in range(len(s)):
		if i == a:
			continue
		if i == b:
			if a < b:
				newS += s[i] + c
			else:
				newS += c + s[i]
		else:
			newS += s[i]
	return newS

main()