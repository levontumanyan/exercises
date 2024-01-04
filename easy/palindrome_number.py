"""
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
import math

def palindrome_number(num):
	# reverse num
	num = abs(num)
	num_initial = num
	reverse_num = 0
	num_of_digits = int(math.log10(num)) + 1
	i = num_of_digits - 1

	while num != 0:
		current_digit = num % 10
		reverse_num += current_digit * pow(10, i)
		num = num // 10
		i -= 1
	return reverse_num == num_initial

print(palindrome_number(12121312431))
print(palindrome_number(121))
print(palindrome_number(151))
print(palindrome_number(-151))

