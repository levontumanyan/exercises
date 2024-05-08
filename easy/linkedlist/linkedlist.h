#ifndef LINKEDLIST_H
#define LINKEDLIST_H

#include <stdlib.h>

struct ListNode {
	int val;
	struct ListNode *next;
} ListNode;

void printlinkedlist(struct ListNode *head);
struct ListNode *createlinkedlistfromarray(int arr[], int size);
struct ListNode *appendlists(struct ListNode *head1, struct ListNode *head2);
size_t get_ll_length(struct ListNode *head);
struct ListNode *reverse_ll(struct ListNode *head);

#endif
