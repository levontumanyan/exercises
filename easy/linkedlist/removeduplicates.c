/* 
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
*/

#include <stdlib.h>
#include "linkedlist.h"

struct ListNode* deleteDuplicates(struct ListNode* head) {
	if (head == NULL) {
		return NULL;
	}
	
	struct ListNode *current = head->next;
	struct ListNode *prev = head;

	while (current != NULL) {
		if (current->val == prev->val) {
			current = current->next;
			prev->next = current;
			continue;
		}
		current = current->next;
		prev = prev->next;
	}

	return head;
}

void test_remove_duplicates() {
	int arr1[] = {1, 1, 1, 2, 4, 4, 5, 6, 7, 7, 7};
	int length = sizeof(arr1) / sizeof(arr1[0]);
	struct ListNode *head1 = createlinkedlistfromarray(arr1, length);
	printlinkedlist(head1);
	printlinkedlist(deleteDuplicates(head1));
}

int main() {
	test_remove_duplicates();
	return 0;
}
