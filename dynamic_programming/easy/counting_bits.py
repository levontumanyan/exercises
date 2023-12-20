"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""
# below is probably cheating

def counting_bits(num):
	binary_n = bin(num)	
	count = 0
	for i in range(2, len(binary_n)):
		if (binary_n[i] == "1"):
			count += 1
	return count

def counting_bits_upto(num):
	ans = []
	for i in range(num + 1):
		ans.append(counting_bits(i))
	return ans

#print(counting_bits_upto(2))

######################
"""0 - 0 - 0
1 - 1 - 1
2 - 10 - 1
3 - 11 - 2
4 - 100 - 1
5 - 101 - 2
6 - 110 - 2
7 - 111 - 3
8 - 1000 - 1
9 - 1001 - 2
10 - 1010 - 2
11 - 1011 - 3
12 - 1100 - 2
13 - 1101 - 3
14 - 1110 - 3 = 1 + bits(110)
15 - 1111 - 4 = 1 + bits(111) = 1 + 1 + bits(11) = 1 + 1 + 1 + bits(1)
"""
memo = {}

def counting_bits(num):
	if num == 0:
		return 0
	
	if num in memo:
		return memo[num]
	else:
		return (num & 1) + counting_bits(num >> 1)

# 8 - 1000 & 1 + counting_bits(100) = 1000 & 1 + 100 & 1 + counting_bits(10) = 1000 & 1 + 100 & 1 + 10 & 1 + counting_bits(1) = 1000 & 1 + 100 & 1 + 10 & 1 + 1 & 0 + counting_bits(0) = 1000 & 1 + 100 & 1 + 10 & 1 + 1 & 1 + 0

# for _ in range(1000):
# 	print(f"{_}: {bin(_)}: {counting_bits(_)}")

def counting_bits_upto(num):
	for i in range(num+1):
		memo[i] = counting_bits(i)
	return list(memo.values())

#print(counting_bits_upto(4))



####

class Solution:
	memo = {}

	def counting_bits(self, num):
		if num == 0:
			return 0
		
		if num in Solution.memo:
			return Solution.memo[num]
		else:
			return (num & 1) + self.counting_bits(num >> 1)

	def countBits(self, n: int):
		for i in range(n + 1):
			Solution.memo[i] = self.counting_bits(i)
		return list(Solution.memo.values())[:n+1]

#solution = Solution()
# print(solution.countBits(4))
# print(solution.countBits(1))

def countBits(n):
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans

#print(countBits(4))

"""
i: 0 - 0
i: 1 - 1
i: 2 - 10
i: 3 - 11
i: 4 - 100
i: 5 - 101	
i: 6 - 110
i: 7 - 111
i: 8 - 1000

countBits(8) = countBits()

"""

def count_zero_bits(num):
	if (num == 1):
		return 0
	
	if ( num & 1 == 0):
		return 1 + count_zero_bits(num >> 1)
	else:
		return count_zero_bits(num >> 1)

# print(count_zero_bits(8))
# print(count_zero_bits(4))
# print(count_zero_bits(5))

# count up to num for each num how many zeroes.
def count_zero_bits(num):
	#zero_bits = [1]*(num + 1)
	zero_bits = [i for i in range(num + 1)]
	for i in range(1, num + 1):
		zero_bits[i] = zero_bits[i >> 1] + (i & 1 == 0)
	return zero_bits

#print(count_zero_bits(8))
print(count_zero_bits(5))

