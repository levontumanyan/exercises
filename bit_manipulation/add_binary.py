"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

def add_binary(num1, num2):
	return bin(int(num1, 2) + int(num2, 2))[2:]

print(add_binary("110", "111"))