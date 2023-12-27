"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

# First solve the case where we are looking for duplicates next to each other

def contains_consecutive_duplicate(nums):
	window_start = 0
	window_end = 1

	while window_end < len(nums):
		if (nums[window_start] == nums[window_end]):
			return True
		window_start += 1
		window_end += 1
	return False

# print(contains_consecutive_duplicate([2, 3, 4, 5, 6]))
# print(contains_consecutive_duplicate([2, 3, 4, 5, 6, 6]))
# print(contains_consecutive_duplicate([x for x in range(100)]))
# print(contains_consecutive_duplicate([x for x in range(100)] + [99]))

def contains_k_duplicate(k, nums):
	window_start = 0
	window_end = k
	frequencies = {}

	for num in nums[window_start:window_end+1]:
		if num in frequencies:
			return True
		else:
			frequencies[num] = 1

	while window_end < len(nums) - 1:
		frequencies.pop(nums[window_start])
		window_start += 1
		window_end += 1
		if nums[window_end] in frequencies:
			return True
		else:
			frequencies[nums[window_end]] = 1
	return False

print(contains_k_duplicate(1, [2, 3, 4, 5, 6]))
print(contains_k_duplicate(1, [2, 3, 4, 5, 6, 6]))
