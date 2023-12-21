"""
Find maximum length sequence of continuous ones (Using Sliding Window)

For example, consider array [ 0, 0, 1, 0, 1, 1, 1, 0, 1, 1 ]. The answer is 3.

"""

def continuous_ones(nums):
	i = 0
	j = 1
	overall_max = 0
	current_max = 0

	while j < len(nums):
		if nums[i] == 1 and nums[j] == 1:
			current_max += 2
			j = j + 1
			i = i + 1
			continue
		elif nums[j] == 0:
			overall_max = max(current_max, overall_max)
			current_max = 0
			i = j + 1
			j = j + 2
			continue
		elif nums[i] == 0:
			overall_max = max(current_max, overall_max)
			current_max = 0
			i = i + 1
			j = j + 1
			continue
	return overall_max


def continuous_ones(nums):
	max_len = 0
	window_start = 0

	for window_end in range(len(nums)):
		if nums[window_end] == 0:
			max_len = max(max_len, window_end - window_start)
			window_start = window_end + 1

	return max(max_len, len(nums) - window_start)
		
	
#print(continuous_ones([0, 1, 1, 0, 0, 1, 1, 1]))
print(continuous_ones([1, 0, 1, 1, 0, 0, 1, 1, 1]))

