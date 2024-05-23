/* Given a string s consisting of lowercase English letters, return the first letter to appear twice.

Note:

A letter a appears twice before another letter b if the second occurrence of a is before the second occurrence of b.
s will contain at least one letter that appears twice.
*/

#include <stdio.h>
#include <stdlib.h>

char repeatedCharacter(char *s) {
	// Your code here
	int *frequencies = calloc(26 , sizeof(int));

	int i = 0;

	while (*(s + i) != '\0') {
		if (frequencies[*(s + i) - 'a'] == 1) {
			return *(s + i);
		}

		frequencies[*(s + i) - 'a']++;
		i++;
	}

 	return 0;
}

void test_repeatedCharacter() {
	// Your test code here
    char *test1 = "abcabc";
    char *test2 = "abcdabcd";
    char *test3 = "abcabcabc";
    char *test4 = "abcdabcdabcd";
    char *test5 = "abcabcabcabc";
    char *test6 = "abccbaacz";

    printf("Test 1: %s\n", repeatedCharacter(test1) == 'a' ? "Passed" : "Failed");
    printf("Test 2: %s\n", repeatedCharacter(test2) == 'a' ? "Passed" : "Failed");
    printf("Test 3: %s\n", repeatedCharacter(test3) == 'a' ? "Passed" : "Failed");
    printf("Test 4: %s\n", repeatedCharacter(test4) == 'a' ? "Passed" : "Failed");
    printf("Test 5: %s\n", repeatedCharacter(test5) == 'a' ? "Passed" : "Failed");
    printf("Test 6: %c\n", repeatedCharacter(test6));
	printf("Test 6: %s\n", repeatedCharacter(test6) == 'c' ? "Passed" : "Failed");
}

int main() {
	test_repeatedCharacter();
	return 0;
}
