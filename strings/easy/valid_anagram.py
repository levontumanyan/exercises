"""Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

def valid_anagram(word1, word2):
	return sorted(word1) == sorted(word2)


def valid_anagram(word1, word2):
	if len(word1) != len(word2):
		return False
	
	for ch in word1:
		if ch not in word2:
			return False
	for ch in word2:
		if ch not in word1:
			return False
	return True

def valid_anagram(word1, word2):

	frequencies = {}

	if (len(word1) != len(word2)):
		return False

	for char in word1:
		if char not in frequencies:
			frequencies[char] = 1
		else:
			frequencies[char] += 1

	for char in word2:
		if char not in frequencies:
			return False
		else:
			frequencies[char] -= 1
	
	for freqs in frequencies.values():
		if freqs != 0:
			return False
	
	return True

print(valid_anagram("cat", "tac"))
print(valid_anagram("cat", "tasc"))
print(valid_anagram("cat", "cet"))
print(valid_anagram("aabb", "abcd"))
print(valid_anagram("nagaram", "anagram"))
