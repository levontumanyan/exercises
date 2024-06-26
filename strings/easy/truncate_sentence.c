/* A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.
You are given a sentence s​​​​​​ and an integer k​​​​​​. You want to truncate s​​​​​​ such that it contains only the first k​​​​​​ words. Return s​​​​​​ after truncating it.
*/

#include <stdio.h>
#include <assert.h>
#include <string.h>

char* truncateSentence(char* s, int k) {
	int i = 0;
	int spaces = 0;

	while (spaces != k) {
		if (s[i] == '\0') {
			return s;
		}

		if(s[i] == ' ') {
			spaces++;
		}
		i++;
	}

	s[i - 1] = '\0';

	return s;
}

void test_truncateSentence() {
    char test1[] = "Hello world this is a test sentence";
    assert(strcmp(truncateSentence(test1, 4), "Hello world this is") == 0);

    char test2[] = "Another test sentence for truncation";
    assert(strcmp(truncateSentence(test2, 2), "Another test") == 0);

    char test3[] = "Singleword";
    assert(strcmp(truncateSentence(test3, 1), "Singleword") == 0);

    char test4[] = "This sentence has many words and we want to truncate it to just a few words";
    assert(strcmp(truncateSentence(test4, 10), "This sentence has many words and we want to truncate") == 0);

    char test5[] = "";
    assert(strcmp(truncateSentence(test5, 5), "") == 0);

    printf("All tests passed!\n");
}

int main() {
	test_truncateSentence();
	return 0;
}
