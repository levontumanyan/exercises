"""
You are given an array of n integers. You want to modify the array so that it is increasing, i.e., every element is at least as large as the previous element.
On each move, you may increase the value of any element by one. What is the minimum number of moves required?
Input
The first input line contains an integer n: the size of the array.
Then, the second line contains n integers x_1,x_2,\ldots,x_n: the contents of the array.
Output
Print the minimum number of moves.
Constraints

1 \le n \le 2 \cdot 10^5
1 \le x_i \le 10^9

Example
Input:
5
3 2 5 1 7 =

3 3 5 2 7
3 4 5 3 7
3 4 5 4 7
3 4 5 5 7
3 4 5 6 7

Output:
5

5 2 4

6 2 2 8 9
6 7 8 9 10

6 12 2 8 9
6 12 13 14 15

12 3 1 14 15
12 13 14 15 16

12 3 14 15 1
12 13 14 


"""
# the below solves the question for a strictly increasing array
def strictly_increasing_array(nums):
	increasing_nums = [0] * (len(nums))
	increasing_nums[0] = nums[0]

	for i in range(1, len(nums)):
		increasing_nums[i] = max(nums[i], increasing_nums[i-1] + 1)
	
	return max([ x-y for x,y in zip(increasing_nums, nums)])

# print(increasing_array([12, 3, 1, 14, 15]))
# print(increasing_array([5, 2, 4]))
# print(increasing_array([6, 2, 2, 8, 9]))
# print(increasing_array([3, 2, 5, 1, 7]))

def increasing_array(nums):
	maximum = nums[0]
	increasing_nums = [0] * (len(nums))
	increasing_nums[0] = maximum

	for i in range(1, len(nums)):
		if nums[i] < maximum:
			increasing_nums[i] = maximum
		else:
			maximum = nums[i]
			increasing_nums[i] = maximum
	
	return increasing_nums
	#return max([ x-y for x,y in zip(increasing_nums, nums)])

# print(increasing_array([100, 1, 101, 1]))
# print(increasing_array([1, 1, 1, 1]))
# print(increasing_array([3, 2, 5, 1, 7]))

def increasing_array(length, nums):
	length = int(length)
	nums = list(map(int, nums.split(" ")))

	moves = 0
	for i in range(1, length):
		if nums[i] <= nums[i-1]:
			moves += nums[i-1] - nums[i]
			nums[i] = nums[i-1]
	return moves

length = input()
nums = input()

print(increasing_array(length, nums))



""" Solution specifically for cses.fi format"""

# def increasing_array(length, nums):
# 	nums = list(map(int, nums.split(" ")))
# 	maximum = nums[0]
# 	increasing_nums = [0] * (len(nums))
# 	increasing_nums[0] = maximum

# 	for i in range(1, len(nums)):
# 		if nums[i] < maximum:
# 			increasing_nums[i] = maximum
# 		else:
# 			maximum = nums[i]
# 			increasing_nums[i] = maximum
	
	
# 	return max([ x-y for x,y in zip(increasing_nums, nums)])

# length = input()
# nums = input()

# print(increasing_array(length, nums))
