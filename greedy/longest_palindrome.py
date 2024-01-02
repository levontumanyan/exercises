"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""

def longest_palindrome(word):
	frequencies = {}
	result = 0
	odd_exists = False

	for ch in word:
		if ch in frequencies:
			frequencies[ch] += 1
		else:
			frequencies[ch] = 1
	
	for frequency in frequencies.values():
		if frequency % 2 == 0:
			result += frequency
		elif frequency > 1:
			result += frequency - 1
	
	for frequency in frequencies.values():
		if frequency % 2 == 1:
			return result + 1
	return result


def longest_palindrome(word):
	frequencies = {}
	result = 0
	odd_exists = False

	for ch in word:
		if ch in frequencies:
			frequencies[ch] += 1
		else:
			frequencies[ch] = 1
	
	for frequency in frequencies.values():
		result += frequency // 2 * 2
		if frequency % 2 == 1:
			odd_exists = True
	
	if odd_exists:
		result += 1
	return result

print(longest_palindrome("abccccdd"))
print(longest_palindrome("a"))
print(longest_palindrome("bb"))
