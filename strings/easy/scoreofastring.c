/* You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s. */

#include <stdio.h>
#include <math.h>

int scoreOfString(char *s) {
	// Your code here
	int score = 0;
	int i = 0;

	while (s[i + 1] != '\0') {
		score += abs(s[i] - s[i + 1]);
		i++;
	}
	
	return score;
}

void test_scoreOfString() {
	// Your test code here
}

int main() {
	test_scoreOfString();
	return 0;
}
