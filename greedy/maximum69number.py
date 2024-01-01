import math
"""
You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.
"""

def maximum69number(num):
	digits = []
	result = 0
	while num > 0:
		digits.append(num % 10)
		num = num // 10

	for i in range(len(digits) - 1, - 1, -1):
		if (digits[i] == 6):
			digits[i] = 9
			break
	
	for i in range(len(digits) - 1, - 1, -1):
		result += digits[i] * pow(10, i)
	
	return result

def maximum69number(num):
	num_of_digits = int(math.log10(num) + 1)

	for i in range(num_of_digits, 0, -1):
		# Extract the left-most digit
		digit = num // 10**(i - 1)

print(maximum69number(699966))