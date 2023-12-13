"""
Write a program to check if a number is a prime number or not using recursion. >
Test Data : 
Input any positive number : 7 
Expected Output :

The number 7 is a prime number.
"""

def prime_number(num, divide_by=2):
	if (divide_by == num or num == 1):
		return True
	
	if (num % divide_by == 0):
		return False

	return prime_number(num, divide_by+1)

print(prime_number(7))
print(prime_number(2))
print(prime_number(9))
print(prime_number(16))
print(prime_number(5))
print(prime_number(1))
