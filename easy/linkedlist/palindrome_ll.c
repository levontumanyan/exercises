#include <stdio.h>
#include <stdbool.h>
#include <assert.h>

#include "linkedlist.h"

// Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

bool isPalindrome(struct ListNode* head) {
	struct ListNode *middle = head;
	struct ListNode *fast = head;

	while (fast != NULL && fast->next != NULL) {
		middle = middle->next;
		fast = fast->next->next;
	}

	struct ListNode *first_half = head;
	struct ListNode *second_half = reversell_iterative(middle);

	while (first_half != NULL && second_half != NULL) {
		if (first_half->val != second_half->val) {
			return false;
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}

	return true;
}

void test_isPalindrome() {
	// Test case 1: Palindrome list
	struct ListNode *head1 = createlinkedlistfromarray((int[]){1, 2, 3, 2, 1}, 5);
	assert(isPalindrome(head1) == true);

	// Test case 2: Not a palindrome list
	struct ListNode *head2 = createlinkedlistfromarray((int[]){1, 2, 3, 4, 5}, 5);
	assert(isPalindrome(head2) == false);

	// Test case 3: Single element list (always a palindrome)
	struct ListNode *head3 = createlinkedlistfromarray((int[]){1}, 1);
	assert(isPalindrome(head3) == true);

	// Test case 4: Even number of items
	struct ListNode *head4 = createlinkedlistfromarray((int[]){1,2,2,1}, 4);
	assert(isPalindrome(head4) == true);

	// Test case 5: Empty list (always a palindrome)
	struct ListNode *head5 = createlinkedlistfromarray((int[]){}, 0);
	assert(isPalindrome(head5) == true);

	// Test case 6: Two items
	struct ListNode *head6 = createlinkedlistfromarray((int[]){1, 2}, 2);
	assert(isPalindrome(head6) == false);

	// Test case 7: Even number of items
	struct ListNode *head7 = createlinkedlistfromarray((int[]){1,5,2,1}, 4);
	assert(isPalindrome(head7) == false);
}

int main() {
	test_isPalindrome();
	return 0;
}
