#include <stdio.h>

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n);

int main() {
	int nums1[] = {1, 2, 9, 0, 0, 0};
	int nums2[] = {2, 5, 6};
	int nums1size = 6;
	int nums2size = 3;
	int m = 3;
	int n = 3;
	merge(nums1, nums1size, m, nums2, nums2size, n);
}

void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n) {
	int nums1pointer = m - 1;
	int nums2pointer = nums2Size - 1;
	int nums1counter = nums1Size - 1;

	while(nums2pointer >= 0) {
		if (nums2[nums2pointer] > nums1[nums1pointer]) {
			nums1[nums1counter] = nums2[nums2pointer];
			nums1counter--;
			nums2pointer--;
		}
		else if (nums2[nums2pointer] <= nums1[nums1pointer]) {
			nums1[nums1counter] = nums1[nums1pointer];
			nums1counter--;
			nums1pointer--;
		}
	}

	for (int x = 0; x < m + n; x++) {
		printf("%d", nums1[x]);
	}
}
