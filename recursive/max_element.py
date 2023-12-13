"""
Given an array, write functions to find the minimum and maximum elements in it. 

The most simplest way to find min and max value of an element is to use inbuilt function sort() in java. So, that value at 0th position will min and value at nth position will be max.
"""

def max_element(numbers, current_max=0):

	if (len(numbers) == 0 ):
		return current_max
	
	if (numbers[0] > current_max):
		return max_element(numbers[1:], numbers[0])
	else:
		return max_element(numbers[1:], current_max)
	
print(max_element([1, 2, 5, 7, 2, 3, 1, 0]))
print(max_element([1, 2, 5, 7, 2, 3, 1, 0, 122]))
print(max_element([]))
