#https://leetcode.com/problems/subtree-of-another-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
r1=TreeNode(3)
r1.left=TreeNode(4)
r1.right=TreeNode(5)
r1.left.left=TreeNode(1)
r1.left.right=TreeNode(2)

r3=TreeNode(1)
r3.left=TreeNode(1)
r4=TreeNode(1)
# r1.left.right.left=TreeNode(0)
r2=TreeNode(4)
r2.left=TreeNode(1)
r2.right=TreeNode(2)
switch=2
def pr(*args):
	if switch==2:
		for i in args:
			print(i,end=' ')
		print()
def issame(a,b):
	if a and b:
		if a.val==b.val:
			pr('d3')
			res= issame(a.left,b.left) and issame(a.right,b.right)
			pr('issame(',a.val,',',b.val,')=',res)
			return res
		else:
			pr('d4')
			pr('issame(',a.val,',',b.val,')=',False)
			return False
	elif not a and not b:
		pr('d1')
		return True
	else:
		pr('d2')
		return False

# def isSubtree(s, t):
	# if s and t:
		# if s.val==t.val:
			# return isSubtree(s.left,t.left) and isSubtree(s.right,t.right)
		# else:
			# return isSubtree(s.left,t)
	# if not s not t:
		# return True
	# else:
		# return False
def isSubtree(s,t):
	if s and t:
		if s.val==t.val:
			pr('d5')
			res=issame(s,t) or issame(s.left,t) or issame(s.right,t)
			pr('isSubtree(',s.val,',',t.val,')=',res)
			return res
		else:
			pr('d6')
			res= isSubtree(s.left,t) or isSubtree(s.right,t)
			pr('isSubtree(',s.val,',',t.val,')=',res)
			return res
	elif s:
		pr('d7')
		pr('isSubtree(',s.val,',',None,')')
		return False
	elif t:
		pr('d8')
		pr('isSubtree(',None,',',t.val,')')
		return False
	else:
		pr('d9')
		pr('isSubtree(',None,',',None,')')
		return True	
print(isSubtree(r3,r4))
# print(issame(r3.left,r4))