"""
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n. 

Example 1:

Input: n = 13
Output: 6
Example 2:

Input: n = 0
Output: 0
"""

def numberof_digits_one(num):
	result = 0
	n = num
	while n > 0:
		if n % 10 == 9:
			n -= 8
			continue
		result += numberof_digits_one_helper(n)
		n -= 1
		
	return result

def numberof_digits_one_helper(num):
	count = 0

	while num > 0:
		if num % 10 == 1:
			count += 1
		num = num // 10
	return count

#print(numberof_digits_one_helper(13))
#print(numberof_digits_one_helper(131))

print(numberof_digits_one(824883294))

# recursive
def numberof_digits_one(num):
	if num == 0:
		return 0
	if num <= 10:
		return 1
	
	return (1 == numberof_digits_one(num % 10))