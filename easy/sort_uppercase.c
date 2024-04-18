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
void sort_uppercase_inplace(char *sentence[], int length);

int main() {
	char *sentence[] = {"Given", "a", "Sentence", "This", "problem", "the", "arrange", "is", "words"};
	char **result = sort_uppercase(sentence, 9);
	
	char *sentence1[] = {"Given", "a", "hello", "Sentence", "This", "problem", "the", "arrange", "Babo", "is", "words", "Akanj"};
	sort_uppercase_inplace(sentence, 9);
	sort_uppercase_inplace(sentence1, 12);

	for(int i = 0; i < 9; i++) {
		printf("%s\n", sentence1[i]);
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

void sort_uppercase_inplace(char *sentence[], int length) {
	for (int i = 0; i < length; i++) {
		for (int j = 0; j < length - 1; j++) {
			if (sentence[j][0] >= 'a' && sentence[j][0] <= 'z') {
				if (sentence[j + 1][0] >= 'A' && sentence[j + 1][0] <= 'Z') {
					char *temp = malloc(strlen(sentence[j + 1]) + 1);
					strcpy(temp, sentence[j + 1]);
					sentence[j + 1] = sentence[j];
					sentence[j] = temp;
				}
			}
		}
	}
}

/* 
{"Given", "a", "Sentence", "This", "problem", "the", "arrange", "is", "words"}; 

- {"Given", "a", "Sentence", "This", "problem", "the", "arrange", "is", "words"};
- {"Given", "a", "Sentence", "This", "problem", "the", "arrange", "is", "words"};

*/
