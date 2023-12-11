def sum_of_digits(num):
	if (num < 10):
		return num
	
	return num % 10 + sum_of_digits(num // 10)


print(sum_of_digits(12312))
print(sum_of_digits(0))
print(sum_of_digits(5))
print(sum_of_digits(24))
