/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
*/

#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

struct ListNode {
	int val;
	struct ListNode *next;
} ListNode;

// return true if cycle exists, otherwise false
bool hasCycle(struct ListNode *head) {
	int list_size = 100;
	struct ListNode **items = malloc(list_size * sizeof(struct ListNode *));
	int size = 0;
	struct ListNode *current = head;

	while (current != NULL) {
		for (int i = 0; i < size; i++) {
			if (items[i] == current) {
				return true;
			}
		}
		if (size >= list_size) {
			list_size *= 2;
			items = realloc(items ,list_size * sizeof(struct ListNode *));
		}
		items[size] = current;
		size++;
		current = current->next;
	}

	return false;
}

int main() {
	// Test case 1: An empty list
	struct ListNode *head = NULL;
	printf("Test case 1: %s\n", hasCycle(head) ? "true" : "false"); // Expected output: false

	// Test case 2: A list with one node and no cycle
	head = malloc(sizeof(struct ListNode));
	head->val = 1;
	head->next = NULL;
	printf("Test case 2: %s\n", hasCycle(head) ? "true" : "false"); // Expected output: false

	// Test case 3: A list with one node that points to itself
	head->next = head;
	printf("Test case 3: %s\n", hasCycle(head) ? "true" : "false"); // Expected output: true

	// Test case 4: A list with multiple nodes and no cycle
	struct ListNode *node2 = malloc(sizeof(struct ListNode));
	node2->val = 2;
	node2->next = NULL;
	head->next = node2;
	printf("Test case 4: %s\n", hasCycle(head) ? "true" : "false"); // Expected output: false

	// Test case 5: A list with multiple nodes and a cycle
	struct ListNode *node3 = malloc(sizeof(struct ListNode));
	node3->val = 3;
	node3->next = head;
	node2->next = node3;
	printf("Test case 5: %s\n", hasCycle(head) ? "true" : "false"); // Expected output: true

	return 0;
}
