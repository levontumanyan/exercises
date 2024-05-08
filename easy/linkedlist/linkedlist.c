#include <stdlib.h>
#include <stdio.h>
#include "linkedlist.h"

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

struct ListNode *appendlists(struct ListNode *head1, struct ListNode *head2) {
	if (head1 == NULL && head2 == NULL) {
		return NULL;
	}

	if (head2 == NULL) {
		return head1;
	}

	if (head1 == NULL) {
		return head2;
	}

	struct ListNode *current = head1;

	while (current->next != NULL) {
		current = current->next;
	}

	current->next = head2;

	return head1;
}

size_t get_ll_length(struct ListNode *head) {
	size_t i = 0;

	while (head != NULL) {
		head = head->next;
		i++;
	}

	return i;
}

struct ListNode *reverse_ll(struct ListNode *head) {
	if (head == NULL || head->next == NULL) {
		return head;
	}

	struct ListNode* rest = reversell_recursive(head->next);
	head->next->next = head;
	head->next = NULL;
	return rest;
}
