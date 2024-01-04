"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

"""

def keyboard_row(words):
	first_row = set("qwertyuiop")
	second_row = set("asdfghjkl")
	third_row = set("zxcvbnm")

	word_rows = {}
	result = []

	for word in words:
		for ch in word:
			if ch.lower() in first_row:
				if word not in word_rows:
					word_rows[word] = set(["first_row"])
				else:
					word_rows[word].add(("first_row"))
			elif ch.lower() in second_row:
				if word not in word_rows:
					word_rows[word] = set(["second_row"])
				else:
					word_rows[word].add(("second_row"))
			elif ch.lower() in third_row:
				if word not in word_rows:
					word_rows[word] = set(["third_row"])
				else:
					word_rows[word].add(("third_row"))
	
	for word in words:
		if len(word_rows[word]) == 1:
			result.append(word)
	
	return result

print(keyboard_row(["adsdf", "sfd"]))
print(keyboard_row(["Hello","Alaska","Dad","Peace"]))
print(keyboard_row(["omk"]))
print(keyboard_row(["asdfghjkla","qwertyuiopq","zxcvbnzzm","asdfghjkla","qwertyuiopq","zxcvbnzzm"]))
print(keyboard_row(["asdfghjkla"]))
print(keyboard_row(["Az"]))
