/* 
You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.

For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.

Return the head of the modified linked list.
*/

#include "../../easy/linkedlist/linkedlist.h"

#include <assert.h>
#include <stdlib.h>
#include <stdio.h>

struct ListNode* mergeNodeswithzeroes(struct ListNode* head) {
	int count = 0;

	struct ListNode *initialhead = head;
	struct ListNode *lastzero_node = head;
	head = head->next;

	while (head != NULL) {
		if (head->val == 0) {
			struct ListNode *node = malloc(sizeof(*node));
			node->val = count;
			lastzero_node->next = node;
			node->next = head;
			lastzero_node = head;
			count = 0;
		}
		else {
			count += head->val;
		}

		head = head->next;
	}
	return initialhead;
}

struct ListNode *mergeNodes(struct ListNode *head) {
	struct ListNode *slow = head;
	struct ListNode *fast = head->next;

	int sum = 0;

	while (fast != NULL) {
		sum += fast->val;

		if (fast->val == 0 && fast->next == NULL) {
			slow->val = sum;
			slow->next = NULL;
		}
		else if (fast->val == 0) {
			slow->val = sum;
			slow->next = fast;
			slow = fast;
			sum = 0;
		}
		fast = fast->next;
	}

	return head;
}

void test_merge_nodes_between_zeroes() {
	// Test case 1: Normal case with multiple zeroes and numbers in between
	int arr[] = {0, 3, 1, 0, 4, 5, 2, 0};
	int len = sizeof(arr) / sizeof(arr[0]);
	struct ListNode* head1 = createlinkedlistfromarray(arr, len);
	printlinkedlist(head1);
	printlinkedlist(mergeNodes(head1));
	//assert(compareLinkedLists(result1, [3, 7]));
}

int main() {
	test_merge_nodes_between_zeroes();
	printf("All test cases passed.\n");
	return 0;
}
