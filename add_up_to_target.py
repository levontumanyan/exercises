"""
Given an array of integers and a target, return indices of the two numbers such that the sum of those two adds up to the target 
"""
# Big(O) = n^2
def add_up_to_target_v1(nums, target):
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			if (nums[i] + nums[j] == target):
				return i,j
			
print(add_up_to_target_v1([4, 5, 22, 2, 4, 2, 3], 6))

# next solution is to sort the array then to loop once
# Please note that the returned indices are based on the sorted array, not the original array. If you need the indices for the original array, you would need a different approach. Also, this solution does not handle the case where the array has duplicate numbers. If your array can have duplicates and you need to find all pairs that sum to the target, you would need a different solution.
def add_up_to_target_v2(nums, target):
	nums = sorted((num, i) for i, num in enumerate(nums))

	left_pointer = 0
	right_pointer = len(nums) - 1

	while left_pointer < right_pointer:
		sum = nums[left_pointer][0] + nums[right_pointer][0]

		if sum < target:
			left_pointer += 1
		elif sum > target:
			right_pointer -= 1
		else:
			return nums[left_pointer][1], nums[right_pointer][1] 

print(add_up_to_target_v2([4, 5, 22, 2, 4, 2, 3], 6))
print(add_up_to_target_v2([4, 5, 22, 0, 4, 2, 3], 22))

# next solution is to use hash_maps/dictionaries somehow this is O(n)

def add_up_to_target_v3(nums, target):

	nums_dict = {}

	for i, num in enumerate(nums):

		complement = target - num

		if (complement in nums_dict):
			return nums_dict[complement], i
		else:
			nums_dict[num] = i
	
	return False

print(add_up_to_target_v3([4, 5, 22, 2, 4, 2, 3], 6))
print(add_up_to_target_v3([4, 5, 22, 0, 4, 2, 3], 22))
