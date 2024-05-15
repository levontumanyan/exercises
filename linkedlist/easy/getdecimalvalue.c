/* 
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.

Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
*/
#include <stdlib.h>
#include <assert.h>
#include <math.h>

struct ListNode {
	int value;
	struct ListNode *next;
} ListNode;

int getDecimalValue(struct ListNode* head);
int getDecimalValueFast(struct ListNode* head);
int getlinkedlistlength(struct ListNode* head);

int main() {
	// Test case 1: Binary 101 = Decimal 5
	struct ListNode* head1 = (struct ListNode*) malloc(sizeof(struct ListNode));
	head1->value = 1;
	head1->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head1->next->value = 0;
	head1->next->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head1->next->next->value = 1;
	head1->next->next->next = NULL;
	assert(getlinkedlistlength(head1) == 3);
	assert(getDecimalValue(head1) == 5);

	// Test case 2: Binary 0 = Decimal 0
	struct ListNode* head2 = (struct ListNode*) malloc(sizeof(struct ListNode));
	head2->value = 0;
	head2->next = NULL;
	assert(getlinkedlistlength(head2) == 1);
	assert(getDecimalValue(head2) == 0);

	// Test case 3: Binary 1111 = Decimal 15
	struct ListNode* head3 = (struct ListNode*) malloc(sizeof(struct ListNode));
	head3->value = 1;
	head3->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head3->next->value = 1;
	head3->next->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head3->next->next->value = 1;
	head3->next->next->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head3->next->next->next->value = 1;
	head3->next->next->next->next = NULL;
	assert(getlinkedlistlength(head3) == 4);
	assert(getDecimalValue(head3) == 15);
	assert(getDecimalValueFast(head3) == 15);
}

int getDecimalValue(struct ListNode* head) {
	int length = getlinkedlistlength(head);
	int result = 0;
	struct ListNode* current = head;

	for (int i = length - 1; i > -1; i--) {
		result += current->value * pow(2, i);
		current = current->next;
	}

	return result;
}

int getlinkedlistlength(struct ListNode* head) {
	struct ListNode* current = head;
	int length = 0;

	while (current != NULL) {
		length++;
		current = current->next;
	}

	return length;
}

int getDecimalValueFast(struct ListNode* head) {
	int result = 0;
	
	while (head != NULL) {
		result = (result << 1) + head->value;
		head = head->next;
	}

	return result;
}
