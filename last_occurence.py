# given an array of integers and a target value. find the last occurence of the target
# nvidia interview question: December 11, 2023

def last_occurence(numbers, target):
	for i in range(len(numbers) - 1, 0, -1 ):
		if (numbers[i] == target):
			return i
		
print(last_occurence([1, 2, 5, 2, 6, 7, 2], 2))

