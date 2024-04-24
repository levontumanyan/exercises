#include <stdio.h>

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n);

#include <stdio.h>

// Function to print an array
void printArray(int* arr, int size) {
	printf("[");
	for (int i = 0; i < size; i++) {
		printf("%d", arr[i]);
		if (i < size - 1) {
			printf(", ");
		}
	}
	printf("]\n");
}

// Test cases for the merge function
void testMerge() {
	int nums1[] = {1, 2, 9, 0, 0, 0};
	int nums2[] = {2, 5, 6};
	int nums1size = 6;
	int nums2size = 3;
	int m = 3;
	int n = 3;
	merge(nums1, nums1size, m, nums2, nums2size, n);
	printArray(nums1, nums1size); // Expected output: [1, 2, 2, 5, 6, 9]

	int nums3[] = {4, 0, 0, 0, 0, 0};
	int nums4[] = {1, 2, 3, 5, 6};
	int nums3size = 6;
	int nums4size = 5;
	m = 1;
	n = 5;
	merge(nums3, nums3size, m, nums4, nums4size, n);
	printArray(nums3, nums3size); // Expected output: [1, 2, 3, 4, 5, 6]

	int nums5[] = {1, 2, 3, 0, 0, 0};
	int nums6[] = {2, 5, 6};
	int nums5size = 6;
	int nums6size = 3;
	m = 3;
	n = 3;
	merge(nums5, nums5size, m, nums6, nums6size, n);
	printArray(nums5, nums5size);

	int nums7[] = {0};
	int nums8[] = {1};
	int nums7size = 1;
	int nums8size = 1;
	m = 0;
	n = 1;
	merge(nums7, nums7size, m, nums8, nums8size, n);
	printArray(nums7, nums7size);

	int nums9[] = {2, 0};
	int nums10[] = {1};
	int nums9size = 2;
	int nums10size = 1;
	m = 1;
	n = 1;
	merge(nums9, nums9size, m, nums10, nums10size, n);
	printArray(nums9, nums9size); // Expected output: [1, 2]
}

int main() {
	testMerge();
	return 0;
}

/* Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
*/

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
	//int nums1p = m - 1;
	if (n == 0) {
		return;
	}
	int nums1p = (m - 1 == -1) ? 0 : m - 1;
	int nums2p = n - 1;
	int mergedp = m + n - 1;

	do {
		if (nums2[nums2p] >= nums1[nums1p]) {
			nums1[mergedp] = nums2[nums2p];
			nums2p--;
		}
		else {
			nums1[mergedp] = nums1[nums1p];
			nums1[nums1p] = 0;
			nums1p--;
			if (nums1p < 0) {
				nums1p = 0;	
			}
		}
		mergedp--;
	}
	while (nums1p < mergedp || nums2p >= 0);
}
