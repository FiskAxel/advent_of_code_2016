def main():
	with open('input07.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()		
		result = 0
		result2 = 0
		for	ip in input:
			N = False
			S = True
			normals = []
			squares = []
			string = ""
			inSq = False
			for i in ip:
				if inSq:
					if i == ']':
						squares.append(string)
						string = ""
						inSq = False
						continue
					string += i
				else:
					if i == '[':
						normals.append(string)
						string = ""
						inSq = True
						continue
					string += i
			normals.append(string.strip())
			
			for string in normals:
				if ABBA(string):
					N = True
					break
			for string in squares:
				if ABBA(string):
					S = False
					break
			if N and S:
				result += 1
			
			abas = []
			for string in normals:
				abas.extend(ABA(string))
			if Valid(squares, abas):
				result2 += 1

		print(f"Part 1: {result}")
		print(f"Part 2: {result2}")

def ABBA(string):
	for	i in range(len(string) - 3):
		if string[i] == string[i + 3] and string[i + 1] == string[i + 2] and string[i] != string[i + 1]:
			return True
	return False
def ABA(string):
	abas = []
	for i in range(len(string) - 2):
		if string[i] == string[i + 2] and string[i] != string[i + 1]:
			abas.append(string[i:i + 3])
	return abas
def BAB(string, aba):
	for i in range(len(string) - 2):
		if string[i] is aba[1] and string[i + 2] is aba[1] and string[i + 1] is aba[0]:
			return True
	return False
def Valid(squares, abas):
	for string in squares:
		for aba in abas:
			if BAB(string, aba):
				return True
	return False

main()