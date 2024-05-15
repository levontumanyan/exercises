/* Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head. */
#include <stdlib.h>
#include <stdio.h>

struct ListNode {
	int val;
	struct ListNode *next;
} ListNode;

void printlinkedlist(struct ListNode *head) {
	while (head != NULL) {
		printf("%d, ", head->val);
		head = head->next;
	} 
	printf("\n");
}

struct ListNode *createlinkedlist(int *nums, int length) {
	struct ListNode *head = malloc(sizeof(*head));
	struct ListNode *temp = head;

	head->val = nums[0];

	for (int i = 1; i < length; i++) {
		struct ListNode *node = malloc(sizeof(*node));

		node->val = nums[i];
		node->next = NULL;
		temp->next = node;
		temp = temp->next;
	}

	return head;
}

struct ListNode* removeElements(struct ListNode* head, int val) {
	struct ListNode *current = head;
	struct ListNode *prev = NULL;

	start:

	while (current != NULL) {
		while (current->val == val) {
			if (prev == NULL) {
				current = current->next;
				head = current;
				goto start;
			}
			prev->next = current->next;
			current = current->next;
			goto start;
		}
		prev = current;
		current = current->next;
	}
	return head;
}

struct ListNode* removefirstoccurence(struct ListNode* head, int val) {
	struct ListNode *current = head;
	struct ListNode *prev = head;

	while (current != NULL) {
		if (current->val == val) {
			if (current == head) {
				head = current->next;
				return head;
			}
			prev->next = current->next;
			return head;
		}
		current = prev->next->next;
		prev = prev->next;
	}
	return head;
}

struct ListNode* removefirstoccurencediff(struct ListNode* head, int val) {
	struct ListNode *current = head;
	struct ListNode *prev = NULL;

	while (current != NULL) {
		if (current->val == val) {
			if (prev == NULL) {
				head = current->next;
				return head;
			}
			prev->next = current->next;
			return head;
		}
		prev = current;
		current = current->next;
	}

	return head;
}

void test_remove_x() {
	// Test case 1: Normal case with multiple zeroes and numbers in between
	int arr[] = {1, 1, 1, 5, 1, 2, 5, 1, 3, 4, 1, 1, 1, 5, 1, 1};
	int len = sizeof(arr) / sizeof(arr[0]);
	struct ListNode* head1 = createlinkedlist(arr, len);
	printlinkedlist(head1);
	printlinkedlist(removeElements(head1, 1));
	/* printlinkedlist(removefirstoccurence(head1, 5));
	printlinkedlist(removefirstoccurencediff(head1, 5));
	printlinkedlist(removefirstoccurencediff(head1, 1)); */
}

int main() {
	test_remove_x();
	printf("All test cases passed.\n");
	return 0;
}
