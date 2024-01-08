"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""
import math

def reverse_integer(num):
	if num == 0:
		return 0
	negative = False
	if num < 0:
		num = abs(num)
		negative = True
	digits = int(math.log10(num)) + 1
	reversed_int = 0

	for i in range(digits - 1, -1, -1):
		reversed_int += (num % 10) * pow(10, i)
		num = num // 10
	if reversed_int > pow(2, 31) - 1 or reversed_int < -pow(2, 31):
		return 0
	if negative:
		return -reversed_int
	return reversed_int

print(reverse_integer(1213125))
print(reverse_integer(-1213125))
