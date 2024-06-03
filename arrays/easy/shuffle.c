/* Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].
*/

#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

int* shuffle(int* nums, int numsSize, int n) {
	int *temp = (int *) malloc(sizeof(int) * numsSize);
	int index = 0;

	for (int i = 0; i < n; i++) {
		temp[index] = nums[i];
		index += 2;
	}

	index = 1;

	for (int i = n; i < numsSize; i++) {
		temp[index] = nums[i];
		index += 2;
	}

	return temp;
}

void test_shuffle() {
	int nums1[] = {2, 5, 1, 3, 4, 7};
    int numsSize1 = sizeof(nums1) / sizeof(nums1[0]);
    int n1 = numsSize1 / 2;
    int *new_nums1 = shuffle(nums1, numsSize1, n1);
    int expected1[] = {2, 3, 5, 4, 1, 7};
    for (int i = 0; i < numsSize1; i++) {
        assert(new_nums1[i] == expected1[i]);
    }
    free(new_nums1);
}

int main() {
	test_shuffle();
	return 0;
}
