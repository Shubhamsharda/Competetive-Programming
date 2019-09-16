from pptree import *
import sys
import time
start = time.time()

n = int(input().strip())
ls=list(map(int, input().strip().split()))
store={}
store2={}
print('store is :',store	)
root44=Node('f('+str(0)+')')
root55=Node('f('+str(0)+')')
result=[]
	
sys.setrecursionlimit(3*n)
print('n is ',n)
print('ls is: ',ls)
def rec2(x,root):
	#print('x is :',x)
	if x==n-1:
		root.name=root.name+'+'+str(ls[x-1])+'='+str(sys.maxsize)
		return sys.maxsize
	elif x==n:
		root.name=root.name+'+'+str(ls[x-1])+'='+str(0)
		return 0
		
	try:
		root.name=root.name+'+'+str(ls[x-1])+'='+str(store2[x])
		return store2[x]
	except:
		child1=Node('f('+str(x+1)+')',root)
		child2=Node('f('+str(x+2)+')',root)
		print('x is : ',x)
		print('ls[x],ls[x+1]: ',ls[x],ls[x+1])
		
		res=min(rec2(x+1,child1)+ls[x],rec2(x+2,child2)+ls[x+1])
		store2[x]=res
		#a=ls[ind]+rec(ind+1,0,child1)
		#b=rec(ind+1,rest+1,child2)
		
		root.name=root.name+'+'+str(ls[x-1])+'='+str(store2[x])
		return store2[x]
		
def rec(x,root):
	#print('x is :',x)
	if x>=n-1:
		root.name=root.name+'+'+str(ls[x-1])+'='+str(0)
		return 0
		
	try:
		root.name=root.name+'+'+str(ls[x-1])+'='+str(store[x])
		return store[x]
	except:
		child1=Node('f('+str(x+1)+')',root)
		child2=Node('f('+str(x+2)+')',root)
		print('x is : ',x)
		print('ls[x],ls[x+1]: ',ls[x],ls[x+1])
		
		res=min(rec(x+1,child1)+ls[x],rec(x+2,child2)+ls[x+1])
		store[x]=res
		#a=ls[ind]+rec(ind+1,0,child1)
		#b=rec(ind+1,rest+1,child2)
		
		root.name=root.name+'+'+str(ls[x-1])+'='+str(store[x])
		return store[x]
		
		
print('Result including last is: ',rec(0,root44))
print('Result including first is: ',ls[0]+rec2(1,root55))
print_tree(root44)
print(store)
print_tree(root55)
print(store2)
#f(0,0,root55)
#print_tree(root44)
#print('f')
#print_tree(root55)