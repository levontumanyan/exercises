"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""

def group_anagrams(words):
	dict_of_frequencies = {}
	for word in words:
		dict_of_frequencies[word] = {}

		for ch in word:
			if ch in dict_of_frequencies[word]:
				dict_of_frequencies[word][ch] += 1
			else:
				dict_of_frequencies[word][ch] = 1
	
	result = []

	for word in words:
		word_list = []
		for freqs in dict_of_frequencies.items():
			if dict_of_frequencies[word] == freqs[1]:
				word_list.append(word)
		result.append(word_list)
	# kinda fail
	return result

def group_anagrams(words):
	anagrams = {}

	for word in words:
		sorted_word = "".join(sorted(word))
		if (sorted_word in anagrams):
			anagrams[sorted_word].append(word)
		else:
			anagrams[sorted_word] = [word]
	
	return list(anagrams.values())

def group_anagrams(strs):
    anagrams = {}
    for word in strs:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        # Convert list to tuple to use as a key in dict
        count = tuple(count)
        if count in anagrams:
            anagrams[count].append(word)
        else:
            anagrams[count] = [word]
    return list(anagrams.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
