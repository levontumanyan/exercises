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









struct ListNode *createlinkedlistdirect(int size) {
	
}



void printlinkedlist(struct ListNode *head) {
	while (head != NULL) {
		printf("%d, ", head->val);
		head = head->next;
	}
	printf("\n");
}

void printprevcur(struct ListNode *head) {
	struct ListNode *current = head->next;
	struct ListNode *prev = head;

	while (current != NULL && current->next != NULL) {
		printf("Previous: %d Current: %d / ", prev->val, current->val);
		prev = prev->next;
		current = current->next;
	}
}

void print2prevcur(struct ListNode *head) {
	struct ListNode *current = head;
	struct ListNode *prev = NULL;

	while (current != NULL && current->next != NULL) {
		prev = current;
		current = current->next;
		printf("Previous: %d Current: %d / ", prev->val, current->val);
	}
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
	printprevcur(test1);
	printf("\n\n\n");
	print2prevcur(test1);
}


