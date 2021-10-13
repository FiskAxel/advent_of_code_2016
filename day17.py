import hashlib
input = "awrkjxxr"
def main():
	superLong = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	result = shortestPath("", 0, 0, superLong)
	print(f"Part 1: {result}")
	result = LongestPath("", 0, 0, result)
	print(f"Part 2: {len(result)}")

def shortestPath(path, x, y, s):
	if len(path) > len(s):
		return None
	if x == 3 and y == 3:
		return path

	key = input + path
	hash = hashlib.md5(key.encode()).hexdigest()[0: 4]
	if x < 3 and isbcdef(hash[3]):
		nPath = path + "R"
		p = shortestPath(nPath, x + 1, y, s)
		s = shortest(s, p)
	if y < 3 and isbcdef(hash[1]):
		nPath = path + "D"
		p = shortestPath(nPath, x, y + 1, s)
		s = shortest(s, p)
	if x > 0 and isbcdef(hash[2]):
		nPath = path + "L"
		p = shortestPath(nPath, x - 1, y, s)
		s = shortest(s, p)
	if y > 0 and isbcdef(hash[0]):
		nPath = path + "U"
		p = shortestPath(nPath, x, y - 1, s)
		s = shortest(s, p)
	return s
def shortest(a, b):		
	if b == None or len(a) < len(b):
		return a
	return b
def isbcdef(c):
	if c == 'b' or c == 'c' or c == 'd' or c == 'e' or c == 'f':
		return True

def LongestPath(path, x, y, l):
	if x == 3 and y == 3:
		return path

	key = input + path
	hash = hashlib.md5(key.encode()).hexdigest()[0: 4]
	if x < 3 and isbcdef(hash[3]):
		nPath = path + "R"
		p = LongestPath(nPath, x + 1, y, l)
		l = longest(l, p)
	if y < 3 and isbcdef(hash[1]):
		nPath = path + "D"
		p = LongestPath(nPath, x, y + 1, l)
		l = longest(l, p)
	if x > 0 and isbcdef(hash[2]):
		nPath = path + "L"
		p = LongestPath(nPath, x - 1, y, l)
		l = longest(l, p)
	if y > 0 and isbcdef(hash[0]):
		nPath = path + "U"
		p = LongestPath(nPath, x, y - 1, l)
		l = longest(l, p)
	return l
def longest(a, b):
	if len(a) > len(b):
		return a
	return b

main()