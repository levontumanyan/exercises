"""
Palindrome: A palindrome is a word, phrase, or sequence that reads the same backward as forward, such as “madam” or “racecar”. The base case is when the string is empty or has one character, it is a palindrome. The recursive case is when the string has more than one character, it is a palindrome if the first and last characters are the same and the rest of the string is a palindrome.
"""

def is_palindrome(word):

	if (len(word) == 1):
		return True
	
	return word[0] == word[-1] and is_palindrome(word[1:-1])


print(is_palindrome("madam"))
print(is_palindrome("mada"))
