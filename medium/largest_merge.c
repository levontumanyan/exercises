/* You are given two strings word1 and word2. You want to construct a string merge in the following way: while either word1 or word2 are non-empty, choose one of the following options:

If word1 is non-empty, append the first character in word1 to merge and delete it from word1.
For example, if word1 = "abc" and merge = "dv", then after choosing this operation, word1 = "bc" and merge = "dva".
If word2 is non-empty, append the first character in word2 to merge and delete it from word2.
For example, if word2 = "abc" and merge = "", then after choosing this operation, word2 = "bc" and merge = "a".
Return the lexicographically largest merge you can construct.

A string a is lexicographically larger than a string b (of the same length) if in the first position where a and b differ, a has a character strictly larger than the corresponding character in b. For example, "abcd" is lexicographically larger than "abcc" because the first position they differ is at the fourth character, and d is greater than c.

 

Example 1:

Input: word1 = "cabaa", word2 = "bcaaa"
Output: "cbcabaaaaa"
Explanation: One way to get the lexicographically largest merge is:
- Take from word1: merge = "c", word1 = "abaa", word2 = "bcaaa"
- Take from word2: merge = "cb", word1 = "abaa", word2 = "caaa"
- Take from word2: merge = "cbc", word1 = "abaa", word2 = "aaa"
- Take from word1: merge = "cbca", word1 = "baa", word2 = "aaa"
- Take from word1: merge = "cbcab", word1 = "aa", word2 = "aaa"
- Append the remaining 5 a's from word1 and word2 at the end of merge.
Example 2:

Input: word1 = "abcabc", word2 = "abdcaba"
Output: "abdcabcabcaba" */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

unsigned char largestahead(char *word1, char *word2);
char* largestMerge(char* word1, char* word2);

int main() {
	char *word1 = "cabaa";
	char *word2 = "bcaaa";

	char *merged1 = largestMerge(word1, word2);
	printf("Merged word is: %s\n", merged1);

	char *wor1 = "abcabc";
	char *wor2 = "abdcaba";
	printf("Largest ahead is: %d\n", largestahead(wor1, wor2));


	char *merged2 = largestMerge(wor1, wor2);
	printf("Merged word is: %s\n", merged2);
}

unsigned char largestahead(char *word1, char *word2) {
	int w1p = 0;
	int w2p = 0;

	while (w1p == w2p) {
		if (word1[w1p] == word2[w2p]) {
			w1p++;
			w2p++;
		}
		else if (word1[w1p] > word2[w2p]) {
			return 1;
		}
		else if (word1[w1p] < word2[w2p]) {
			return 2;
		}

		if (w1p == strlen(word1) && w2p == strlen(word2)) {
			return 0;
		}
		else if (w1p == strlen(word1)) {
			return 2;
		}
		else if (w2p == strlen(word2)) {
			return 1;
		}
	}

	return 0;
}

char* largestMerge(char* word1, char* word2) {
	int merged_len = strlen(word1) + strlen(word2);
	char *merged = (char *) malloc(sizeof(char) * (merged_len + 1));

	int w1p = 0;
	int w2p = 0;

	while (w1p < strlen(word1) || w2p < strlen(word2)) {
		if (w1p < strlen(word1) && w2p < strlen(word2)) {
			if (word1[w1p] > word2[w2p]) {
				merged[w1p + w2p] = word1[w1p];
				w1p++;
			}
			else if (word1[w1p] < word2[w2p]) {
				merged[w1p + w2p] = word2[w2p];
				w2p++;
			}
			else {
				if (largestahead(word1 + w1p, word2 + w2p) == 1) {
					merged[w1p + w2p] = word1[w1p];
					w1p++;
				}
				else if (largestahead(word1 + w1p, word2 + w2p) == 2 || largestahead(word1 + w1p, word2 + w2p) == 0) {
					merged[w1p + w2p] = word2[w2p];
					w2p++;
				}
			}
		}
		else if (w1p < strlen(word1)) {
			merged[w1p + w2p] = word1[w1p];
			w1p++;
		}
		else {
			merged[w1p + w2p] = word2[w2p];
			w2p++;
		}
	}

	merged[merged_len + 1] = '\0';

	return merged;
}
