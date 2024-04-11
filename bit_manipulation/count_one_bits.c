/*
Write a function that takes the binary representation of an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

Example 1:

Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
Example 2:

Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
Example 3:

Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
*/
#include <stdio.h>

int hammingWeight(int num) {
	// thinking about anding with one, if result is 1 count++, shifting to the right by a bit and repeating the process until the number is less than or equal to zero
	int count = 0;
	while (num > 0) {
		if ((num & 1) == 1) {
			count++;
		}
		num = num >> 1;
	}
	return count;
}

void print_binary(int num) {
	if (num == 0) {
		return;
	}

	print_binary(num / 2);

	printf("%d", num % 2);
}

int main() {
	print_binary(8);
	printf("\n");
	print_binary(9 >> 2);
	printf("\n");
	print_binary(7 >> 1);
	hammingWeight(11);
}
