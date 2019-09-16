
#import sys
from binarytree import tree
from binarytree import Node
import time
start = time.time()


n = int(input().strip())
ls=list(map(int, input().strip().split()))
store=[[-3 for i in range(3)] for j in range(n)]
#sys.setrecursionlimit(3*n)
root=Node(0.0)
root2=Node(0)
result=[]
#lll=input().strip().split()
#ls=[int(i) for i in lll]


def qq(ind,rest,result):
	print('returning ',result,' for',' rec(',ind,rest,')','')
def pq(ind,rest):
	a=ind+1
	b=rest+1
	print('calls rec(',a,',0) and calls rec(',a,',',b,')')
	
def p(ind,rest):
	print('ind,rest: ',ind,rest,store)
def nn(ind,rest):
	a=ind+1
	b=rest+1
	return 'rec(',a,',0)'
def jj(ind,rest):
	a=ind+1
	b=rest+1
	return 'rec(',a,',',b,')'
#def rr(ind,rest):
	
#sys.setrecursionlimit(3*n)
def rec(ind,rest,root,root2):
	
	if rest==3:
		#p(ind,rest)
		qq(ind,rest,999)
		root2.value=999
		return 999
	elif ind==n:
		#p(ind,rest)
		qq(ind,rest,0)
		root2.value=0
		return 0
	#result=-10
	elif store[ind][rest]!=-3:
		p(ind,rest)
		qq(ind,rest,store[ind][rest])
		print('already calculated value for rec(',ind,rest,')',store[ind][rest])
		root2.value=store[ind][rest]
		return store[ind][rest]
	else:
		pq(ind,rest)
		#root.left=Node(root.value+1)
		root.left=Node((ind+1)+1.0-1.0)
		root2.left=Node(1000)
		root2.right=Node(1000)
		#root.right=Node(root.value+2)
		root.right=Node((ind+1) + ((rest+1)*0.1))
		a=ls[ind]+rec(ind+1,0,root.left,root2.left)
		b=rec(ind+1,rest+1,root.right,root2.right)
		if (a<b):
			store[ind][rest]=a
			print('selected index is: ',ind)
			result.append(ind)
		else:
			store[ind][rest]=b
			
		#store[ind][rest]=min(ls[ind]+rec(ind+1,0,root.left,root2.left),rec(ind+1,rest+1,root.right,root2.right))
		#p(ind,rest)
		qq(ind,rest,store[ind][rest])
		#root.value=root.value+(store[ind][rest]*0.01)
		root2.value=store[ind][rest]
		#print(root)
		#print(root2)
		return store[ind][rest]
	

print(rec(0,0,root,root2))
print(root)
print(root2)

print(ls)
end = time.time()
print(str(end - start)+'s')