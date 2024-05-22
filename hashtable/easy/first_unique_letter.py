"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
"""

def first_unique_letter(word):
	word_frequencies = {}

	for ch in word:
		if ch in word_frequencies:
			word_frequencies[ch] += 1
		else:
			word_frequencies[ch] = 1

	for i in range(len(word)):
		if word_frequencies[word[i]] == 1:
			return i
	return -1

print(first_unique_letter("leetcode"))
print(first_unique_letter("aabb"))
print(first_unique_letter("loveleetcode"))