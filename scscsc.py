
#import sys
from pptree import *	
inp = input().split()
n=int(inp[0])
k=int(inp[1])
lll=input().split()
ls=[int(i) for i in lll]
fstore={}
bstore={}
#sys.setrecursionlimit(3*n)
r1=Node('f('+str(k-1)+')')
r2=Node('f('+str(n-1)+')')
def forward(i,root):
	res=0
	if i==n-1:
		root.name=root.name+'='+str(ls[n-1])
		return ls[n-1]
	elif i==n-2:
		child=Node('f('+str(n-1)+')'+str(ls[n-1])+':',root)
		res=forward(n-1,child)
		root.name=root.name+'='+str(ls[n-2]+res)
		return ls[n-2]+res
	elif i in fstore:
		root.name=root.name+'='+str(res)
		res=fstore[i]
	else:
		child1=Node('f('+str(i+1)+')'+str(ls[i+1])+':',root)
		child2=Node('f('+str(i+2)+')'+str(ls[i+1])+':',root)
		fstore[i]=max(ls[i]+forward(i+1,child1),ls[i]+forward(i+2,child2))
		res=fstore[i]
		root.name=root.name+'='+str(res)
	return res
def back(j,root):
	if j==0:
		root.name=root.name+'='+str(ls[0])
		return ls[0]
	elif j==1:
		child=Node('f('+str(j-1)+'):',root)
		res=back(j-1,child)
		root.name=root.name+'='+str(ls[1]+res)
		return ls[1]+res
	elif j in bstore:
		root.name=root.name+'='+str(bstore[j])
		return bstore[j]
	else:
		child1=Node('f('+str(j-1)+')'+str(ls[j-1])+':',root)
		child2=Node('f('+str(j-2)+')'+str(ls[j-2])+':',root)
		bstore[j]= max(ls[j]+back(j-1,child1),ls[j]+back(j-2,child2))
		root.name=root.name+'='+str(bstore[j])
		return bstore[j]

a=forward(k-1,r1)-ls[k-1]
b=back(n-1,r2)-ls[n-1]
print('a:',a)
print('b:',b)
print_tree(r1)
print_tree(r2)