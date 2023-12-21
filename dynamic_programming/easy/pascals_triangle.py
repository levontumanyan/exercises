"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

	1
   1 1
  1 2 1
 1 3 3 1
"""

def pascal(numRows):
	pascals_triangle = [[1], [1, 1]]

	for i in range(2, numRows):
		current_level = [1]*(i+1)
		for j in range(1, len(current_level) - 1):
			current_level[j] = pascals_triangle[i - 1][j - 1] + pascals_triangle[i - 1][j + 1]
		pascals_triangle.append(current_level)
	return pascals_triangle

#print(pascal(5))

def generate(numRows):
    if numRows == 0:
        return []
    elif numRows == 1:
        return [[1]]
    else:
        result = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
        return result

# Test the function
print(generate(5))
