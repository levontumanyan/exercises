"""
Write a program in C to print even or odd numbers in a given range using recursion. >
Test Data : 
Input the range to print starting from 1 : 10 
Expected Output :

All even numbers from 1 to 10 are : 2  4  6  8  10                              
All odd numbers from 1 to 10 are : 1  3  5  7  9
"""

def odd_integers(numbers):
	if (len(numbers) == 0):
		return []
	
	if (numbers[0] % 2 == 1):
		return [numbers[0]] + odd_integers(numbers[1:])
	else:
		return odd_integers(numbers[1:])
	
print(odd_integers([1, 2, 4, 2, 3, 4, 5]))