"""
Factorial: The factorial of a positive integer n is defined as the product of all positive integers less than or equal to n. The base case is when n is 0 or 1, the factorial is 1. The recursive case is when n is greater than 1, the factorial is n times the factorial of n-1.
"""

def factorial(num):

	if (num == 0):
		return 1
	
	return num*factorial(num-1)

print(factorial(5))
print(factorial(3))
