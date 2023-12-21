"""
Sure, here's a simple sliding window problem for you:

**Problem: Maximum Sum Subarray of Size K**

Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

**Example:**

Input: [2, 1, 5, 1, 3, 2], k=3 
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

This problem is a classic example of the sliding window pattern and is quite straightforward. The window size is fixed, and you need to find the maximum sum within this window as it slides through the array. Happy coding! 😊

"""

# max sum of size 2 subarrays
def maximum_2sum_subarray(nums):
	current_max = 0
	window_start = 0
	window_end = 1

	while window_end < len(nums):
		current_max = max(current_max, sum(nums[window_start:window_end+1]))
		window_start += 1
		window_end += 1

	return current_max

print(maximum_2sum_subarray())

def maximum_sum_subarray(k, nums):
	pass