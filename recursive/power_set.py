"""
return the power set of a list
"""

def power_set(elements):

	if len(elements) == 0:
		return []
	
	return elements, [power_set(elements[1:])]



def power_set(lst):
    # base case: an empty list has one subset, the empty set
    if len(lst) == 0:
        return [[]]

    # recursive case:
    # for each subset in the power set of the list without the first element...
    subsets = power_set(lst[1:])
    # ...add that subset both with and without the first element of the list
    return subsets + [[lst[0]] + subset for subset in subsets]

print(power_set([1, 2, 3]))# --> [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
