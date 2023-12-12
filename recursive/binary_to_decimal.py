def binary_to_decimal(binary):
	if (len(binary) == 0):
		return 0
	
	return int(binary[0]) * 2 ** (len(binary) - 1) + binary_to_decimal(binary[1:])

print(binary_to_decimal("1000"))
print(binary_to_decimal("1010110111"))
print(binary_to_decimal("10001"))
