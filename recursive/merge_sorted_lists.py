"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""
result = []

def merge_sorted_lists(list1, list2):
	if len(list1) == 0:
		result.append(list2[0])
		print(result)
		return
	
	if len(list2) == 0:
		result.append(list1[0])
		print(result)
		return

	if (list1[0] < list2[0]):
		result.append(list1[0])
		list1 = list1[1:]
	else:
		result.append(list2[0])
		list2 = list2[1:]
	
	merge_sorted_lists(list1, list2)


def merge_sorted_lists(list1, list2):
	if len(list1) == 0:
		return list2[0]
	
	if len(list2) == 0:
		return [list1[0]]

	if (list1[0] < list2[0]):
		return [list1[0]] + merge_sorted_lists(list1[1:], list2)
	else:
		return [list2[0]] + merge_sorted_lists(list1, list2[1:])
	
	merge_sorted_lists(list1, list2)

print(merge_sorted_lists([1, 2, 5, 10], [2, 4, 6, 7]))