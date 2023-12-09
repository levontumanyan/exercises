"""
def give_change(amount, coins):
Given the amount of money, expressed as the total number of kopecks of Latveria, Ruritania, Mon- tenegro or some other one of those such vaguely Slavic 6ictional countries that Tintin and similar hearty fellows like to visit for a wacky chase to grab the current year’s MacGuf6in, followed by the list of available denominations of coins also expressed as kopecks, this function should create and return a list of coins that add up to the amount using the greedy approach where you use as many of the highest denomination coins when possible before moving on to the next lower denomination. The list of coin denominations is guaranteed to be given in descending sorted order, as should your returned result also be.
amount
coins
Expected result
64
[50, 25, 10, 5, 1]
[50, 10, 1, 1, 1, 1]
123
[100, 25, 10, 5, 1]
[100, 10, 10, 1, 1, 1]
100
[42, 17, 11, 6, 1]
[42, 42, 11, 1, 1, 1, 1, 1]
"""

# def give_change(amount, coins):
# 	result = []
# 	current = 0
# 	for coin in coins:
# 		n = 0
# 		while True:
# 			if ((n+1)*coin <= amount):
# 				n += 1
# 			else:
# 				result.append(n*[coin])
# 				amount -= n*coin
# 				break
# 	flattened_list = [ item for sublist in result for item in sublist ]
# 	return flattened_list

def give_change(amount, coins):
	result = []
	current = 0
	for coin in coins:
		while coin <= amount:
				result.append(coin)
				amount -= coin
	return result


print(give_change(64, [50, 25, 10, 5, 1]))
print(give_change(123, [100, 25, 10, 5, 1]))
print(give_change(100,[42, 17, 11, 6, 1]))