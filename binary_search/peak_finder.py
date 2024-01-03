"""
Problem: Peak Finding

Given an array of integers, a peak is an element which is not smaller than its neighbors. More formally, for any given index i in the array arr, arr[i] is a peak if and only if arr[i] >= arr[i-1] and arr[i] >= arr[i+1]. For the edge cases, we only consider one neighbor. For example, for i = 0, arr[i] is a peak if arr[i] >= arr[i+1].

The task is to find any peak element in the array, if it exists.

Since the problem includes >= and <=, there will always be a solution.

Example:

Input: [1, 3, 7, 1, 2, 6, 0] Output: 7 (Index 2 is a peak)

Input: [6, 7, 4, 3, 2, 1, 4, 5] Output: 7 (Index 1 is a peak), 5 (Index 7 is a peak)

Note: The output can be any peak element in the array, and the array may contain multiple peaks.
"""

def peak_finder(nums, i=0):
	if len(nums) == 1:
		return i
	if len(nums) == 2:
		if nums[0] > nums[1]:
			return i
		else:
			return i + 1
	
	if nums[len(nums) // 2] > nums[len(nums) // 2 + 1] and nums[len(nums) // 2] > nums[len(nums) // 2 - 1]:
		return i + (len(nums) // 2)
	if nums[len(nums) // 2] < nums[len(nums) // 2 + 1]:
		return peak_finder(nums[(len(nums) // 2 + 1):], i + (len(nums) // 2 + 1) )
	else:
		return peak_finder(nums[:(len(nums) // 2)], i)

print(peak_finder([6, 7, 4, 3, 5, 2, 1, 4, 5]))
print(peak_finder([9, 2, 3, 4, 5, 6, 7]))
print(peak_finder([9, 2, 3, 22, 5, 6, 7]))
print(peak_finder([2, 1]))
print(peak_finder([1,2,3]))
print(peak_finder([1,3,2,1]))
print(peak_finder([1,2,3,4,5,6,1]))

def peak_finder(nums):
	i = 0
	index=0
	
	while i < len(nums) // 2:
		if len(nums) == 2:
			if (nums[0] > nums[1]):
				return index
			else:
				return 1 + index
		if nums[len(nums) // 2] > nums[len(nums) // 2 + 1] and nums[len(nums) // 2] > nums[len(nums) // 2 - 1]:
			index += len(nums) // 2
			return index
		elif nums[len(nums) // 2] < nums[len(nums) // 2 + 1]:
			index += (len(nums) // 2 + 1)
			nums = nums[(len(nums) // 2 + 1):]
		else:
			nums = nums[:(len(nums) // 2)]
	return index

print(peak_finder([6, 7, 4, 3, 5, 2, 1, 4, 5]))
print(peak_finder([9, 2, 3, 4, 5, 6, 7]))
print(peak_finder([9, 2, 3, 22, 5, 6, 7]))
print(peak_finder([2, 1]))
print(peak_finder([1,2,3]))
print(peak_finder([1,3,2,1]))
print(peak_finder([1,2,3,4,5,6,1]))




"""
[6, 7, 4, 3, 2, 1, 4, 5]
choose middle element - 2, 1 is less than three pick right side. 
[ 1, 4, 5 ] - pick middle element - 4, 1 is less than 4 pick left side. 1



[1, 2, 4, 5, 6, 7, 8] --- sort of worst case for logn
choose 5, 6 is greater than 5 so we choose the right side. 
[6, 7, 8] - 7 is less than 8, so we choose right side. 8 is the element
"""