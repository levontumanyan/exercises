# [1, 2, 2, 3, 5, 6, 7, 12, 23, 42, 55] - 11 elements
# left 0, right 10 - mid 5

# [7, 12, 23, 42, 55] - left index: 6 right 10

def binary_search(nums, target):
	left, right = 0, len(nums) - 1
	
	while left <= right:
		mid = left + (right - left) // 2
		if nums[mid] == target:
			return mid
		elif nums[mid] < target:
			left = mid + 1
		else:
			right = mid - 1
	return -1

print(binary_search([1, 2, 2, 3, 5, 6, 7, 12, 23, 42, 55], 42))
print(binary_search([-1, 0, 3, 5, 9, 12], 2))
print(binary_search([5], 5))