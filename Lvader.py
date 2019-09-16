
#10^9 + 7
import math
from sys import stdin, stdout	
	
def f(i,j,k,s):
	if i==k and j==s:
		return 1
	elif i>k or j>s:
		return 0
	elif (i,j) in store:
		return store[(i,j)]
	else:
		store[(i,j)]= f(i+1,j,k,s) + f(i,j+1,k,s) +f(i+1,j+1,k,s)
		return store[(i,j)]





t=int(input())
# t=int(stdin.readline())
ls=[]
for i in range(t):
	inp=list(map(int, input().split()))
	# inp=raw_input().split()
	# inp=stdin.readline().split() 
	# l=[int(j) for j in inp]
	# ls.append(inp)
	store={}
	res= f(inp[0],inp[1],inp[2],inp[3])
	ls.append(res%(pow(10,9) +7))





for i in ls:
	print(i)
	