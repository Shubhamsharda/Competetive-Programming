
from pptree import *
import sys
def f(i):
	if i==0:
		# print('f(',i,'): ',1)
		return 1
	elif i in dp:
		# print('f(',i,'): ',dp[i])
		return dp[i]
	else:
		j=i-1
		while(j>=0):
			if abs(ls[j]) < abs(ls[i]) and (( ls[i]>0 and ls[j]<0 ) or (ls[i]<0 and ls[j]>0)) :
				dp[i]=max(f(j),1+f(j))
				# print('f(',i,'): ',dp[i])
				return dp[i]
			else:
				j-=1
		# print('f(',i,'): ',1)
		return 1


dp={}
n=int(input())
if n!=1:
	sys.setrecursionlimit(n*n)
ls=input().split()
ls=[int(i) for i in ls]
k=n-1
maxx=0

while(k>=0):
	# print('k: ',k)
	# root=Node('f(',k,'): ')
	res=f(k)
	# root.value+=str(res)
	if res>maxx:
		maxx=res
	k-=1
	# print(dp)
print(maxx)
