"""
def count_dominators(items):
De6ine an element of a list of items to be a dominator if every element to its right (not just the one element that is immediately to its right) is strictly smaller than that element. Note how according to this de6inition, the last item of the list is automatically a dominator, regardless of its value. This func- tion should return the count of how many elements in items are dominators. For example, the dominators of the list [42, 7, 12, 9, 13, 5] would be 42, 13 and 5. Regardless of its value, the last element of the list is trivially a dominator, since nothing greater follows it in the list.
Before starting to write code for this function, you should consult the parable of “Shlemiel the painter” and think how this seemingly silly tale from a simpler time relates to today’s computational problems performed on lists, strings and other sequences. This problem will be the 6irst of many that you will encounter during and after this course to illustrate the important principle of using only one loop to achieve in a tiny fraction of time the same end result that Shlemiel achieves with two nested loops. Your workload therefore increases only linearly with respect to the number of items, whereas the total time of Shlemiel’s back-and-forth grows quadratically, that is, as a func- tion of the square of the number of items.
Trying to hide the inner loop of some Shlemiel algorithm inside a function call (this includes Python built-ins such as max and list slicing) and pretending that this somehow makes those inner loops take a constant time will only summon the Gods of Compubook Headings to return with tumult to claim their lion’s share of execution time.
"""

def count_dominators_v1(items):
	dominators = [items[len(items) - 1]]
	for i in range(len(items)-1):
		count = 0
		for value in items[i+1:]:
			if items[i] > value:
				count += 1
			else:
				break
			if count == len(items[i+1:]):
				dominators.append(items[i])
	return len(dominators)


print(count_dominators_v1(range(10**7, 0, -1)))
print(count_dominators_v1([42, 7, 12, 9, 2, 5]))


def count_dominators_v2(items):
	current_max = float('-inf')
	count = 0
	reversed_items = reversed(items)
	for item in reversed_items:
		if item > current_max:
			count += 1
			current_max = item
	return count

print(count_dominators_v2(range(10**7, 0, -1)))
print(count_dominators_v2([42, 7, 12, 9, 2, 5]))

def count_dominators_v3(items):
	dominators = [items[-1]]

	for i in range(len(items) - 2, -1, -1):
		if (items[i] > dominators[-1]):
			dominators.append(items[i])
	return len(dominators)

print(count_dominators_v3([42, 7, 12, 9, 2, 5]))
print(count_dominators_v3(range(10**7, 0, -1)))