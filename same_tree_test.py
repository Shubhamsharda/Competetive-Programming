import itertools
switch=False
def pr(*args):
	if switch==True:
		for i in args:
			print(i,end=' ')
		print()
def isSameTree(p, q):
# def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
	if p is None and q is None:
		return True
	elif p is None and q is not None:
		return False
	elif p is not None and q is None:
		return False
	que1=[p]
	que2=[]
	a1=[q]
	a2=[]
	flag=False
	while(len(a1)>0 and len(que1)>0):
		# pr('debug')
		if flag==False:
			for (i,j) in zip(que1,a1):
				pr('i,j=',i.val,j.val)
				if i.val==j.val:
					if i.left is not None and j.left is not None and i.right is not None and j.right is not None:
						que2.append(i.left)
						que2.append(i.right)
						a2.append(j.left)
						a2.append(j.right)
						pr('debug 111')
					elif i.left is not None and j.left is not None :
						que2.append(i.left)
						a2.append(j.left)
						pr('debug 222')
						if i.right is not None and j.right is not None :
							que2.append(i.right)
							a2.append(j.right)
							pr('debug 333')
						elif i.right is  None and j.right is  None :
							pr('debug 777')
						else:
							flag= True
							break
					elif i.left is  None and j.left is  None :
						# que2.append(i.left)
						# a2.append(j.left)
						pr('debug 8888')
						if i.right is not None and j.right is not None :
							que2.append(i.right)
							a2.append(j.right)
							pr('debug 9999')
						elif i.right is  None and j.right is  None :
							pr('debug 555555')
						else:
							flag= True
							break
					elif i.left is  None and j.left is  None and i.right is  None and j.right is  None:
						pr('debug 444')
						# que1,que2,a1,a2=que2,[],a2,[]
						# break
						# pass
					else:
						pr('debug 555')
						# pr('p.left=',i.left.val,'p.right=',i.right.val,'q.left=',j.left.val,'q.right=',j.right.val)
						flag=True
						# que1,que2,a1,a2=que2,[],a2,[]
						break
				
				else:
					pr('debug 666')
					flag=True
					break
			que1,que2,a1,a2=que2,[],a2,[]	
				
		else:
			break
	pr('flag=',flag)
	if flag==True:
		return False
	else:
		return True

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

t=TreeNode(2)
# t.left=TreeNode(2)
t.right=TreeNode(4)
# t.left.left=TreeNode(4)
# t.left.right=TreeNode(5)

t2=TreeNode(2)
# t2.left=TreeNode(3)
t2.right=TreeNode(4)
# t2.left.left=TreeNode(4)
# t2.left.right=TreeNode(6)

print(isSameTree(t,t2))


