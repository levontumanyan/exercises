"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T. Your task is to find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
Input
The only input line contains a string of n characters.
Output
Print one integer: the length of the longest repetition.
Constraints

1 \le n \le 10^6

Example
Input:
ATTCGGGA

Output:
3
"""

def longest_repetition(dna_sequence):

	current_max = 1
	overall_max = 1
	
	for i in range(len(dna_sequence) - 1):
		if dna_sequence[i] == dna_sequence[i+1]:
			current_max += 1
		else:
			overall_max = max(overall_max, current_max)
			current_max = 1
	return overall_max

print(longest_repetition("AACTGGGA"))
print(longest_repetition("AACTGGGGGA"))
print(longest_repetition("AACTTTTGGGA"))
print(longest_repetition("ATTCGGGA"))
print(longest_repetition("A"))


# dna_sequence = input()
# print(longest_repetition(dna_sequence))
