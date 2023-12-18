"""
You are given all numbers between 1,2,\ldots,n except one. Your task is to find the missing number.
Input
The first input line contains an integer n.
The second line contains n-1 numbers. Each number is distinct and between 1 and n (inclusive).
Output
Print the missing number.
Constraints

2 \le n \le 2 \cdot 10^5

Example
Input:
5
2 3 1 5

Output:
4
"""

def missing_number(length, nums):
	nums = str(nums)
	sorted_nums = [int(i) for i in sorted(nums.split(" "))]
	correct_nums = [i for i in range(1, length+1, 1)]

	return sum(correct_nums) - sum(sorted_nums)

def missing_number(length, nums):
	correct_sum = sum([i for i in range(1, length+1)])
	wrong_sum = sum([int(i) for i in nums.split(" ")])
	return correct_sum - wrong_sum

def missing_number(length, nums):
	nums = [int(i) for i in nums.split(" ")]
	for i in range(len(nums) - 1):
		if (abs(nums[i] - nums[i+1]) != 1):
			return abs(nums[i] - nums[i+1])

# length = int(input())
# nums = input()

print(missing_number(4, "2 3 1"))
