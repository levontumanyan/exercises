"""
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
 

Constraints:

1 <= s.length <= 105
s[i] is either 'A', 'C', 'G', or 'T'.
"""

def repeated_dna_sequences(sequences):
	dna = [ 'A', 'C', 'G', 'T' ]
	result = []

	window_start = 0
	window_end = 1

	while window_end < len(sequences):
		if sequences[window_start] == sequences[window_end]:
			window_end += 1
			continue
		else:
			result.append(sequences[window_start:window_end])
			window_start = window_end
			window_end = window_start + 1
	result.append(sequences[window_start:window_end])
	return result

# print(repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
# print(repeated_dna_sequences("AAAAAAAAAACCCCCCAAAAAGGGTTT"))
# print(repeated_dna_sequences("AAA"))

# Now the solution to the actual problem.
# My idea is to have a sliding window of size 10. As we slide through the array we add each substring of size 10 into a hashtable which keeps occurences of each substring.
# At the end we will loop through the hashtable and return the substrings which have an occurence of more than 1.

def repeated_dna_sequences(sequences):
	frequencies = {}
	window_start = 0
	window_end = 9
	result = set()

	while window_end < len(sequences):
		ten_substring = sequences[window_start:window_end+1]

		if ten_substring in frequencies:
			result.add(ten_substring)
		else:
			frequencies[ten_substring] = 1
		
		window_start += 1
		window_end += 1
	
	return result

print(repeated_dna_sequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(repeated_dna_sequences("AAAAAAAAAACCCCCCAAAAAGGGTTT"))
print(repeated_dna_sequences("AAA"))
print(repeated_dna_sequences("AAAAAAAAAAA"))

