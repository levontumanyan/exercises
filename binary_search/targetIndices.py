"""
You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order. If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.
Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.
Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.
"""

def targetIndices(nums, target):
	nums = sorted(nums)
	i = 0
	index = len(nums) // 2
	result = []

	while i < (len(nums) // 2 + 1):

		if nums[index] == target:
			j = 1
			k = 1
			while index - k > 0:
				if nums[index - k] == target:
					result.append(index - k)
					k += 1
				else:
					break
			result.append(index)
			while j + index < len(nums):
				if nums[j + index] == target:
					result.append(j + index)
					j += 1
				else:
					break
			return result
		elif nums[index] < target:
			index += (len(nums) - index) // 2
		else:
			index -= (len(nums) - index) // 2
		i += 1

	return result

def targetIndices(nums, target):

	nums = sorted(nums)
	left, right = 0, len(nums) - 1
	result = []

	while left <= right:
		mid = left + (right - left) // 2
		if nums[mid] == target:
			result.append(mid)
			i = mid - 1
			while i >= 0 and nums[i] == target:
				result.append(i)
				i -= 1
			i = mid + 1
			while i < len(nums) and nums[i] == target:
				result.append(i)
				i += 1
			return sorted(result)
		elif nums[mid] < target:
			left = mid + 1
		else:
			right = mid - 1

	return result

print(targetIndices([1, 2, 5, 2, 3], 5))
print(targetIndices([1, 2, 5, 2, 8, 3, 4, 5, 2], 8))
print(targetIndices([1, 2, 5, 2, 8, 3, 4, 5, 2], 5))
print(targetIndices([1,2,5,2,3], 2))
print(targetIndices([2, 1], 1))
