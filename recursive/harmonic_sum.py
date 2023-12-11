

def harmonic_sum(k):

	if (k == 1):
		return 1

	return 1/k + harmonic_sum(k-1)


print(harmonic_sum(4))