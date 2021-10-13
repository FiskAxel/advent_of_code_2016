def main():
	input = "11101000110010100"
	diskLen = 272
	filled = expand(input, diskLen)[0: diskLen:]
	result = getChecksum(filled)
	print(f"Part 1: {result}")

	# Part 2 is pretty slow (about 50s)

	diskLen = 35651584
	filled = expand(input, diskLen)[0: diskLen:]
	result = getChecksum(filled)
	print(f"Part 2: {result}")

def expand(stri, length):
	a = stri
	b = stri[::-1]
	nb = ""
	for c in b:
		if c == '1':
			nb += '0'
		else:
			nb += '1'
	
	output = a + '0' + nb
	if len(output) < length:
		output = expand(output, length)
	
	return output
def getChecksum(stri):
	while len(stri) % 2 == 0:
		newStri = ""
		i = 0
		while i < len(stri):
			if stri[i] == stri[i + 1]:
				newStri += '1'
			else:
				newStri += '0'
			i += 2
		stri = newStri
	return stri

main()