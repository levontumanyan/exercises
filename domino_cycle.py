"""A single domino tile is represented as a two-tuple of its pip values, such as (2,5) or (6,6). This function should determine whether the given list of tiles forms a cycle so that each tile in the list ends with the exact same pip value that its successor tile starts with, the successor of the last tile being the 6irst tile of the list since this is supposed to be a cycle instead of a chain. Return True if the given list of tiles forms such a cycle, and False otherwise."""

def domino_cycle(tiles):
	for i in range(len(tiles)):
		if i == len(tiles) - 1:
			if tiles[i][1] == tiles[0][0]:
				return True
			else:
				return False
		if (tiles[i][1] == tiles[i+1][0]):
			continue

		return False
	
print(domino_cycle([(3, 5), (5, 2), (2, 3)]))
print(domino_cycle([(4, 4)]))
print(domino_cycle([(2, 6)]))
print(domino_cycle([]))
print(domino_cycle([(4, 3), (3, 1)]))

