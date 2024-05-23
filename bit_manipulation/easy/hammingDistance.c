/* The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.
*/

#include <stdio.h>

// approach will be to xor the numbers together then count the one bits
int count_one_bits(int num) {
	int count = 0;

	while (num > 0) {
		if ((num & 1) == 1) {
			count++;
		}
		num = num >> 1;
	}

	return count;
}

int hammingDistance(int x, int y) {
	// Your code here
	return (count_one_bits(x^y));
}

void test_hammingDistance() {
	// Your test code here
	printf("%d ", hammingDistance(1, 4));
    printf("Test 1 passed: %s\n", hammingDistance(1, 4) == 2 ? "Yes" : "No");
    printf("Test 2 passed: %s\n", hammingDistance(3, 1) == 1 ? "Yes" : "No");
	printf("%d ", hammingDistance(14, 4));
	printf("Test 4 passed: %s\n", hammingDistance(0, 0) == 0 ? "Yes" : "No");
    printf("Test 5 passed: %s\n", hammingDistance(7, 8) == 4 ? "Yes" : "No");
}

int main() {
	test_hammingDistance();
	return 0;
}
