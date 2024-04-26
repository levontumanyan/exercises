#include "linkedlist.h"
#include <stdlib.h>

/* struct ListNode {
	int val;
	struct ListNode *next;
} ListNode;
 */
struct ListNode *findmiddle(struct ListNode *head) {
	struct ListNode *current = head;
	struct ListNode *og_head = head;
	
	int count = 0;

	while (current != NULL) {
		current = current->next;
		count++;
	}

	// number of elements. 11 - 5
	for (int i = 0; i < count / 2; i++) {
		og_head = og_head->next;
	}

	return og_head;
}

struct ListNode *findmiddlefast(struct ListNode *head) {
	struct ListNode *slow = head;
	struct ListNode *fast = head;

	while (fast != NULL && fast->next != NULL) {
		slow = slow->next;
		fast = fast->next->next;
	}

	return slow;
}

int main() {
	int arr[] = {2, 3, 4, 5, 1, 2, 5, 10, 4};
	int size = sizeof(arr) / sizeof(arr[0]);
	printlinkedlist(createlinkedlistfromarray(arr, size));
	printlinkedlist(findmiddle(createlinkedlistfromarray(arr, size)));
}
