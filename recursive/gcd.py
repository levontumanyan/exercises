"""
GCD: The greatest common divisor (GCD) of two positive integers a and b is the largest positive integer that divides both a and b without leaving a remainder. The base case is when b is 0, the GCD is a. The recursive case is when b is not 0, the GCD is the same as the GCD of b and the remainder of a divided by b.
"""

def gcd(num1, num2):

	if (num2 == 0):
		return num1
	
	return gcd(num2, num1 % num2)


print(gcd(6,2))

print(gcd(12,8))

print(gcd(8,12))
