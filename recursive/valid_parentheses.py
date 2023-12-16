"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def valid_parentheses(input_str):

	if len(input_str) % 2 == 1:
		return False
	
	if len(input_str) == 0:
		return True
	
	if input_str[0] == "(":
		return input_str[-1] == ")" and valid_parentheses(input_str[1:-1])
	
	if input_str[0] == "[":
		return input_str[-1] == "]" and valid_parentheses(input_str[1:-1])
	
	if input_str[0] == "{":
		return input_str[-1] == "}" and valid_parentheses(input_str[1:-1])

print(valid_parentheses("(())"))
print(valid_parentheses("(()))"))
print(valid_parentheses("(()))"))
print(valid_parentheses(")"))
print(valid_parentheses("([{{[]}}])"))
