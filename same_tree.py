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
class Solution:
	def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
		def func(p,q):
			if camp(p,q):
				if p is not None and q is not None:
					if checkifleaf(p) and checkifleaf(q):
						return True
					elif not checkifleaf(p) and not checkifleaf(p):
						return func(p.left,q.left) and func(p.right,q.right)
					else:
						return False
				else:
					return True
			else:
				return False
		return func(p,q)