"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

5 element - [1, 0, 1, 0, 1] - [0, 1, 0, 1, 0] - [1, 0, 1, 0, 1]
[0, 0, 0, 1, 0] - [0, 1, 0, 1, 0] - [1, 0, 0, 1, 0]
"""

def can_place_flowers(flowerbed, flowers_num):
	can_place = False
	can_plant = 0

	for spot in flowerbed:
		if can_place == True:
			can_plant += 1
			can_place = False
		if spot == 0:
			can_place = True
	return (flowers_num - can_plant) > 0

def can_place_flowers(flowerbed, flowers_num):
	
	if flowerbed[0] == 1 and len(flowerbed) % 2 == 1:
		spots = len(flowerbed) // 2 + 1
	else:
		spots = len(flowerbed) // 2
	
	can_place = spots - sum(flowerbed)
	return can_place >= flowers_num

print(can_place_flowers([1,0,0,0,1], 2))
print(can_place_flowers([1,0,0,0,1], 1))
print(can_place_flowers([1,0,0,0,0,1], 2))


# [1, 0, 0, 0, 0] - 5 // 2 + 1 max - 5 // 2 min
# 