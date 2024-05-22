"""
You are given a 0-indexed string word, consisting of lowercase English letters. You need to select one index and remove the letter at that index from word so that the frequency of every letter present in word is equal.

Return true if it is possible to remove one letter so that the frequency of all letters in word are equal, and false otherwise.

Note:

The frequency of a letter x is the number of times it occurs in the string.
You must remove exactly one letter and cannot choose to do nothing.

Example 1:

Input: word = "abcc"
Output: true
Explanation: Select index 3 and delete it: word becomes "abc" and each character has a frequency of 1.
Example 2:

Input: word = "aazz"
Output: false
Explanation: We must delete a character, so either the frequency of "a" is 1 and the frequency of "z" is 2, or vice versa. It is impossible to make all present letters have equal frequency.
"""

def remove_letter_equalize_frequency(word):
	frequencies = {}

	for ch in word:
		if ch in frequencies:
			frequencies[ch] += 1
		else:
			frequencies[ch] = 1
	
	i = 0
	result = 0
	frequency_values = list(frequencies.values())

	for j in range(len(frequency_values)):
		if frequency_values[j] == 1 and j == len(frequency_values) - 1:
			return True
		elif frequency_values[j] == 1:
			continue
		else:
			break

	if len(frequency_values) % 2 == 0:
		while i < len(frequency_values):
			if i % 2 == 0:
				result += frequency_values[i]
			else:
				result -= frequency_values[i]
			i += 1
		return (result == 1)
	else:
		frequency_values = sorted(frequency_values)
		while i < len(frequency_values):
			if i % 2 == 0:
				result += frequency_values[i]
			else:
				result -= frequency_values[i]
			i += 1
		
		return result == frequency_values[len(frequency_values) - 1] or result == frequency_values[0]



print(remove_letter_equalize_frequency("aazz"))
print(remove_letter_equalize_frequency("aaz"))
print(remove_letter_equalize_frequency("aabbccc"))

print(remove_letter_equalize_frequency("aaabbbccccddd"))
print(remove_letter_equalize_frequency("aazza"))

print(remove_letter_equalize_frequency("adbc"))
print(remove_letter_equalize_frequency("bbac"))
print(remove_letter_equalize_frequency("abbcc"))
print(remove_letter_equalize_frequency("cbccca"))

