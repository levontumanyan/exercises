/* 
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself. 

* Definition for singly-linked list.
* struct ListNode {
*     int val;
*     struct ListNode *next;
* };

Medium

Topics
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
*/

#include <stdio.h>
#include <stdlib.h>

struct ListNode {
	int val;
	struct ListNode *next;
};

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
	if (l1->next == 0 || l2->next == 0) {
		return;
	}

	addTwoNumbers(l1->next, l2->next);
}

int *add_two_digits(int num1, int num2) {
	int *res = (int *) malloc(sizeof(int) * 2);
	
	if (num1 + num2 > 10) {
		res[0] = (num1 + num2) % 10;
		res[1] = (num1 + num2) / 10;
	}
	else {
		res[0] = num1 + num2;
		res[1] = 0;
	}

	return res;
}

int *add_two_digits_carry(int num1, int num2, int carry) {
	int *res = (int *) malloc(sizeof(int) * 2);
	
	if (num1 + num2 + carry > 10) {
		res[0] = (num1 + num2 + carry) % 10;
		res[1] = (num1 + num2 + carry) / 10;
	}
	else {
		res[0] = num1 + num2 + carry;
		res[1] = 0;
	}

	return res;
}

int main() {
	printf("Sum of 5 and 6 is: %d, carry is: %d\n", add_two_digits(5, 8)[0], add_two_digits(5, 8)[1]);
	printf("Sum of 5 and 6 and 4c is: %d, carry is: %d\n", add_two_digits_carry(5, 8, 1)[0], add_two_digits_carry(5, 8, 1)[1]);

}
