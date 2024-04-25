#include <stdlib.h>
#include "linkedlist.h"
#include <stdio.h>

void printlinkedlist(struct ListNode *head) {
	struct ListNode *current = head;

	while (current != NULL) {
		if (current->next == NULL) {
			printf("%d ", current->val);
		}
		else {
			printf("%d -> ", current->val);
		}
		current = current->next;
	}
	printf("\n");
}

struct ListNode *createlinkedlistfromarray(int arr[], int size) {
	if (size == 0) {
		return NULL;
	}
	
	struct ListNode *head = malloc(sizeof(*head));
	struct ListNode *node = head;

	for (int i = 0; i < size; i++) {
		node->val = arr[i];
		if (i == size - 1) {
			node->next = NULL;
		}
		else {
			node->next = malloc(sizeof(*node));
		}
		node = node->next;
	}

	return head;
}
