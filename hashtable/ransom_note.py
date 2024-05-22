"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

def ransom_note( ransomnote, magazine ):
	ransom_note_frequencies = {}
	magazine_frequencies = {}

	for ch in ransomnote:
		if ch in ransom_note_frequencies:
			ransom_note_frequencies[ch] += 1
		else:
			ransom_note_frequencies[ch] = 1
	
	for ch in magazine:
		if ch in magazine_frequencies:
			magazine_frequencies[ch] += 1
		else:
			magazine_frequencies[ch] = 1
	
	for ch in ransom_note_frequencies.keys():
		if ch not in magazine_frequencies:
			return False
		if ransom_note_frequencies[ch] <= magazine_frequencies[ch]:
			continue
		if ransom_note_frequencies[ch] > magazine_frequencies[ch]:
			return False
	return True

print(ransom_note("aa", "aab"))
print(ransom_note("a", "b"))

			