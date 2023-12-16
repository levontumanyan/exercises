"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

Can't use recursion or looping

Idea here is that every power of two in binary representation is: 10000

2 = 10
4 = 100
8 = 1000
16 = 10000

10000
and
00000
00000

1000
and
1000

1000
xor
0001
1001 = num + 1

1000
+
1000

1000
0000

1000
and
1111
1000


1000
and
0111
0000

1000
-
0001
0111

1000
0111
and
0

1100
-
0001
0011


"""

def is_power_of_two(num):
	if num != 0 and num & (num - 1) == 0:
		return True
	else:
		return False
	
print(is_power_of_two(8))
print(is_power_of_two(16))
print(is_power_of_two(2))
print(is_power_of_two(1))
print(is_power_of_two(15))
print(is_power_of_two(13))
print(is_power_of_two(0))
