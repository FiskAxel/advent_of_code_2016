def main():
	input = 1350
	x, y = 1, 1 # starting point
	dx, dy = 31, 39 # destination
	path = [[1,1]]
	result = findPath(x, y, dx, dy, input, path, 0, 100)
	# PART 1 runs in about 5 seconds
	print(f"Part 1: {result}")

	# PART 2 takes a minute to run
	
	result = 0
	for dx in range(50):
		for dy in range(50):
			if isOpen(dx, dy, input):
				if findPath(x, y, dx, dy, input, path, 0, 51) <= 50:
					result += 1
	print(f"Part 2: {result}")

def findPath(x, y, dx, dy, fn, path, len, sLen):
	if len > sLen:
		return 100
	if x == dx and y == dy:
		return len
	
	nx = x + 1
	if isOpen(nx, y, fn) and [nx, y] not in path:
		nPath = []
		for c in path:
			nPath.append(c)
		nPath.append([nx, y])
		nLen = findPath(nx, y, dx, dy, fn, nPath, len + 1, sLen)
		if nLen < sLen:
			sLen = nLen

	nx = x - 1
	if isOpen(nx, y, fn) and [nx, y] not in path:
		nPath = []
		for c in path:
			nPath.append(c)
		nPath.append([nx, y])
		nLen = findPath(nx, y, dx, dy, fn, nPath, len + 1, sLen)
		if nLen < sLen:
			sLen = nLen

	ny = y + 1
	if isOpen(x, ny, fn) and [x, ny] not in path:
		nPath = []
		for c in path:
			nPath.append(c)
		nPath.append([x, ny])
		nLen = findPath(x, ny, dx, dy, fn, nPath, len + 1, sLen)
		if nLen < sLen:
			sLen = nLen

	ny = y - 1
	if isOpen(x, ny, fn) and [x, ny] not in path:
		nPath = []
		for c in path:
			nPath.append(c)
		nPath.append([x, ny])
		nLen = findPath(x, ny, dx, dy, fn, nPath, len + 1, sLen)
		if nLen < sLen:
			sLen = nLen
	
	return sLen

def isOpen(x, y, favNum):
	if x < 0 or y < 0:
		return False
	num = x*x + 3*x + 2*x*y + y + y*y + favNum
	bin = format(num, 'b')
	totOne = 0
	for c in bin:
		if c == '1':
			totOne += 1
	if totOne % 2 == 0:
		return True
	return False

main()