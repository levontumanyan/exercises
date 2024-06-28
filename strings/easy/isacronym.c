/* Given an array of strings words and a string s, determine if s is an acronym of words.

The string s is considered an acronym of words if it can be formed by concatenating the first character of each string in words in order. For example, "ab" can be formed from ["apple", "banana"], but it can't be formed from ["bear", "aardvark"].

Return true if s is an acronym of words, and false otherwise.

*/

#include <stdio.h>
#include <assert.h>
#include <stdbool.h>

bool isacronym(char **words, int wordsSize, char *s) {
	int i = 0;

	while (i < wordsSize) {
		if (s[i] == '\0') {
			return false;
		}

		if (words[i][0] != s[i]) {
			return false;
		}
		i++;
	}

	if (s[i] != '\0') {
		return false;
	}

	return true;
}

void test_isacronym() {
	// Your test code here
}

int main() {
	test_isacronym();
	return 0;
}
