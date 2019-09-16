import itertools
switch=False
def pr(*args):
	if switch==True:
		for i in args:
			print(i,end=' ')
		print()
def checkifleaf(node):
	if node.left is None and node.right is None:
		return True
	else:
		return False
def camp(p,q):
	if p is not None and q is not None:
		return p.val==q.val
	elif p is None and q is None:
		return True
	else:
		return False
def isSameTree(p, q):
# def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
	if camp(p,q):
		if p is not None and q is not None:
			if checkifleaf(p) and checkifleaf(q):
				return True
			elif not checkifleaf(p) and not checkifleaf(p):
				return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
			else:
				return False
		else:
			return True
	else:
		return False
	# if p is None and q is None:
		# return True
	# elif checkifleaf(p) and checkifleaf(q):
		# if p.val==q.val:
			# return True
	# elif p is not None and q is not None:
		# if checkifleaf(p) and checkifleaf(q):
			# if p.val==q.val:
				# return True
		# return isSameTree(p.left,q.left) and isSameTree(p.right,q.right) 

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t=TreeNode(1)
t.left=TreeNode(2)
t.right=TreeNode(3)
t.left.left=TreeNode(4)
t.left.right=TreeNode(5)

t2=TreeNode(1)
t2.left=TreeNode(2)
t2.right=TreeNode(3)
# t2.left.left=TreeNode()
t2.left.right=TreeNode(5)

print(isSameTree(t,t2))


