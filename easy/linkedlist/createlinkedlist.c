#include <stdio.h>
#include <stdlib.h>

struct ListNode {
	int val;
	struct ListNode *next;
} ListNode;

void add_element(struct ListNode *head, int val) {
	struct ListNode *node = malloc(sizeof(struct ListNode *));
	node->next = NULL;
	node->val = val;

	while (head->next != NULL) {
		head = head->next;
	}

	head->next = node;
}

struct ListNode *createlinkedlist(int size) {
	struct ListNode *head = malloc(sizeof(struct ListNode *));
	
	for (int i = 0; i < size; i++) {
		add_element(head, i);
	}

	return head;
}

void printlinkedlist(struct ListNode *head) {
	while (head != NULL) {
		printf("%d, ", head->val);
		head = head->next;
	}
	printf("\n");
}

int main() {
	struct ListNode *head = malloc(sizeof(struct ListNode *));
	head->val = 12;
	add_element(head, 15);
	add_element(head, 23);
	add_element(head, 1);
	add_element(head, 105);
	add_element(head, 18);
	printlinkedlist(head);

	struct ListNode *test1 = createlinkedlist(15);
	printlinkedlist(test1);
}


