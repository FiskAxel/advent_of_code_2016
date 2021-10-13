import hashlib
def main():
	salt = "zpqevtbw"
	i, index = 0, 0
	while (i < 64):
		toHash = salt + str(index)
		hash = hashlib.md5(toHash.encode()).hexdigest()
		triple = getTriple(hash)
		if len(triple) == 3:
			if checkFiveple(triple, salt, index + 1):
				i += 1
		index += 1
	result = index - 1
	# PART 1 Runs in about a minute
	print(f"Part 1: {result}")

	#	PART 2 (Takes another 3 minutes)

	hashes2016 = []
	for l in range(1000):
		toHash = salt + str(l)
		hash = hashlib.md5(toHash.encode()).hexdigest()
		for _ in range(2016):
			hash = hashlib.md5(hash.encode()).hexdigest()
		hashes2016.append(hash)

	i, index = 0, 0
	while (i < 64):
		toHash = salt + str(index + 1000)
		hash = hashlib.md5(toHash.encode()).hexdigest()
		for _ in range(2016):
			hash = hashlib.md5(hash.encode()).hexdigest()
		hashes2016.append(hash)
		triple = getTriple(hashes2016[0])
		if len(triple) == 3:
			if checkFiveplePart2(triple, hashes2016):
				i += 1
		index += 1
		hashes2016.pop(0)
	result = index - 1
	print(f"Part 2: {result}")

def getTriple(input):
	prev = ""
	streak = 0
	for i in input:
		if i == prev:
			streak += 1
		else:
			streak = 1
			prev = i
			continue
		if streak == 3:
			return prev + prev + prev
	return ""
def checkFiveple(triple, salt, starti):
	c = triple[0]
	for i in range(starti, starti + 1000):
		toHash = salt + str(i)
		hash = hashlib.md5(toHash.encode()).hexdigest()
		streak = 0
		for j in hash:
			if j == c:
				streak += 1
			else:
				streak = 0
				continue
			if streak == 5:
				return True
	return False
def checkFiveplePart2(triple, hashes):
	c = triple[0]
	for i in hashes:
		if i == hashes[0]:
			continue
		streak = 0
		for j in i:
			if j == c:
				streak += 1
			else:
				streak = 0
				continue
			if streak == 5:
				return True
	return False

main()