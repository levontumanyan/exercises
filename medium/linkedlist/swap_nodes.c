/* Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
*/

#include <stdlib.h>
#include <stdio.h>
#include "../../easy/linkedlist/linkedlist.h"

struct ListNode* swapNodes(struct ListNode* head, int k) {
	struct ListNode *curr = head;
	
	for (int i = 1; i < k; i++) {
		curr = curr->next;
	}
	
	struct ListNode *left_k = curr;

	curr = head;

	struct ListNode *right_k;

	size_t size = 0;
	while (curr != NULL) {
		size++;
		curr = curr->next;
	}

	curr = head;

	for (int j = 0; j < size - k; j++) {
		curr = curr->next;
	}
	
	right_k = curr;
	
	int temp = left_k->val;
	left_k->val = right_k->val;
	right_k->val = temp;

	return head;
}

void test_swap_nodes() {
	// Test case 1: Normal case with multiple zeroes and numbers in between
	int arr[] = {7,9,6,6,7,8,3,0,9,5};
	struct ListNode* head1 = createlinkedlistfromarray(arr, sizeof(arr) / sizeof(arr[0]));
	printlinkedlist(head1);
	printlinkedlist(swapNodes(head1, 5));
	//assert(compareLinkedLists(result1, [3, 7]));
}

int main() {
	test_swap_nodes();
	return 0;
}
