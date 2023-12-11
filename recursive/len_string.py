"""
Given a string calculate length of the string using recursion. 

Examples: 

Input : str = "abcd"
Output :4

Input : str = "GEEKSFORGEEKS"
Output :13
"""

def len_string(word):

	if word == "":
		return 0
	
	return 1 + len_string(word[:-1])

print(len_string("asdasdas"))
