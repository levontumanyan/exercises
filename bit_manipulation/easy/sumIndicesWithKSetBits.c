/* You are given a 0-indexed integer array nums and an integer k.

Return an integer that denotes the sum of elements in nums whose corresponding indices have exactly k set bits in their binary representation.

The set bits in an integer are the 1's present when it is written in binary.

For example, the binary representation of 21 is 10101, which has 3 set bits. */

#include <stdio.h>

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

int sumIndicesWithKSetBits(int *nums, int numsSize, int k) {
	int sum = 0;

	for (int i = 0; i < numsSize; i++) {
		if (count_one_bits(i) == k) {
			sum += nums[i];
		}
	}
	printf("%d ", sum);
	return sum;
}

void test_sumIndicesWithKSetBits() {
	// Your test code here
	int nums1[] = {5, 10, 1, 5, 2};
	int nums2[] = {5, 1, 6};
	int nums3[] = {3, 4, 5, 6, 7, 8};
	int nums4[] = {0};
	int nums5[] = {1, 2, 3, 4, 5};

	printf("%d ", sumIndicesWithKSetBits(nums1, 5, 1));
	printf("Test 1 passed: %s\n", sumIndicesWithKSetBits(nums1, 5, 1) == 13 ? "Yes" : "No");
	/*
	printf("Test 2 passed: %s\n", sumIndicesWithKSetBits(nums2, 3, 2) == 7 ? "Yes" : "No");
	printf("Test 3 passed: %s\n", sumIndicesWithKSetBits(nums3, 6, 2) == 15 ? "Yes" : "No");
	printf("Test 4 passed: %s\n", sumIndicesWithKSetBits(nums4, 1, 0) == 0 ? "Yes" : "No");
	printf("Test 5 passed: %s\n", sumIndicesWithKSetBits(nums5, 5, 2) == 7 ? "Yes" : "No"); */
}

int main() {
	test_sumIndicesWithKSetBits();
	return 0;
}
