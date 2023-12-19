from matplotlib import pyplot as plt
# Solve fibonacci by iteration, no looping
# Fib(1) = 1, Fib(2) = 2
fib = {1 : 1, 2 : 1}

def fibonacci(num):
	for i in range(3, num + 1):
		fib[i] = fib[i-1] + fib[i-2]
	return fib[num]

for k in range(1, 100):
	print(f"{k}: {fibonacci(k)}")

x = [x for x in fib.keys()]
y = [y for y in fib.values()]

plt.plot(x, y, 'o-', label='fibonaccinear')
#plt.ylim(0, 218922995834)
plt.xlabel('n-th fibonacci number')
plt.ylabel('Value')
plt.title('Not at all Linear Plot')
plt.legend()
plt.show()
