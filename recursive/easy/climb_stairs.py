"""n = 3
1 1 1
2 1
1 2

n = 2
1 1
2

n = 1
1

n = 4

1 1 1 1
2 1 1
1 2 1
1 1 2
2 2

to climb n stairs - we can either climb it from n - 1 stair or n - 2
"""

def climbStairs(n: int) -> int:
	if n == 0 or n == 1:
		return 1
	
	return climbStairs(n - 1) + climbStairs(n - 2)

# memoized solution is in dynamic programming
