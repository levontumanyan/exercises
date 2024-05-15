/* You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure indicate the result:


Build the result list and return its head.

Example 1:
Input: list1 = [10,1,13,6,9,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [10,1,13,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue edges and nodes in the above figure indicate the result.
*/

#include <stdio.h>
#include "../linkedlist.h"

struct ListNode* mergeInBetween(struct ListNode* list1, int a, int b, struct ListNode* list2) {
	// Your code here
	struct ListNode *head = list1;

	for (int i = 0; i < a - 1; i++) {
		list1 = list1->next;
	}

	struct ListNode *first_pivot = list1;

	struct ListNode *to_free = list1->next;

	for (int i = 0; i < b - a + 2; i++) {
		list1 = list1->next;
	}

	struct ListNode *second_pivot = list1;

	struct ListNode *curr = to_free;
	
	while (curr != second_pivot) {
		struct ListNode *next = curr->next;
		free(curr);
		curr = next;
	}

	first_pivot->next = list2;

	while (list2->next != NULL) {
		list2 = list2->next;
	}

	list2->next = second_pivot;
	return head;
}

void test_mergeInBetween() {
	// Your test code here
	// Test case 1
	struct ListNode* list1 = createlinkedlistfromarray((int[]){10,1,13,6,9,5}, 6);
	struct ListNode* list2 = createlinkedlistfromarray((int[]){1000000,1000001,1000002}, 3);
	struct ListNode* expected1 = createlinkedlistfromarray((int[]){10,1,13,1000000,1000001,1000002,5}, 7);
	struct ListNode* result1 = mergeInBetween(list1, 3, 4, list2);
	printlinkedlist(result1);
	//assert(isEqual(result, expected));

	/* // Test case 1
	struct ListNode* list3 = createlinkedlistfromarray((int[]){0,1,2,3,4,5,6}, 7);
	struct ListNode* list4 = createlinkedlistfromarray((int[]){1000000,1000001,1000002,1000003,1000004}, 5);
	struct ListNode* result2 = mergeInBetween(list1, 2, 5, list2);
	printlinkedlist(result2); */
}

int main() {
	test_mergeInBetween();
	return 0;
}
