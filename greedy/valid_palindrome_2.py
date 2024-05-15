"""
Valid Palindrome II

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
"""
# below solves a different problem

def valid_palindrome(word):
	frequencies = {}
	count_odds = 0
	even_exists = False

	for ch in word:
		if ch in frequencies:
			frequencies[ch] += 1
		else:
			frequencies[ch] = 1

	for frequency in frequencies.values():
		if frequency % 2 == 0:
			even_exists = True
		else:
			count_odds += 1
		
		if count_odds > 2:
			return False
	return even_exists

print(valid_palindrome("abc"))
print(valid_palindrome("aba"))
print(valid_palindrome("abba"))
print(valid_palindrome("tebbem"))

def valid_palindrome(word):
	window_start = 0
	window_end = len(word) - 1

	while window_start < window_end:
		

		