"""
Subset Sum:
Write a recursive function to check if there is a subset of a list that adds up to a given target sum.
"""

def subset_sum(numbers, target):
	
	if sum(numbers) == target:
		return numbers
	
	



print(subset_sum([2, 3, 4, 1], 4))