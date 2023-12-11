def reverse_string(word):
	if len(word) == 1:
		return word
	
	return word[-1] + reverse_string(word[:-1])

print(reverse_string("hello"))
print(reverse_string("madam"))
print(reverse_string("gergo"))
