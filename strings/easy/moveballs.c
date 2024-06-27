/* You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes. */

#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// below is a n squared approach - slow
int *minOperations_slow(char *boxes, int *returnSize) {
	// Your code here
	int *answer = malloc(sizeof(int) * strlen(boxes));
	*returnSize = strlen(boxes);

	for (int i = 0; i < strlen(boxes); i++) {
		int score = 0;

		for (int j = 0; j < strlen(boxes); j++) {
			if (i == j) {
				continue;
			}

			if (boxes[j] == '1') {
				score += abs(j - i);
			}
		}
		answer[i] = score;
	}

	return answer;
}

int *minOperations(char *boxes, int *returnSize) {
	// Your code here
	int *answer = malloc(sizeof(int) * strlen(boxes));
	*returnSize = strlen(boxes);

	// count the initial stats
	int score = 0;
	int ones_total = 0;
	int ones_right = 0;
	int ones_left = 0;
	
	for (int i = 0; i < strlen(boxes); i++) {
		if (boxes[i] == '1') {
			ones_total += 1;
		}
	}

	for (int i = 1; i < strlen(boxes); i++) {
		if (boxes[i] == '1') {
			score += i;
		}
	}

	if (boxes[0] == '0') {
		ones_right = ones_total;
	}
	else if (boxes[0] == '1') {
		ones_right = ones_total - 1;
	}

	answer[0] = score;
	// 110
	// score starts: 1
	// ones_right = 
	for (int j = 1; j < strlen(boxes); j++) {
		if (boxes[j] == '1') {
			ones_right--;
			score--;
		}

		if (boxes[j - 1] == '1') {
			ones_left++;
		}

		score = score - ones_right + ones_left;
		answer[j] = score;
	}

	return answer;
}

void test_minOperations() {
    char boxes1[] = "1101";
	int returnsize = 4;
    int *answer1 = minOperations(boxes1, &returnsize);
    assert(answer1[0] == 4);
    assert(answer1[1] == 3);
    assert(answer1[2] == 4);
    assert(answer1[3] == 5);
    free(answer1);

    char boxes2[] = "001011";
	returnsize = 6;
    int *answer2 = minOperations(boxes2, &returnsize);
    assert(answer2[0] == 11);
    assert(answer2[1] == 8);
    assert(answer2[2] == 5);
    assert(answer2[3] == 4);
    assert(answer2[4] == 3);
    assert(answer2[5] == 4);
    free(answer2);

    printf("All tests passed!\n");
}

int main() {
	test_minOperations();
	return 0;
}
