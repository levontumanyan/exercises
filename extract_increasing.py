"""
def extract_increasing(digits):
Given a string of digits guaranteed to only contain ordinary integer digit characters 0 to 9, create and return the list of increasing integers acquired from reading these digits in order from left to right. The 6irst integer in the result list is made up from the 6irst digit of the string. After that, each element is an integer that consists of as many following consecutive digits as are needed to make that integer strictly larger than the previous integer. The leftover digits at the end of the digit string that do not form a suf6iciently large integer are ignored.
This problem can be solved with a for-loop through the digits that looks at each digit exactly once regardless of the position of that digit in the beginning, end or middle of the string. Keep track of the current number (initially zero) and the previous number to beat (initially equal to minus one). Each digit d is then processed by pinning it at the end of current number with the assignment current=10*current+int(d), updating the result and previous as needed.
"""

def extract_increasing(digits):
	result = [int(digits[0])]

	for i in range(1, len(digits)):
		for j in range(i+1, len(digits)):
			if (int(digits[i:j]) > result[-1]):
				result.append(int(digits[i:j]))
				break
	
	return result

print(extract_increasing('045349'))
print(extract_increasing('77777777777777777777777'))

def extract_increasing_v2(digits):
	result = []
	current = 0
	previous = -1
	for digit in digits:
		current = 10*current + int(digit)

		if (current > previous):
			result.append(current)
			previous = current
			current = 0
	return result


print(extract_increasing_v2('045349'))
print(extract_increasing_v2('77777777777777777777777'))
