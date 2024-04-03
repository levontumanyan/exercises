#include <stdlib.h>
#include <string.h>
#include <stdio.h>

char *mergeAlternately(char *word1, char *word2);

int main() {
	char *word1 = "abc";
	char *word2 = "pqrtb";
	char *merged1 = mergeAlternately(word1, word2);
	printf("%s\n", merged1);
	char *wor1 = "abcd";
	char *wor2 = "ef";
	char *merged2 = mergeAlternately(wor1, wor2);
	printf("%s\n", merged2);
}


char *mergeAlternately(char *word1, char *word2){
	int merged_length = strlen(word1) + strlen(word2);
	char *result = malloc((merged_length + 1)*sizeof(char));

	int word1p = 0;
	int word2p = 0;

	while (word1p + word2p < merged_length) {
		if (word1p < strlen(word1)) {
			result[word1p + word2p] = word1[word1p];
			word1p++;
		}

		if (word2p < strlen(word2)) {
			result[word1p + word2p] = word2[word2p];
			word2p++;
		}
	}

	result[merged_length + 1] = '\0';

	return result;
}
