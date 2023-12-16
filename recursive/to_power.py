"""
Power: The power of a number x raised to an exponent n is defined as the product of x multiplied by itself n times. The base case is when n is 0, the power is 1. The recursive case is when n is positive, the power is x times the power of x raised to n-1.
"""
# below works only for positive
def to_power(num, power):

	if power == 0:
		return 1
	
	return num*to_power(num, power - 1)

#print(to_power(3,-3))


"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2^-2 = 1/22 = 1/4 = 0.25
"""

def to_power(num, power):

	if num == 1:
		return 1

	powers = { 100 : None, 1000: None, 10000: None }
	#powers = []
	if power == 0:
		return 1

	if power < 0:
		return (1/to_power(num, -power))

	if power > 10000:
		if not powers[10000]:
			powers[10000] = powers[100] * powers[100]
		else:
			return powers[10000] * to_power(num, power-10000)

	if power > 1000:
		if not powers[1000]:
			powers[1000] = powers[100] * powers[10]
		else:
			return powers[1000] * to_power(num, power-1000)

	if power > 100:
		if not powers[100]:
			powers[100]=to_power(num, 100)
		else:
			return powers[100] * to_power(num, power-100)
	
	return num*to_power(num, power-1)

#print(to_power(3,-3))
#print(to_power(2,-2))
#print(to_power(0.00001,111))
#print(to_power(2,1110))

def to_power(x, n):
    # Base case: n is 0, x^0 is 1
    if n == 0:
        return 1
    # Recursive case: n is negative
    elif n < 0:
        return 1 / pow(x, -n)
    # Recursive case: n is even
    elif n % 2 == 0:
        half = pow(x, n // 2)
        return half * half
    # Recursive case: n is odd
    else:
        half = pow(x, n // 2)
        return half * half * x

print(to_power(2,2147))
