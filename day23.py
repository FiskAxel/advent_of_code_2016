def main():
	with open('input23.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		regs = { "a": 7, "b": 0, "c": 0, "d": 0 }
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
			elif s[0] == "tgl":
				v = tryInt(s[1])
				if isinstance(v, int):
					d = i + int(s[1])
				else:
					d = i + regs[v]
				if 0 <= d and d < len(input):
					input[d] = tgl(input[d])
			i += 1
		result = regs["a"]
		print(f"Part 1: {result}")
		result = part2()
		print(f"Part 2: {result}")

def tgl(instruction):
	ins = instruction.rsplit()
	if len(ins) == 2:
		if ins[0] == "inc":
			return "dec " + ins[1]
		else:
			return "inc " + ins[1]
	else:
		if ins[0] == "jnz":
			return "cpy " + ins[1] + " " + ins[2]
		else:
			return "jnz " + ins[1] + " " + ins[2]
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
# translation of my input with a inititialized to 12
def part2():
	# calculates a factorial (12! in this case)
	a = 12
	b = 11
	while True:
		a *= b
		b -= 1
		c = b * 2
		if c == 2:
			break
	# since c will be going from 20 to 18 to 16... to 2
	# every instruction an even number of steps from 
	# "tgl c" will get toggled(=>) once.
	c = - 16	#cpy -16 c
	c = 1		#(jnz 1 c) => cpy 1 c
	c = 94		#cpy 94 c
	d = 80		#(jnz 80 d) => cpy 80 d
	a += d * c	#inc a
				#(inc d) => dec d
				#jnz d -2
				#(inc c) => dec c
				#jnz c -5
	return a

main()