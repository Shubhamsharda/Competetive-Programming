
import sys


n = int(input())
lll=input().split()
ls=[int(i) for i in lll]
#ls=list(map(int, input().strip().split()))
store={}
store2={}

	
sys.setrecursionlimit(3*n)


def rec2(x):
	#print('x is :',x)
	if x==n-1:
		
		return sys.maxsize
	elif x==n:
		
		return 0
		
	try:
		
		return store2[x]
	except:
		res=min(rec2(x+1)+ls[x],rec2(x+2)+ls[x+1])
		store2[x]=res
		#a=ls[ind]+rec(ind+1,0,child1)
		#b=rec(ind+1,rest+1,child2)
		
		
		return store2[x]
		
def rec(x):
	#print('x is :',x)
	if x>=n-1:
		return 0
	if x in store:
		return store[x]
	else:
		res=min(rec(x+1)+ls[x],rec(x+2)+ls[x+1])
		store[x]=res
		#a=ls[ind]+rec(ind+1,0,child1)
		#b=rec(ind+1,rest+1,child2)
		return store[x]
res1=rec(0)
res2=rec2(1)
print(min(res1,res2+ls[0]))

