#include <stdlib.h>
#include <assert.h>

/**
 * struct Node - a structure for linked list node
 * @data: integer data in the node
 * @next: pointer to the next node
*/

typedef struct Node {
	int data;
	struct Node *next;
} Node;

/**
 * createLinkedListFromArray - function to create a linked list from an array
 * @arr: array of integers
 * @size: size of the array
 *
 * Return: pointer to the head of the linked list
*/

Node *createlinkedlistfromarray(int nums[], int size) {
	if (size == 0) {
		return NULL;
	}
	
	Node *head = malloc(sizeof(*head));
	Node *curr = head;
	head->data = nums[0];
	head->next = NULL;

	for (int i = 1; i < size; i++) {
		Node *node = malloc(sizeof(*node));

		curr->next = node;
		node->data = nums[i];

		curr = curr->next;
	}

	return head;
}

Node *createlinkedlistfromarraycompact(int nums[], int size) {
	if (size == 0) {
		return NULL;
	}

	Node *head = malloc(sizeof(*head));
	Node *node = head;

	for (int i = 0; i < size; i++) {
		node->data = nums[i];
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

void test_createLinkedListFromArray() {
	// Test case 1: Normal case
	int arr1[] = {1, 2, 3, 4, 5};
	Node* head1 = createlinkedlistfromarray(arr1, 5);
	assert(head1->data == 1);
	assert(head1->next->data == 2);
	assert(head1->next->next->data == 3);
	assert(head1->next->next->next->data == 4);
	assert(head1->next->next->next->next->data == 5);
	assert(head1->next->next->next->next->next == NULL);

	// Test case 2: Empty array
	int arr2[] = {};
	Node* head2 = createlinkedlistfromarray(arr2, 0);
	assert(head2 == NULL);

	// Test case 3: Single element array
	int arr3[] = {10};
	Node* head3 = createlinkedlistfromarray(arr3, 1);
	assert(head3->data == 10);
	assert(head3->next == NULL);

	// Test case 4: Normal case compact
	int arr4[] = {1, 2, 3, 4, 5};
	Node* head4 = createlinkedlistfromarraycompact(arr1, 5);
	assert(head4->data == 1);
	assert(head4->next->data == 2);
	assert(head4->next->next->data == 3);
	assert(head4->next->next->next->data == 4);
	assert(head4->next->next->next->next->data == 5);
	assert(head4->next->next->next->next->next == NULL);
}

int main() {
	test_createLinkedListFromArray();
	return 0;
}
