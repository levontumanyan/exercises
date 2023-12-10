"""
Decimal to Binary: Write a recursive function that takes a positive integer n and prints its binary representation.

13 --- 13 % 2 = 1
13 // 2 = 6

"""

def decimal_to_binary(num):
	if num == 0 or num == 1:
		print(num, end="")
		return

	decimal_to_binary(num // 2)
	print(num % 2, end ="")	

print(decimal_to_binary(8))
print(decimal_to_binary(13))
