/* You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

Return an integer array answer where answer = [even, odd].
*/

/**
 * Note: The returned array must be malloced, assume caller calls free().
*/

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int *evenOddBit(int n, int* returnSize) {
	// Your code here
	int *result = calloc(2, sizeof(int));
	*returnSize = 2;

	int i = 0;

	while (n > 0) {
		if ((n & 1) == 1) {
			if (i % 2 == 0) {
				result[0]++;
			}
			else {
				result[1]++;
			}
		}
		n = n >> 1;
		i++;
	}

	return result;
}

void test_evenOddBit() {
    int returnSize;
    int *result;

    // Test case 1: n = 5 (binary: 101)
    result = evenOddBit(5, &returnSize);
    assert(returnSize == 2);
    assert(result[0] == 2);
    assert(result[1] == 0);
    free(result);

    // Test case 2: n = 10 (binary: 1010)
    // even indices with value 1: 2 (indices 1, 3)
    // odd indices with value 1: 0
    result = evenOddBit(10, &returnSize);
    assert(returnSize == 2);
    assert(result[0] == 0);
    assert(result[1] == 2);
    free(result);

    printf("All test cases passed for evenOddBit.\n");
}

int main() {
	test_evenOddBit();
	return 0;
}
