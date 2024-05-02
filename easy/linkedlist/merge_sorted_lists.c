/* You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
*/
#include <stdlib.h>
#include <stdio.h>
#include "linkedlist.h"

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2);

int main() {
	// Create first list
	struct ListNode* list1 = malloc(sizeof(struct ListNode));
	list1->val = 1;
	list1->next = malloc(sizeof(struct ListNode));
	list1->next->val = 3;
	list1->next->next = malloc(sizeof(struct ListNode));
	list1->next->next->val = 5;
	list1->next->next->next = NULL;
	printlinkedlist(list1);

	// Create second list
	struct ListNode* list2 = malloc(sizeof(struct ListNode));
	list2->val = 2;
	list2->next = malloc(sizeof(struct ListNode));
	list2->next->val = 4;
	list2->next->next = malloc(sizeof(struct ListNode));
	list2->next->next->val = 6;
	list2->next->next->next = NULL;
	printlinkedlist(list2);

	// Merge the lists
	struct ListNode* mergedList = mergeTwoLists(list1, list2);

	// Print the merged list
	struct ListNode* current = mergedList;
	printlinkedlist(current);

	return 0;

}

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
	struct ListNode* result;
	struct ListNode* head;

	if (list1 == NULL && list2 == NULL) {
		return NULL;
	}

	if (list1 == NULL) {
		return list2;
	}
	
	if (list2 == NULL) {
		return list1;
	}

	if (list1->val <= list2->val) {
		result = list1;
		list1 = list1->next;
	}
	else {
		result = list2;
		list2 = list2->next;
	}

	head = result;

	while (list1 != NULL || list2 != NULL) {
		if (list1 == NULL) {
			result->next = list2;
			break;
		}
		if (list2 == NULL) {
			result->next = list1;
			break;
		}
		
		if (list1->val <= list2->val) {
			result->next = list1;
			list1 = list1->next;
		}
		else {
			result->next = list2;
			list2 = list2->next;
		}
		
		result = result->next;
 	}

	return head;
}
