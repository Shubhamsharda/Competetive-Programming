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
r3.left.left=TreeNode(1)
# r3.left.left.left=TreeNode(1)
r4=TreeNode(1)
# r1.left.right.left=TreeNode(0)
r2=TreeNode(4)
r2.left=TreeNode(1)
r2.left=TreeNode(2)

class Solution:

	def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
		# if s and t:
			# if s.val==t.val:
				# print('d1')
				# res=self.issame(s,t) 
				# if res:
					# return True
				# else:
					# return self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
				# print('d2')
				# res= self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
				# return res
			# # return self.isSubtree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
		# elif s:
			# print('d3')
			# return False
		# elif t:
			# print('d4')
			# return False
		# else:
			# print('d5')
			# return True	
		return s is not None and self.issame(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)
	def issame(self,a,b):
		if a and b:
			return a.val==b.val and self.issame(a.left,b.left) and self.issame(a.right,a.right)
			# if a.val==b.val:
				# print('d6')
				# res= self.issame(a.left,b.left) and self.issame(a.right,b.right)
				# return res
			# else:
				# print('d7')
				# return False
		elif not a and not b:
			print('d8')
			return True
		else:
			print('d9')
			return False

a=Solution()

print(a.isSubtree(r3,r4))
# print(a.issame(r3.left.left.left,r4))
