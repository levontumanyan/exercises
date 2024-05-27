"""
def can_balance(items):
Each element in items is a positive integer, in this problem considered to be a physical weight. Your task is to 6ind a fulcrum position in this list of weights so that when balanced on that position, the total torque of the items to the left of that position equals the total torque of the items to the right of that position. The item on the fulcrum is assumed to be centered symmetrically on the ful- crum, and so does not participate in the torque calculation.
"""

def can_balance(items):
	current_index = 1

	while current_index < len(items):

		left_weights = items[:current_index]
		right_weights = items[current_index+1:]

		left_torque = 0
		right_torque = 0
	
		for i in range(len(left_weights)):
			left_torque += (current_index-i)*left_weights[i]

		for i in range(len(right_weights)):
			right_torque += (i+1)*right_weights[i]
		
		if (left_torque == right_torque):
			return current_index
		
		current_index += 1
	
	return -1

def can_balance(items):
    total_weight = sum(items)
    left_weight = 0

    for i in range(len(items)):
        total_weight -= items[i]
        if left_weight == total_weight:
            return i
        left_weight += items[i]

    return -1
			

print(can_balance([6, 1, 10, 5, 4, 0])) # ---> 2
print(can_balance([10, 3, 3, 2, 1])) # ---> 1
print(can_balance([7, 3, 4, 2, 9, 7, 4])) # ---> -1
print(can_balance([42])) # ---> 0
