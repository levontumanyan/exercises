#include "linkedlist.h"

void test_reverse_ll_iteratively() {
	int arr1[] = {2, 4, 1, 5, 100, 22, 10};
	struct ListNode *list1 = createlinkedlistfromarray(arr1, sizeof(arr1) / sizeof(arr1[0]));
	printlinkedlist(list1);
	printlinkedlist(reversell_iterative(list1));
}

int main() {
	test_reverse_ll_iteratively();
}
