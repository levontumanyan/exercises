

# array of ints, last occurence of a number

def last_element(numbers, target):

	for i in range(len(numbers), 0, -1):
		if (numbers[i] == target):
			return i
		
