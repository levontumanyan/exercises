/* Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces. 
*/
#include <string.h>
#include <assert.h>
#include <stdio.h>

int lengthOfLongestSubstring(char* s);

int main() {
	/* assert(lengthOfLongestSubstring("abcabcbb") == 3);
	assert(lengthOfLongestSubstring("bbbbb") == 1);
	assert(lengthOfLongestSubstring("pwwkew") == 3);
	assert(lengthOfLongestSubstring("") == 0);
	assert(lengthOfLongestSubstring(" ") == 1);
	assert(lengthOfLongestSubstring("au") == 2);
	assert(lengthOfLongestSubstring("dvdf") == 3);
	assert(lengthOfLongestSubstring("anviaj") == 5); */

	printf("All tests passed!\n");
	printf("%d\n", lengthOfLongestSubstring("abcabcbb"));
	printf("%d\n", lengthOfLongestSubstring(" "));
	printf("%d\n", lengthOfLongestSubstring("dvdf"));
	return 0;
}

int lengthOfLongestSubstring(char* s) {
	int left = 0;
	int right = 0;
	int max_length = 0;
	int length = 0;
	gotohere:

	while (right < strlen(s)) {
		for (int i = left; i < right; i++) {
			if (s[right] == s[i]) {
				left++;
				if (length > max_length) {
					max_length = length;
				}
				length--;
				goto gotohere;
			}
		}
		length++;
		right++;
		if (length > max_length) {
			max_length = length;
		}
	}

	return max_length;
}
