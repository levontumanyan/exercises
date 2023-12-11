def sum_of_odd_numbers(nums):

	if len(nums) == 1:
		if (nums[0] % 2) == 0:
			return 0
		else:
			return nums[0]
		
	return sum_of_odd_numbers([nums[0]]) + sum_of_odd_numbers(nums[1:])

def sum_of_odd_numbers(nums):
	if not nums:
		return 0
	if (nums[0] % 2 != 0):
		return nums[0] + sum_of_odd_numbers(nums[1:])
	return sum_of_odd_numbers(nums[1:])


print(sum_of_odd_numbers([ 2, 4, 2, 3, 5, 10]))
print(sum_of_odd_numbers([ 2, 4, 2, 3, 5, 10, 11]))
print(sum_of_odd_numbers([ 2, 4, 2, 3, 5, 10]))
