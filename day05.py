import hashlib
with open('input05.txt', 'r') as puzzleInput:
	input = puzzleInput.readlines()
	index = 0
	password = ""
	password2 = ["", "", "", "", "", "", "", ""]
	while True:
		hashthis = input[0] + str(index)
		hash = hashlib.md5(hashthis.encode()).hexdigest()
		if hash[:5] == "00000":
			if len(password) < 8:
				password += hash[5]
			if hash[5] in ['0', '1', '2', '3', '4', '5', '6', '7']:
				if password2[int(hash[5])] == "":
					password2[int(hash[5])] = hash[6]
			if len(''.join(password2)) == 8:
				break
		index += 1
	# Takes about one and a half minute to run 
	print(f"Part 1: {password}")
	print(f"Part 2: {''.join(password2)}")