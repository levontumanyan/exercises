"""
Count down to zero: Write a recursive function that takes a positive integer n and prints the numbers from n to 0.
"""

def count_down(n):

	if n == 0:
		return 0
	
	return f'{n}' + f'{count_down(n-1)}'

def count_down(n):

	if n == 0:
		return 0
	
	return f'{n}' + f'{count_down(n-1)}'

print(count_down(6))
print(count_down(12))
print(count_down(14))
