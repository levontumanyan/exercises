"""
A permutation of integers 1,2, ... ,n is called beautiful if there are no adjacent elements whose difference is 1.
Given n, construct a beautiful permutation if such a permutation exists.
Input
The only input line contains an integer n.
Output
Print a beautiful permutation of integers 1,2,\ldots,n. If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".
Constraints

1 \le n \le 10^6

Example 1
Input:
5

Output:
4 2 5 3 1
Example 2
Input:
3

Output:
NO SOLUTION
"""

def beautiful_permutation(length):
	length = int(length)
	
	if length == 1:
		return 1
	
	if length < 4:
		return "NO SOLUTION"
	
	sequence = [ n for n in range(1, length + 1)]
	
	sequence_odd = [str(n) for n in sequence if n % 2 == 1]
	sequence_even = [str(n) for n in sequence if n % 2 == 0]

	return " ".join(sequence_even + sequence_odd)
	
# print(beautiful_permutation([1, 2, 3, 4]))
# print(beautiful_permutation([1, 2, 3, 4, 5]))
# print(beautiful_permutation([1, 2, 3, 4, 5, 6]))
# print(beautiful_permutation([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# below is for the cses problem specifically


length = input()

print(beautiful_permutation(length))
