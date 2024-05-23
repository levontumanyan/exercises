/* A bit flip of a number x is choosing a bit in the binary representation of x and flipping it from either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and we may choose any bit (including any leading zeros not shown) and flip it. We can flip the first bit from the right to get 110, flip the second bit from the right to get 101, flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of bit flips to convert start to goal.
*/

#include <stdio.h>

// approach will be xor the two numbers. then count the 1 bits. that count is the answer
int minBitFlips(int start, int goal) {
	// Your code here
	int xor = start^goal;
	int count = 0;

	while (xor > 0) {
		if (xor & 1 == 1) {
			count++;
		}
		xor = xor >> 1;
	}

	return count;
}

void test_minBitFlips() {
	// Your test code here
}

int main() {
	test_minBitFlips();
	return 0;
}
