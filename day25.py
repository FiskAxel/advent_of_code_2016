def main():
	with open('input25.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		regs = { "a": 0, "b": 0, "c": 0, "d": 0 }
		clockS = "1"
		aStart = 0
		while len(clockS) < 100:
			regs["a"] = aStart
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
				elif s[0] == "out":
					if str(regs[s[1]]) == clockS[len(clockS) - 1]:
						clockS = "1"
						break
					clockS += str(regs[s[1]])
					if len(clockS) == 100:
						break
				i += 1
			aStart += 1
		result = aStart - 1 
		# Takes about a minute to run
		print(f"Part 1: {result}")

def cpy(regs, x, y):
	x = tryInt(x)
	if isinstance(tryInt(y), int):
		return
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

main()