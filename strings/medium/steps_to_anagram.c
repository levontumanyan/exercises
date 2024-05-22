/* You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering. 

Example 1:

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams. 
*/

#include <stdio.h>

int minSteps(char* s, char* t) {
	// Your code here
	int *frequencies = calloc(256, sizeof(int));
	int result = 0;

	// iterate through the first word and create the frequencies table
	int i = 0;
	while (*(s + i) != '\0') {
		frequencies[*(s + i)]++;
		i++;
	}

	i = 0;
	while (*(t + i) != '\0') {
		frequencies[*(t + i)]--;
		i++;
	}

	for (int i = 0; i < 256; i++) {
		
	}



	return 0;
}

void test_minSteps(`) {
	// Your test code here
}

int main() {
	test_minSteps(`);
	return 0;
}
