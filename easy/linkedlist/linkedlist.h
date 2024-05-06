struct ListNode {
	int val;
	struct ListNode *next;
} ListNode;

void printlinkedlist(struct ListNode *head);
struct ListNode *createlinkedlistfromarray(int arr[], int size);
struct ListNode *appendlists(struct ListNode *head1, struct ListNode *head2);
