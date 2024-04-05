/* Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1. */

#include <stdio.h>

int pivotIndex(int* nums, int numsSize);

int main() {
	int numbers[] = {1, 7, 3, 6, 5, 6};
	int numbers2[] = {2, 1, -1};
	int numbers3[] = {1, 2, 3, 5, 6, 7, 10};
	printf("Pivot is at: %d\n", pivotIndex(numbers, 6));
	printf("Pivot is at: %d\n", pivotIndex(numbers2, 3));
	printf("Pivot is at: %d\n", pivotIndex(numbers3, 7));
}

int pivotIndex(int* nums, int numsSize) {
	int pivot = 0;
	int left_sum = 0;
	int right_sum = 0;

	for (int i = 1; i < numsSize; i++) {
		right_sum += nums[i];
	}

	while (left_sum != right_sum) {
		if (pivot == numsSize) {
			return -1;
		}
		pivot++;
		left_sum += nums[pivot - 1];
		right_sum -= nums[pivot];
	}

	return pivot;
}
