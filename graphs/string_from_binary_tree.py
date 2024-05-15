"""
Given the root of a binary tree, construct a string consisting of parenthesis and integers from a binary tree with the preorder traversal way, and return it.

Omit all the empty parenthesis pairs that do not affect the one-to-one mapping relationship between the string and the original binary tree.
"""

#Definition for a binary tree node.
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

def string_from_binary_tree(root):

	current_node = root

	while current_node.left or current_node.right:
		if current_node.left:
			current_node = current_node.left
			continue
		else:
			print(current_node.val)


root = TreeNode([1,2,3,4])
print(string_from_binary_tree(root))