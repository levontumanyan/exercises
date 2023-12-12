"""
Binary Search:
Write a recursive function to perform a binary search on a sorted list and return the index of a target element.
"""

def binary_search(numbers, target):
	
	if len(numbers) == 1 and numbers[0] == target:
		return True
	elif len(numbers) == 1 and numbers[0] != target:
		return False
	
	if len(numbers) == 0:
		return False

	
	midpoint = len(numbers) // 2
	
	if (target < numbers[midpoint]):
		return binary_search(numbers[:midpoint], target)
	elif (target > numbers[midpoint]):
		return binary_search(numbers[midpoint+1:], target)
	else:
		return True

# the solution above does slicing, which is not needed.
# instead we want to pass the function a new list in place


def binary_search(numbers, target, low=0, high=None):

	if not high:
		high = len(numbers) - 1

	midpoint = (high + low) // 2

	if low <= high:

		if (target < numbers[midpoint]):
			return binary_search(numbers, target, low, midpoint - 1)
		elif (target > numbers[midpoint]):
			return binary_search(numbers, target, midpoint + 1, high)
		else:
			return midpoint
	else:
		return -1


print(binary_search([1, 4, 6, 8, 12, 232, 565, 2134], 565))
print(binary_search(range(1000), 565))
print(binary_search([0, 1, 2, 3, 4, 5], 6))

