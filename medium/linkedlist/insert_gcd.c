/* Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers. */

#include <stdio.h>

#include "../../easy/linkedlist/linkedlist.h"

int gcd(int a, int b) {
	while (b != 0) {
		int temp = b;
		b = a % b;
		a = temp;
	}

	return a;
}

/* Initialize two pointers, fast and slow. Fast will be one node ahead from slow. */
struct ListNode* insertGreatestCommonDivisors(struct ListNode* head){
	if (head == NULL) {
		return NULL;
	}

	if (head->next == NULL) {
		return head;
	}

	struct ListNode *slow = head;
	struct ListNode *fast = head->next;

	while (fast != NULL) {
		struct ListNode *gcd_node = malloc(sizeof(*gcd_node));
		gcd_node->val = gcd(slow->val, fast->val);
		gcd_node->next = fast;
		slow->next = gcd_node;
		slow = fast;
		fast = fast->next;
	}

	return head;
}
