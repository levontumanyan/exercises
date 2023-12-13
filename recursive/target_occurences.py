"""
Count Occurrences:
Create a recursive function to count the occurrences of a specific element in a list.
"""

def target_occurrences(numbers, target):
	if len(numbers) == 0:
		return 0
	
	if (numbers[0] == target):
		return 1 + target_occurrences(numbers[1:], target)
	else:
		return target_occurrences(numbers[1:], target)



print(target_occurrences([1, 2, 3, 2, 5, 1, 2, 9, 2], 2))