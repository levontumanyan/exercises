/* You are given the head of a linked list.

Remove every node which has a node with a greater value anywhere to the right side of it.

Return the head of the modified linked list. */

#include <stdio.h>
#include <stdlib.h>

#include "../linkedlist.h"

struct ListNode* removeNodes(struct ListNode* head) {
	int size = 10;
	int num_of_elements = 0;
	int *nums = malloc(sizeof(int) * size);

	struct ListNode *current = head;
	while (current != NULL) {
		if (size <= num_of_elements) {
			size *= 2;
			nums = realloc(nums, size);
		}

		nums[num_of_elements] = current->val;
		current = current->next;
		num_of_elements++;
	}

	int max_so_far = 0;
	
	for (int i = 0; i < num_of_elements; i++) {
		if (max_so_far < nums[num_of_elements - i - 1]) {
			max_so_far = nums[num_of_elements - i - 1];
		}

		nums[num_of_elements - i - 1] = max_so_far;
	}

	int i = 0;
	current = head;
	struct ListNode *prev = NULL;

	while (current != NULL) {
		if (prev == NULL && current->val < nums[i]) {
			head = head->next;
		} else if (current->val < nums[i]) {
			prev->next = current->next;
		}

		if (current->val >= nums[i]) {
			prev = current;
		}
		i++;
		current = current->next;
	}

	return head;
}

void test_removeNodes() {
	// Test case 1
	struct ListNode* list1 = createlinkedlistfromarray((int[]){5, 2, 13, 3, 8}, 5);
	printlinkedlist(list1);
	printlinkedlist(removeNodes(list1));

	// Test case 3
	int arr3[] = {138,466,216,67,642,978,264,136,463,331,60,600,223,275,856,809,167,101,846,165,575,276,409,590,733,200,839,515,852,615,8,584,250,337,537,63,797,900,670,636,112,701,334,422,780,552,912,506,313,474,183,792,822,661,37,164,601,271,902,792,501,184,559,140,506,94,161,167,622,288,457,953,700,464,785,203,729,725,422,76,191,195,157,854,730,577,503,401,517,692,42,135,823,883,255,111,334,365,513,338,65,600,926,607,193,763,366,674,145,229,700,11,984,36,185,475,204,604,191,898,876,762,654,770,774,575,276,165,610,649,235,749,440,607,962,747,891,943,839,403,655,22,705,416,904,765,905,574,214,471,451,774,41,365,703,895,327,879,414,821,363,30,130,14,754,41,494,548,76,825,899,499,188,982,8,890,563,438,363,32,482,623,864,161,962,678,414,659,612,332,164,580,14,633,842,969,792,777,705,436,750,501,395,342,838,493,998,112,660,961,943,721,480,522,133,129,276,362,616,52,117,300,274,862,487,715,272,232,543,275,68,144,656,623,317,63,908,565,880,12,920,467,559,91,698};
	struct ListNode* list3 = createlinkedlistfromarray(arr3, sizeof(arr3) / sizeof(arr3[0]));
	printlinkedlist(list3);
	printf("Result: ");
	printlinkedlist(removeNodes(list3));	
}

int main() {
	test_removeNodes();
	return 0;
}
