
def sum_of_odd_sub_even(nums):

	if not nums:
		return 0
	
	if (nums[0] %2 == 0 ):
		return sum_of_odd_sub_even(nums[1:]) - nums[0]
	else:
		return nums[0] + sum_of_odd_sub_even(nums[1:])
	
print(sum_of_odd_sub_even([1, 4, 5, 12]))
print(sum_of_odd_sub_even([ 2, 4, 2, 3, 5, 10, 11]))
print(sum_of_odd_sub_even([ 2, 4, 2, 3, 5, 10]))
