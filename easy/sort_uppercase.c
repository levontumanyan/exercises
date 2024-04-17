/* 
Given a sentence, arrange words starting with upper case letters first and then lower case in the same order that they appear

["hello", "Bye", "Yellow", "Geeeee", "Petty", "tree"]

["hello", "Bye", "Yellow", "Geeeee", "Petty", "tree"]

Problem Statement: Arrange Words

You are given an array of words representing a sentence. Your task is to rearrange the words such that all words starting with an uppercase letter appear before words starting with a lowercase letter. Maintain the original order of words within each group.

Write a function arrangeWords(sentence: List[str]) -> List[str] to accomplish this.

Input:
sentence: A list of strings representing the words in the sentence. Each word consists of alphabetic characters only.
Output: Return a list of strings representing the rearranged sentence according to the specified rules.

Constraints:

The sentence may contain punctuation, but it should be treated as part of the words.
Example:

sentence = ["Given", "a", "Sentence", "This", "problem", "the", "arrange", "is", "words"]
arrangeWords(sentence) ➞ ["Given", "Sentence", "This", "arrange", "Sentence", "This", "problem", "the", "is", "words"]
Explanation:
The words starting with uppercase letters are "Given", "Sentence", "This", and "Sentence". The words starting with lowercase letters are "a", "problem", "arrange", "is", and "words". The rearranged sentence maintains the original order of words within each group.

This problem statement outlines the task clearly, along with input/output specifications and constraints.

Attempt: go through the array, and create two new arrays. First will be the position of the capital letter starting words in the original sentence, the other the lowercase ones.

then add the lowercase letter array to the capital letter array
*/
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char **sort_uppercase(char *sentence[], int length);

int main() {
	char *sentence[] = {"Given", "a", "Sentence", "This", "problem", "the", "arrange", "is", "words"};
	char **result = sort_uppercase(sentence, 9);

	for(int i = 0; i < 9; i++) {
		printf("%s\n", result[i]);
	}
}

char **sort_uppercase(char *sentence[], int length) {
	int *capitals = malloc(sizeof(int) * length);
	int *lowercase = malloc(sizeof(int) * length);
	char **result = malloc(sizeof(char *) * length);
	
	int uppercase_index = 0;
	int lowercase_index = 0;

	for (int i = 0; i < length; i++) {
		if (sentence[i][0] >= 'A' && sentence[i][0] <= 'Z') {
			capitals[uppercase_index] = i;
			uppercase_index++;
		}
		else if (sentence[i][0] >= 'a' && sentence[i][0] <= 'z') {
			lowercase[lowercase_index] = i;
			lowercase_index++;
		}
	}

	for (int i = 0; i < uppercase_index; i++) {
		result[i] = malloc(strlen(sentence[capitals[i]]) + 1);
		strcpy(result[i], sentence[capitals[i]]);
	}

	for (int i = 0; i < lowercase_index; i++) {
		result[i + uppercase_index] = malloc(strlen(sentence[lowercase[i]]) + 1);
		strcpy(result[i + uppercase_index], sentence[lowercase[i]]);
	}

	return result;
}

// [0, 1, 2]

/* 
["hello", "Bye", "Yellow", "Geeeee", "Petty", "tree"]
capital - [ 1, 2, 3, 4]
lowercase - [0, 5]

uppercase_index - 4
lowercase_index - 2

for (int i = 0; i < uppercase_index + 1; i++) {
	strcpy(result[i], sentence[capitals[i]]);
}

i: 0 - 4
result[0] <-- sentence[1]
result[1] <-- sentence[2]
result[2] <-- sentence[3]
result[3] <-- sentence[4]

for (int i = 0; i < lowercase_index + 1; i++) {
	strcpy(result[i + lowercase_index], sentence[capitals[i]]);
}

i: 0 - 2
result[4] <-- sentence[]

*/
