"""
def words_with_letters(words, letters):
This problem serves as an excuse to introduce some general discrete math terminology that will help make many later problem speci6ications less convoluted and ambiguous. A substring of a string consists of characters taken in order from consecutive positions. Contrast this with the simi- lar concept of subsequence of characters still taken in order, but not necessarily at consecutive po- sitions. For example, each of the 6ive strings '', 'e', 'put', 'ompu' and 'computer' is both a substring and subsequence of the string 'computer', whereas 'cper' and 'out' are subse- quences, but not substrings.
Note how the empty string is always a substring of every possible string, including itself. Every string is always its own substring, although not a proper substring the same way how all other substrings are proper. Concepts of sublist and subsequence are de6ined for lists in an analogous manner. Since sets have no internal order on top of the element membership in that set, sets can meaningfully have both proper and improper subsets. (The concept of “subsetquence” might mean a subset that would be a subsequence, were the members of that set were written out sequentially in sorted order. But that term was just made up ad hoc for its comical value.)
Now that you know all that, given a list of words sorted in alphabetical order, and a string of re- quired letters, 6ind and return the list of words that contain letters as a subsequence.
"""

def words_with_letters(words, letters):
	with open(words) as words:
		for word in words:
			for letter in letters:
				
