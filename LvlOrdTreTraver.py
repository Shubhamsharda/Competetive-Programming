# Definition for a binary tree node.
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

def levelOrder(root):
	def func(a):
		# print('func(',a,')')
		if len(a)==0:
			return
		r=[]
		for i in a:
			if i.left is not None:
				r.append(i.left)
			if i.right is not None:
				r.append(i.right)
		# print(r)
		if len(r)!=0:
			rr=[j.val for j in r]
			res.append(rr)
		if len(r)!=0:
			func(r)
	func([root])
	print(res)

root= TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
root.left.left=TreeNode(4)
root.left.right=TreeNode(5)
res=[[root.val]]
levelOrder(root)   
# print('res:',res)