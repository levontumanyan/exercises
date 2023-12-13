"""
Given a string find its first uppercase letter
Examples : 

Input : geeksforgeeKs
Output : K

Input  : geekS
Output : S
Method 1: linear search 
Using linear search, find the first character which is capital 
"""

def first_uppercase(word):
	if len(word) == 0:
		return None
	
	if word[0].isupper():
		return word[0]
	else:
		return first_uppercase(word[1:])

print(first_uppercase("elloHyeaufn"))
print(first_uppercase("elloyeaufn"))
print(first_uppercase(""))
