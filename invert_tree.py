# invert a tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# class Solution:
	# def invertTree(self, root: TreeNode) -> TreeNode:
def invertTree(root) :
	def isleaf(n):
		if n.left is None and n.right is None:
			return True
		else:
			return False
	def func(node):
		if node is None:
			pass
		elif isleaf(node):
			pass
		else:
			temp=node.left
			node.left=node.right
			node.right=temp
			func(node.left)
			func(node.right)
	func(root)
	return root

t=TreeNode(1)
t.left=TreeNode(2)
t.right=TreeNode(3)
t.left.left=TreeNode(4)
t.left.right=TreeNode(5)
t1=invertTree(t)
print(t1.val)
print(t1.left.val)
print(t1.right.val)
print(t1.right.left.val)
print(t1.right.right.val)

	# t2=TreeNode(1)
	# t2.left=TreeNode(2)
	# t2.right=TreeNode(3)
	# # t2.left.left=TreeNode()
	# t2.left.right=TreeNode(5)
			
		