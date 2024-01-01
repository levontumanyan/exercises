"""
The k-beauty of an integer num is defined as the number of substrings of num when it is read as a string that meet the following conditions:

It has a length of k.
It is a divisor of num.
Given integers num and k, return the k-beauty of num.

Note:

Leading zeros are allowed.
0 is not a divisor of any value.
A substring is a contiguous sequence of characters in a string.

Example 1:

Input: num = 240, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "24" from "240": 24 is a divisor of 240.
- "40" from "240": 40 is a divisor of 240.
Therefore, the k-beauty is 2.
Example 2:

Input: num = 430043, k = 2
Output: 2
Explanation: The following are the substrings of num of length k:
- "43" from "430043": 43 is a divisor of 430043.
- "30" from "430043": 30 is not a divisor of 430043.
- "00" from "430043": 0 is not a divisor of 430043.
- "04" from "430043": 4 is not a divisor of 430043.
- "43" from "430043": 43 is a divisor of 430043.
Therefore, the k-beauty is 2.
"""

# simplest approach lets convert the num to a string and use a sliding window approach

def find_k_beauty(num, k):
	str_num = str(num)
	window_start = 0
	window_end = k - 1
	k_beauty = 0

	while window_end < len(str_num):
		try:
			if num % int(str_num[window_start:window_end + 1]) == 0:
				k_beauty += 1
		except:
			pass
		window_start += 1
		window_end += 1
	return k_beauty

# print(find_k_beauty(430043, 2))
# print(find_k_beauty(2, 1))
# print(find_k_beauty(11, 1))
# print(find_k_beauty(37, 1))

# let's try a recursive approach

def find_k_beauty(num, k):
	def find_k_beauty_recursive(num, current_num, k):
		if current_num < pow(10,k):
			return int(num % current_num == 0)

		# new num is num % 10^k
		try:
			if num % (current_num % pow(10,k)) == 0:
				return 1 + find_k_beauty_recursive(num, current_num // 10, k)
		except:
			return find_k_beauty_recursive(num, current_num // 10, k)

		return find_k_beauty_recursive(num, current_num // 10, k)
	return find_k_beauty_recursive(num, num, k)

print(find_k_beauty(430043, 2))
print(find_k_beauty(37, 1))
# 430043 . k = 2
# 430043 % 100 = 43, 430043 % 43 == 0 
# 43004 % 100 = 4, 430043 % 4 == 0 