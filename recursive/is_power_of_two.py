"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

def is_power_of_two(num):
	if (num == 1):
		return True
	
	if (num < 1):
		return False
	
	return is_power_of_two(num / 2)

print(is_power_of_two(1))
print(is_power_of_two(8))
print(is_power_of_two(9))
print(is_power_of_two(16))
print(is_power_of_two(17))

for _ in range(100):
	print(_)
	print(is_power_of_two(_))
