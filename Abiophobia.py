# Abiohphobia

import sys

def func(i,j,s):
	if i==j:
		return 0
	elif abs(i-j) == 1 and s[i]==s[j]:
		return 0
	elif (i,j) in store:
		return store[(i,j)]
	elif s[i]==s[j]:
		return func(i+1,j-1,s)
	else: 
		store[(i,j)]=min(1+func(i+1,j,s),1+func(i,j-1,s))
		return store[(i,j)]

t=int(input())
strings=[]
for i in range(t):
	inp=str(input())
	strings.append(inp)
sys.setrecursionlimit(3*len(strings[0]))
for i in range(t):
	store={}
	a=0
	b=len(strings[i])-1
	# print('called for func(',a,',',b,')')
	print(func(a,b,strings[i]))
	# print('store is :',store)
