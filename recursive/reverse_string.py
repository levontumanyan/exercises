"""
Reverse a String: The reverse of a string is the string with its characters in the opposite order. The base case is when the string is empty or has one character, the reverse is the same string. The recursive case is when the string has more than one character, the reverse is the last character of the string concatenated with the reverse of the rest of the string.
"""

def reverse_string(word):

	if len(word) == 1:
		return word
	
	return word[-1] + reverse_string(word[:-1])


print(reverse_string('hello'))