# PART 1
# The elf in the position, stealing a packet when the sum of elves left is a power of 2 wins.
input = 3001330
# Finds the largest power of 2 (in input) and subtracts it.
# The resulting number is the number of elves who will be removed before the winners first turn.
binStr = format(input, "b")
result = input - pow(2, len(binStr) - 1)
# (It starts at position 1. Shifts 2 positions per elf removed.)
result = 1 + result * 2
print(f"Part 1: {result}")

# PART 2
# The elf at the position before the one who has the turn when there are some power of 3 elves left wins.
# For example elf 3 wins in a ring of 3 elves (starting at 1). Elf 1 in a ring of 4.
# So the number of steps in the ring before getting to the winner is: 
# startNum (input) - greatest power of 3(less than input) - 1.
tri = 3
while (tri * 3) < input:
	tri *= 3
steps = input - tri - 1
result = 1 + steps 
# If the the steps needed to get to the winner position is past the halfwaypoint of the circle it gets
# more complicated (because of passing by removed positions).
# But I didn't need to deal with that for my input :).
if steps >= tri:
	result = "something else"
print(f"Part 2: {result}")