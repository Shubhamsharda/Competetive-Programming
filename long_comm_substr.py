

A='qwertyuiopshardaaqwert'
B='zxcvbshardaazxcv'
from pptree import *

r=Node('f(0,0)')
count={}
def long(i,j,root):
	if i>=aa-1 or j>=bb-1:
		return 0
	elif (i,j) in count:
		return count[(i,j)]
	elif A[i+1]==B[j+1]:
		child=Node('f('+str(i)+','+str(j)+')',root)
		res=1+ long(i+1,j+1,child)
		root.name+=':'+str(res)
		return res
	else:
		child1=Node('f('+str(i+1)+','+str(j)+')',root)
		child2=Node('f('+str(i)+','+str(j+1)+')',root)
		a=long(i+1,j,child1)
		b=long(i,j+1,child2)
		count[(i,j)]=max(a,b)
		root.name+=':'+str(count[(i,j)])
		return count[(i,j)]

aa= len(A)
bb=len(B)
print(long(0,0,r))
#print_tree(r)