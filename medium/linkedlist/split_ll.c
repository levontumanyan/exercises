/* Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.
*/

#include <stdlib.h>
#include <stdio.h>
#include "../../easy/linkedlist/linkedlist.h"

struct ListNode** splitListToParts(struct ListNode* head, int k, int* returnSize) {
	size_t size = get_ll_length(head);
	size_t alists_size = size / k;
	struct ListNode** lists = malloc(k*sizeof(*lists));
	int *sizes = malloc(k * sizeof(int));
	*returnSize = k;

	for (int i = 0; i < k; i++) {
		sizes[i] = alists_size;
	}

	size_t leftover = size % k;
	int i = 0;

	while (leftover != 0) {
		sizes[i]++;
		leftover--;
		i++;
	}

	int n_th_list = 0;

	for (int i = 0; i < k; i++) {
		struct ListNode *og_head = head;
		struct ListNode *curr = head;

		while (sizes[n_th_list] > 1) {
			curr = curr->next;
			sizes[n_th_list]--;
		}

		if (curr != NULL) {
    		head = curr->next;
		}

		if (curr != NULL && curr->next != NULL) {
    		curr->next = NULL;
		}
		
		lists[n_th_list] = og_head;
		n_th_list++;
	}

	return lists;
}

void test_split_list_to_parts() {
	int arr[] = {1,2,3};
	struct ListNode* head1 = createlinkedlistfromarray(arr, sizeof(arr) / sizeof(arr[0]));
	printlinkedlist(head1);
	// Call splitListToParts
    int returnSize;
    struct ListNode** parts = splitListToParts(head1, 5, &returnSize);
	for (int i = 0; i < 3; i++) {
		printlinkedlist(parts[i]);
	}
}

int main() {
	test_split_list_to_parts();
	return 0;
}
