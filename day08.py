from os import system, name
from time import sleep
def main():
	with open('input08.txt', 'r') as puzzleInput:
		input = puzzleInput.readlines()
		rows, cols = (6, 50)
		screen = []
		for _ in range(rows):
			newRow = []
			for _ in range(cols):
				newRow.append('.')
			screen.append(newRow)
		
		for inst in input:
			parse = inst.split(' ')
			if parse[0] == "rect":
				parse2 = parse[1].split('x')
				a = int(parse2[0])
				b = int(parse2[1])
				Rect(a, b, screen)
			else:
				b = int(parse[4])
				parse2 = parse[2].split('=')
				a = int(parse2[1])
				if parse[1] == "row":
					RotateRow(a, b, screen)
				if parse[1] == "column":
					RotateColumn(a, b, screen)
			Display(screen)
			sleep(0.03)
			_ = system("cls")

		result = 0
		for	row in screen:
			for px in row:
				if px == '#':
					result += 1
		
		# Takes about 10 seconds
		print(f"Part 1: {result}")
		print(f"Part 2:")
		Display(screen)

def Rect(A, B, screen):
	for y in range(B):
		for x in range(A):
			screen[y][x] = '#'
def RotateRow(A, B, screen):
	temp = screen[A].copy()
	for i in range(len(screen[A])):
		screen[A][i] = temp[(i - B) % len(screen[A])]
def RotateColumn(A, B, screen):
	temp = []
	for i in range(len(screen)):
		temp.append(screen[i][A])
	for i in range(len(screen)):
		screen[i][A] = temp[(i - B) % len(screen)]
def Display(screen):
	for row in screen:
		for	px in row:
			print(px, end='')
		print()
	print()
	
main()