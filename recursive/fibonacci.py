"""
Fibonacci: The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1. The base case is when n is 0 or 1, the Fibonacci number is n. The recursive case is when n is greater than 1, the Fibonacci number is the sum of the Fibonacci numbers of n-1 and n-2.
"""

def fibonacci(num):

	if (num == 0 or num == 1):
		return 1
	
	return fibonacci(num-1) + fibonacci(num-2)

print([fibonacci(n) for n in range(9)])
