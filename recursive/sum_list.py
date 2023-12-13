"""
Sum of List:
Write a recursive function to find the sum of all elements in a list.
"""


def sum_list(numbers):

	if len(numbers) == 1:
		return numbers[0]
	
	return numbers[0] + sum_list(numbers[1:])


print(sum_list([1, 4, 4]))