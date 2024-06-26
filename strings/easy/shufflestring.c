/* You are given a string s and an integer array indices of the same length. The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string. */

#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

char *restorestring(char *s, int *indices, int indicesSize) {
	// Your code here
	char *restored = malloc(indicesSize * sizeof(char));

	for (int i = 0; i < indicesSize; i++) {
		restored[indices[i]] = s[i];
	} 

	restored[indicesSize] = '\0'; 
	return restored;
}

void test_restorestring() {
    char s1[] = "abc";
    int indices1[] = {0, 1, 2};
    assert(strcmp(restorestring(s1, indices1, 3), "abc") == 0);

    char s2[] = "abc";
    int indices2[] = {2, 1, 0};
    assert(strcmp(restorestring(s2, indices2, 3), "cba") == 0);

    char s3[] = "hello";
    int indices3[] = {0, 2, 1, 3, 4};
    assert(strcmp(restorestring(s3, indices3, 5), "hlelo") == 0);

    char s4[] = "world";
    int indices4[] = {4, 3, 2, 1, 0};
    assert(strcmp(restorestring(s4, indices4, 5), "dlrow") == 0);

    printf("All tests passed!\n");
}

int main() {
	test_restorestring();
	return 0;
}
