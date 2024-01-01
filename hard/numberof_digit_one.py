def countDigitOne(num):
	ans = 0
	m = num
	dig = []
	i = 0

	while num > 0:
		dig.append(num % 10)
		num = num//10
		i += 1

	for i in range(len(dig) - 1, -1, -1):
		while dig[i] > 2:
			ans += i*pow(10,i-1)
			dig[i] -= 1
			m -= pow(10,i)

		if (dig[i] == 2):
			ans += 2*i*pow(10,i-1) + pow(10,i)
			dig[i] = 0
			m -= 2*pow(10,i)

		if (dig[i] == 1):
			ans += m - pow(10,i) + i*pow(10,i-1) + 1
			m -= pow(10,i)
			dig[i] -= 1
	return int(ans)

print(countDigitOne(13))