/* 
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.
*/

#include <string.h>

int minOperations(char** logs, int logsSize) {
	int min_ops = 0;
	const char *move_parent = "../";
	const char *remain = "./";
	//char *change_dir = "../";


	for (int i = 0; i < logsSize; i++) {
		if (strcmp(logs[i], move_parent) == 0) {
			if (min_ops == 0) {
				continue;
			}
			else {
				min_ops -= 1;
			}
		}
		else if(strcmp(logs[i], remain) == 0) {
			continue;
		}
		else {
			min_ops += 1;
		}
	}
	return min_ops;
}
