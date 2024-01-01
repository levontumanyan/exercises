def find_k_beauty(num, current_num, k):
	if current_num < pow(10,k):
		return int(num % current_num == 0)

	# new num is num % 10^k
	try:
		if num % (current_num % pow(10,k)) == 0:
			return 1 + find_k_beauty(num, current_num // 10, k)
	except:
		return find_k_beauty(num, current_num // 10, k)

	return find_k_beauty(num, current_num // 10, k)
