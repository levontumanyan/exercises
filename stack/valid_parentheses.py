"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""

def valid_parentheses(input_str):

	# idea is we create a stack
	# not valid examples: ({))
	# valid examples: ((())), ({[]})
	# lets do for just regular brackets first

	stack = []

	for ch in input_str:
		if ch in ["(", "[", "{"]:
			stack.append(ch)
		if len(stack) == 0:
			return False
		elif ch == ")":
			if (stack.pop() == "("):
				pass
			else:
				return False
		elif ch == "]":
			if (stack.pop() == "["):
				pass
			else:
				return False
		elif ch == "}":
			if (stack.pop() == "{"):
				pass
			else:
				return False
	
	if len(stack) != 0:
		return False

	return True

def valid_parentheses(input_str):

	# if len(input_str) % 2 != 0:
	# 	return False
	stack = []

	brackets = { "(" : ")", "{" : "}", "[": "]" }
	opening_brackets = set(["(", "[", "{"])

	for ch in input_str:
		if ch in opening_brackets:
			stack.append(ch)
		elif stack and ch == brackets[stack[-1]]:
			stack.pop()
		else:
			return False

	return stack == []

print(valid_parentheses("("))	
print(valid_parentheses("(]"))	
print(valid_parentheses("()"))
print(valid_parentheses("())"))
print(valid_parentheses("((((()))))"))
print(valid_parentheses("[((((()))))]"))
print(valid_parentheses("[]]"))
print(valid_parentheses("[]])"))
print(valid_parentheses("[]])"))
print(valid_parentheses("{{{[(([]))]}}}"))
print(valid_parentheses("{]}"))
