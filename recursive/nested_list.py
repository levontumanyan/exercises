"""
Traverse a nested list: Write a recursive function that takes a nested list and returns a flattened list.
"""

def nested_list(items):
	if len(items) == 1:
		return items[0]
	
	return items[0] + nested_list(items[1:])

def flatten_list(nested_list):
    """
    This function takes a nested list as input and returns a flattened list.
    """
    if not nested_list:
        return []
    if isinstance(nested_list[0], list):
        return flatten_list(nested_list[0]) + flatten_list(nested_list[1:])
    return [nested_list[0]] + flatten_list(nested_list[1:])

print(flatten_list([12, 2, [12, 23], 5, 6]))# ---> [12, 2, 12, 23, 5, 6]

