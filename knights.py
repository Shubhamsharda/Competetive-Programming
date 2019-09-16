from pptree import *
import sys
import time
start = time.time()

n = int(input().strip())
ls=list(map(int, input().strip().split()))
store=[[-3 for i in range(2)] for j in range(n)]
store2=[[-3 for i in range(2)] for j in range(n)]
root44=Node('f('+str(0)+')')
root55=Node('f('+str(0)+')')
result=[]
	
sys.setrecursionlimit(3*n)

def rec(ind,rest,root):
	if rest==2:
		root.name=root.name+'='+str(sys.maxsize)
		return sys.maxsize
	elif ind==n:
		# if rest=1:
			# return 0
		# else:
			# return 
		root.name=root.name+'='+str(0)
		return 0
	elif store[ind][rest]!=-3:
		root.name=root.name+'='+str(store[ind][rest])
		return store[ind][rest]
	else:
		child1=Node('f('+str(ind+1)+','+str(0)+')',root)
		child2=Node('f('+str(ind+1)+','+str(rest+1)+')',root)
		store[ind][rest]=min(ls[ind]+rec(ind+1,0,child1),rec(ind+1,rest+1,child2))
		#a=ls[ind]+rec(ind+1,0,child1)
		#b=rec(ind+1,rest+1,child2)
		
		root.name=root.name+'='+str(store[ind][rest])
		return store[ind][rest]
		
def f(ind,rest,root2):
	if rest==2:
		root2.name=root2.name+'='+str(sys.maxsize)
		return sys.maxsize
	elif ind==n:
		if rest==1:
			root2.name=root2.name+'='+str(sys.maxsize)
			print('indnjds',str(ind),str(rest))
			return sys.maxsize
		elif(rest==0):
			print('indnjds',str(ind),str(rest))
			root2.name=root2.name+'='+str(0)
			return 0
		
	elif store2[ind][rest]!=-3:
		root2.name=root2.name+'='+str(store2[ind][rest])
		return store2[ind][rest]
	else:
		child1=Node('f('+str(ind+1)+','+str(0)+')',root2)
		child2=Node('f('+str(ind+1)+','+str(rest+1)+')',root2)
		store2[ind][rest]=min(ls[ind]+f(ind+1,0,child1),f(ind+1,rest+1,child2))
		#a=ls[ind]+rec(ind+1,0,child1)
		#b=rec(ind+1,rest+1,child2)
		
		root2.name=root2.name+'='+str(store2[ind][rest])
		return store2[ind][rest]
		
rec(0,0,root44)
print_tree(root44)
f(0,0,root55)
#print_tree(root44)
#print('f')
print_tree(root55)