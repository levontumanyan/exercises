"""
Problem: Minimum Window Substring

Given two strings, string1 and string2, find the minimum window in string1 which will contain all the characters in string2 in complexity O(n).

Example:

Input: string1 = “ADOBECODEBANC”, string2 = “ABC” Output: “BANC” Explanation: The minimum window in string1 which contains all the characters in string2 is “BANC”.

This problem is a bit more challenging than the previous one, but it’s a great way to practice the sliding window technique. You need to find the smallest substring in string1 that contains all the characters of string2. Remember, the characters don’t have to be in the same order as in string2. Happy coding!
"""

def maximum_window_substring(string1, string2):
	string2_list = [ letter for letter in string2]

	min_window_size = float('inf')
	window_start = 0
	window_end = 1

	while window_end < len(string1):
		if (string1[window_start] not in string2):
			window_start += 1
			window_end += 1
		else:
			



	return string2_list


print(maximum_window_substring("ADOBECODEBANC", "ABC"))