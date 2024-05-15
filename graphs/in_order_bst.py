"""

"""
class TreeNode:
	def __init__(self, val, right=None, left=None) -> None:
		self.val = val
		self.right = right
		self.left = left

def inorderTraversal(self, root):
	if root:
		if root.left:
			return [root.val] + self.inorderTraversal(root.left)
		else:
			return [root.val] + self.inorderTraversal(root.right)
	else:
		return None
