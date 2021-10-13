def main():
	with open('input09.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		decompressed = decompress(input[0])
		print(f'Part 1: {len(decompressed)}')
		print(f'Part 2: {v2decompLen(input[0])}')

def decompress(input):
	decompressed = ''
	i = 0
	while i < len(input):
		if input[i] == '(':
			marker = ''
			while input[i + 1] != ')':
				i += 1
				marker += input[i]
			starti = i + 2
			parse = marker.split('x')
			i += int(parse[0]) + 1
			for _ in range(int(parse[1])):
				decompressed += input[starti:(starti + int(parse[0]))]
		elif input[i] != ' ' or input[i] != '\n':
			decompressed += input[i]
		i += 1
	return decompressed
def v2decompLen(input):
	if '(' not in input:
		return len(input)
	output = 0
	i = 0
	while i < len(input):
		if input[i] == '(':
			marker = ''
			while input[i + 1] != ')':
				i += 1
				marker += input[i]
			i += 2
			parse = marker.split('x')
			length = int(parse[0])
			times = int(parse[1])
			output += v2decompLen(input[i:i + length]) * times
			i += int(parse[0])
		else:
			output += 1
			i += 1
	return output

main()