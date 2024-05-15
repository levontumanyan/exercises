/* Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1:

Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:

Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100 
*/
#include <stdlib.h>
#include <assert.h>

struct ListNode {
	int val;
	struct ListNode *next;
} ListNode;

struct ListNode* middleNode(struct ListNode* head);
int getlinkedlistlength(struct ListNode* head);

int main() {
	// Test case 1: Middle node of [1,2,3,4,5] is 3
	struct ListNode* head1 = (struct ListNode*) malloc(sizeof(struct ListNode));
	head1->val = 1;
	head1->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head1->next->val = 2;
	head1->next->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head1->next->next->val = 3;
	head1->next->next->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head1->next->next->next->val = 4;
	head1->next->next->next->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head1->next->next->next->next->val = 5;
	head1->next->next->next->next->next = NULL;
	assert(middleNode(head1)->val == 3);

	// Test case 2: Middle node of [1,2,3,4,5,6] is 4
	struct ListNode* head2 = (struct ListNode*) malloc(sizeof(struct ListNode));
	head2->val = 1;
	head2->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head2->next->val = 2;
	head2->next->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head2->next->next->val = 3;
	head2->next->next->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head2->next->next->next->val = 4;
	head2->next->next->next->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head2->next->next->next->next->val = 5;
	head2->next->next->next->next->next = (struct ListNode*) malloc(sizeof(struct ListNode));
	head2->next->next->next->next->next->val = 6;
	head2->next->next->next->next->next->next = NULL;
	assert(middleNode(head2)->val == 4);
}

struct ListNode* middleNode(struct ListNode* head) {
	int length = getlinkedlistlength(head);
	int i = 0;

	while (i != length / 2) {
		i++;
		head = head->next;
	}

	return head;
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

struct ListNode* middleNodeFast(struct ListNode* head) {
	struct ListNode *fast = head;
	struct ListNode *slow = head;

	while (fast != NULL && fast->next != NULL) {
		fast = fast->next->next;
		slow = slow->next;
	}

	return slow;
}
