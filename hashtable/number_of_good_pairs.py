"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
"""
# let's do both approaches: with hash table and "brute "

def number_of_good_pairs(nums):
	count = 0
	for i in range(len(nums)):
		for j in range(i + 1, len(nums)):
			if nums[i] == nums[j]:
				count += 1
	return count

print(number_of_good_pairs([1,1,1,1]))
print(number_of_good_pairs([1, 2, 3]))
print(number_of_good_pairs([1, 2, 3, 1, 1, 3]))

# next approach is to traverse the list once. add all the elements with their corresponding index in the 
# hash table.
def number_of_good_pairs(nums):
	element_to_indices = {}
	for i in range(len(nums)):
		if nums[i] in element_to_indices:
			element_to_indices[nums[i]] += [i]
		else:
			element_to_indices[nums[i]] = [i]
	
	count = 0
	for i in range(len(nums) - 1, 0, -1):
		count += len(element_to_indices[nums[i]]) - 1
		element_to_indices[nums[i]].pop()
	
	return count


print(number_of_good_pairs([1,1,1,1]))
print(number_of_good_pairs([1,2,3]))
print(number_of_good_pairs([1, 2, 3, 1, 1, 3]))
