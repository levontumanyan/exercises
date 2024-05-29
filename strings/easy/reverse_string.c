/* Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
*/

#include <stdio.h>

// 

void reverseString(char *s, int sSize) {
	// Your code here
	int i = 0;

	while (i != (sSize / 2)) {
		int swap = s[i];
		s[i] = s[sSize - i - 1];
		s[sSize - i - 1] = swap;
		i++;
	}

}

void test_reverseString() {
    char test1[] = "hello";
    reverseString(test1, 5);
    printf("%s\n", test1); // Expected output: "olleh"

    char test2[] = "world";
    reverseString(test2, 5);
    printf("%s\n", test2); // Expected output: "dlrow"

    char test3[] = "Github Copilot";
    reverseString(test3, 15);
    printf("%s\n", test3); // Expected output: "tolipoC buhtiG"

    char test4[] = "1234567890";
    reverseString(test4, 10);
    printf("%s\n", test4); // Expected output: "0987654321"

    char test5[] = "A";
    reverseString(test5, 1);
    printf("%s\n", test5); // Expected output: "A"

	char test6[] = "helsi moto";
    reverseString(test6, 10);
    printf("%s\n", test6); // Expected output: "tolipoC buhtiG"
}

int main() {
	test_reverseString();
	return 0;
}
