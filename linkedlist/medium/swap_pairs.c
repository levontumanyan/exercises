/* Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
*/

#include <stdio.h>
#include "../linkedlist.h"

struct ListNode *swapPairs(struct ListNode *head) {
	if (head == NULL) {
		return head;
	}
	if (head->next == NULL) {
		return head;
	}

	struct ListNode *first = head;
	struct ListNode *second = head->next;
	struct ListNode *new_head;

	while (second->next != NULL) {
		first->next = second->next;
		second->next = first;

		if (first == head) {
			new_head = second;
		}

		first = first->next;
		second = first->next;
	}

	return new_head;
}

void test_swapPairs() {
	// Test case 1 - even number of items
	struct ListNode* list1 = createlinkedlistfromarray((int[]){5, 2, 13, 3, 8, 12}, 6);
	printlinkedlist(list1);
	printlinkedlist(swapPairs(list1));
}

int main() {
	test_swapPairs();
	return 0;
}
