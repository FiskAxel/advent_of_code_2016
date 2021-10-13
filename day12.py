def main():
	with open('input12.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		regs = { "a": 0, "b": 0, "c": 0, "d": 0 }
		i = 0
		while i < len(input):
			s = input[i].rsplit()
			if s[0] == "cpy":
				cpy(regs, s[1], s[2])
			elif s[0] == "inc":
				inc(regs, s[1])
			elif s[0] == "dec":
				dec(regs, s[1])
			elif s[0] == "jnz":
				i += jnz(regs, s[1], s[2])
				continue
			i += 1

		# PART 1 takes about 10 seconds
		result = regs["a"]
		print(f"Part 1: {result}")
		# (Part 2 worked with the code for part 1 but it took a couple of minutes)
		result = part2()
		print(f"Part 2: {result}")

def cpy(regs, x, y):
	x = tryInt(x)
	if isinstance(x, int):
		regs[y] = x
	else:
		regs[y] = regs[x]
def inc(regs, x):
	regs[x] = regs[x] + 1
def dec(regs, x):
	regs[x] = regs[x] - 1
def jnz(regs, x, y):
	x = tryInt(x) 
	if isinstance(x, int):
		if x != 0:
			if isinstance(tryInt(y), int):
				return int(y)
			else:
				return regs[y]
	elif regs[x] != 0:
		if isinstance(tryInt(y), int):
			return int(y)
		else:
			return regs[y]
	return 1

def tryInt(input):
	try:
		return int(input)
	except ValueError:
		return input
# translated and simplyfied version of my input (with c initialized to 1)
def part2():
	a = 1
	b = 1
	d = 26
	c = 7
	d += c
	
	# gets the fibonacci nr d + 2 (35)
	while d != 0:
		c = a
		a += b
		b = c
		d -= 1

	c = 16
	a += 12 * 16
	return a

main()