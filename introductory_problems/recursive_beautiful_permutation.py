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

def beautiful_permutation(sequence):

	if len(sequence) == 1:
		return sequence
	
	if (len(sequence)) == 4:
		return [3, 1, 4, 2]
	
	if len(sequence) % 2 == 0:
		return beautiful_permutation(sequence[:-1]) + [sequence[-1]]
	else:
		return [sequence[-1]] + beautiful_permutation(sequence[:-1])

# print(beautiful_permutation([1, 2, 3, 4]))
# print(beautiful_permutation([1, 2, 3, 4, 5]))
# print(beautiful_permutation([1, 2, 3, 4, 5, 6]))
# print(beautiful_permutation([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# below is for the cses problem specifically

def permutation(length):
	if int(length) == 3 or int(length) == 2:
		return "NO SOLUTION"
	
	sequence = [ n for n in range(1, int(length) + 1)]
	result = beautiful_permutation(sequence)

	return " ".join([ str(num) for num in result ])

length = input()
print(permutation(length))