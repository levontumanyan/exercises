/**
Given the head of a singly linked list, reverse the list, and return the reversed list.
* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     struct ListNode *next;
* };

*/

#include <stdio.h>
#include <stdlib.h>

#include "linkedlist.h"

struct ListNode* reversell_recursive(struct ListNode *head) {
	if (head == NULL || head->next == NULL) {
		return head;
	}

	struct ListNode* rest = reversell_recursive(head->next);
	head->next->next = head;
	head->next = NULL;
	return rest;
}

struct ListNode* reversell_iterative(struct ListNode *head) {
	struct ListNode *first = head;
	struct ListNode *second = head->next;

	while(1) {
		second->next = first;

	}
}

void testReverseList() {
	int arr1[] = { 4, 2, 1, 5, 2, 7, 7, 8};
	struct ListNode* test1 = createlinkedlistfromarray(arr1, sizeof(arr1) / sizeof(arr1[0]));
	printf("Original List: ");
	printlinkedlist(test1);
	printf("Reversed List: ");
	printlinkedlist(reversell_recursive(test1));
}

int main() {
	testReverseList();
	return 0;
}
