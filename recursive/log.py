# Recursive function to find the logarithm of n. For example log(100) = 2

def log(n):
	if (n == 1):
		return 0
	
	return 1 + log(n // 10)
	

print(log(1000))
print(log(100))
print(log(1))
print(log(10))
print(log(1500))

