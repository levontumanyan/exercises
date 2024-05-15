/* In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list. */

// create an array of size n / 2. as we next on the linked list. i - th element in the array will be the twin sum of i th member of linked list and (n - 1 - i). Initialize the array with a certain size then keep expanding as we go. When we pass half way line we can just start going down on the index and filling it up.
#include <stdlib.h>
#include <stdio.h>
#include "../../easy/linkedlist/linkedlist.h"

int pairSum(struct ListNode* head) {
	size_t size = 10;
	size_t element_count = 0;
	int i = 0;

	int *pair_sums =  malloc(sizeof(int) * size);

	// doing the below to figure out the middle element
	struct ListNode *slow = head;
	struct ListNode *fast = head;

	while (1) {
		if (element_count >= size) {
			size *= 2;
			pair_sums = realloc(pair_sums, sizeof(int) * (size));
		}

		pair_sums[i] = slow->val;
		element_count++;
		if (fast->next->next == NULL) {
			slow = slow->next;
			fast = fast->next->next;
			break;
		}
		slow = slow->next;
		fast = fast->next->next;
		i++;
	}

	int max = 0;

	while (slow != NULL) {
		if (element_count >= size) {
			size *= 2;
			pair_sums = realloc(pair_sums, sizeof(int) * (size));
		}

		pair_sums[i] += slow->val;
		if (pair_sums[i] > max) {
			max = pair_sums[i];
		}
		i--;
		element_count++;
		slow = slow->next;
	}

	return max;
}

void test_pair_sum() {
	// Test case 1: Normal case with multiple zeroes and numbers in between
	int arr[] = {5, 4, 2, 1};
	struct ListNode* head1 = createlinkedlistfromarray(arr, sizeof(arr) / sizeof(arr[0]));
	printlinkedlist(head1);
	//printlinkedlist(mergeNodes(head1));
	printf("Element count is: %d\n", pairSum(head1));
	//assert(compareLinkedLists(result1, [3, 7]));
}

int main() {
	test_pair_sum();
	return 0;
}
