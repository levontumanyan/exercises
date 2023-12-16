"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

def power_of_two(num):
	if (num == 1):
		return True
	
	if (num < 1):
		return False
	
	return power_of_two(num / 2)
print(power_of_two(1))
print(power_of_two(8))
print(power_of_two(9))
print(power_of_two(16))
print(power_of_two(17))

for _ in range(100):
	print(_)
	print(power_of_two(_))
