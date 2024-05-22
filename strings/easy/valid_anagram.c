/* 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
*/

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <assert.h>

// We can employ the following approach. Create an array of frequencies. index will correspond to the ascii value. We do this for the first string, then when we traverse through the characters of the second string we will check at the end to see if the array is all zeroes. That should mean an anagram. anything else means not an anagram.

bool isAnagram(char* s, char* t) {
	// Your code here
	int *frequencies = calloc(256, sizeof(int));

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
		if (frequencies[i] != 0) {
			return false;
		}
	}

	return true;
}

void test_valid_anagram() {
	assert(isAnagram("hello", "olleh") == true);
    assert(isAnagram("listen", "silent") == true);
    assert(isAnagram("triangle", "integral") == true);
    assert(isAnagram("hello", "world") == false);
    assert(isAnagram("test", "tset") == true);
    assert(isAnagram("anagram", "nagaram") == true);
    assert(isAnagram("rat", "car") == false);
    assert(isAnagram("", "") == true);
    assert(isAnagram("a", "a") == true);
    assert(isAnagram("ab", "a") == false);
    printf("All test cases passed for isAnagram.\n");
}

int main() {
	test_valid_anagram();
	return 0;
}
