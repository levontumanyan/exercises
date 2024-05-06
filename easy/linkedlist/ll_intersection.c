/* Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:

The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns. */

#include "linkedlist.h"

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

struct ListNode *getIntersectionNode(struct ListNode *headA, struct ListNode *headB) {
	size_t size = 10;
	struct ListNode **nodes1 = malloc(sizeof(*nodes1) * size);
	struct ListNode **nodes2 = malloc(sizeof(*nodes1) * size);
	int i = 0;

	while (headA != NULL) {
		if (i >= size) {
			size *= 2;
			struct ListNode **temp = realloc(nodes1, sizeof(*nodes1) * size);
			if (temp == NULL) {
				printf("Failed to allocate memory.\n");
				free(nodes1);
				return NULL;
			}
			nodes1 = temp;
		}
		nodes1[i] = headA;
		i++;	
		headA = headA->next;
	}

	size = 10;
	int j = 0;
	while (headB != NULL) {
		if (j >= size) {
			size *= 2;
			struct ListNode **temp = realloc(nodes2, sizeof(*nodes1) * size);
			if (temp == NULL) {
				printf("Failed to allocate memory.\n");
				free(nodes2);
				return(NULL);
			}
			nodes2 = temp;
		}
		nodes2[j] = headB;
		headB = headB->next;
		j++;
	}

	for (int k = 0; k < i; k++) {
		for (int l = 0; l < j; l++) {
			if (nodes1[k] == nodes2[l]) {
				return nodes1[k];
			}
		}
	}
	return NULL;
}

void test_getIntersectionNode() {
	// Test case 1: Intersection exists
	struct ListNode *shared = createlinkedlistfromarray((int[]){8, 4, 5}, 3);
	struct ListNode *headA1 = appendlists(createlinkedlistfromarray((int[]){4, 1}, 2), shared);
	struct ListNode *headB1 = appendlists(createlinkedlistfromarray((int[]){5, 0, 1}, 3), shared);
	assert(getIntersectionNode(headA1, headB1) == shared);

	// Test case 2: No intersection
	struct ListNode *headA2 = createlinkedlistfromarray((int[]){2, 6, 4}, 3);
	struct ListNode *headB2 = createlinkedlistfromarray((int[]){1, 5}, 2);
	assert(getIntersectionNode(headA2, headB2) == NULL);
}

int main() {
	test_getIntersectionNode();
	return 0;
}
