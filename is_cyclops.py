"""
def is_cyclops_v1(n):
A nonnegative integer is said to be a cyclops number if it consists of an odd number of digits so that the middle (more poetically, the “eye”) digit is a zero, and all the other digits of that number are non zero. This function should determine whether its parameter integer n is a cyclops number, and return either True or False accordingly.
0
True
101
True
98053
True
777888999
False
1056
False
675409820
False
"""

def is_cyclops_v1(n):
	digits = has_odd_digits(n)
	if not digits:
		return False
	else:
		power = (len(digits)-1)//2
		middle_digit = digits[(len(digits) - 1)//2]
		zeros = 0
		if middle_digit == 0:
			for digit in digits:
				if digit == 0:
					zeros += 1
			if zeros == 1:
				return True
			else:
				return False
		else:
			return False

def has_odd_digits(n):
	if n == 0:
		return [0]
	digits = []
	while n > 0:
		digits.append(n%10)
		n = n//10
	if len(digits) % 2 == 1:
		return digits
	else:
		return False
	
def is_cyclops_v2(n):
	string_n = str(n)
	zeros = 0
	if len(string_n) % 2 == 0:
		return False
	
	middle_element = string_n[len(string_n)//2]
	if (int(middle_element) != 0):
		return False

	for digit in string_n:
		if int(digit) == 0:
			zeros += 1
	
	if zeros == 1:
		return True
	else:
		return False

print("Version1")
print(is_cyclops_v1(0))
print(is_cyclops_v1(101))
print(is_cyclops_v1(98053))
print(is_cyclops_v1(777888999))
print(is_cyclops_v1(1056))
print(is_cyclops_v1(675409820))

print("Version2")
print(is_cyclops_v2(0))
print(is_cyclops_v2(101))
print(is_cyclops_v2(98053))
print(is_cyclops_v2(777888999))
print(is_cyclops_v2(1056))
print(is_cyclops_v2(675409820))

print("Version3")
print(is_cyclops_v3(0))
print(is_cyclops_v3(101))
print(is_cyclops_v3(98053))
print(is_cyclops_v3(777888999))
print(is_cyclops_v3(1056))
print(is_cyclops_v3(675409820))