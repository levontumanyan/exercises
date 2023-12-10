"""
Power: The power of a number x raised to an exponent n is defined as the product of x multiplied by itself n times. The base case is when n is 0, the power is 1. The recursive case is when n is positive, the power is x times the power of x raised to n-1.
"""

def to_power(num, power):

	if power == 0:
		return 1
	
	return num*to_power(num, power - 1)

print(to_power(3,3))