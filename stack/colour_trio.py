"""
def colour_trio(colours):
This problem was inspired by the Mathologer video “Secret of Row 10”. To start, assume the exis- tence of three values called “red”, “yellow” and “blue”. These names serve as colourful (heh) mnemonics and could as well have been 0, 1, and 2, or “foo”, “bar” and “baz”; no connection to actual physical colours is implied. Next, de6ine a rule to mix such colours so that mixing any colour with itself gives that same colour, whereas mixing any two different colours always gives the third colour. For example, mixing blue to blue gives that same blue, whereas mixing blue to yellow gives red, same as mixing yellow to blue, or red to red.
Given the 6irst row of colours as a string of lowercase letters, this function should construct the rows below the 6irst row one row at the time according to the following discipline. Each row is one element shorter than the previous row. The i:th element of each row comes from mixing the colours in positions i and i + 1 of the previous row. Rinse and repeat until only the singleton element of the bottom row remains, returned as the 6inal answer. For example, starting from 'rybyr' leads to 'brrb', which leads to 'yry', which leads to 'bb', which leads to 'b' for the 6inal answer, Regis. When the Python virtual machine laughs and goes 'brrrrr', that will lead to 'yrrrr', 'brrr', 'yrr', and 'br' for the 6inal answer 'y' for “Yes, please!”
"""

def mix_colors(color1, color2):
	colors = [ 'r', 'y', 'b']

	if color1 == color2:
		return color1
	else:
		colors.remove(color1)
		colors.remove(color2)
		return colors.pop()

def color_trio(colors):
	while len(colors) > 1:
		next_colors = [None] * (len(colors) - 1)
		for i in range(len(next_colors)):
			next_colors[i] = mix_colors(colors[i], colors[i+1])
		colors = next_colors
	return next_colors

print(color_trio('y'))
print(color_trio('bb'))
print(color_trio('rybyry'))
print(color_trio('rbyryrrbyrbb'))
print(color_trio('yrbbbbryyrybb'))
