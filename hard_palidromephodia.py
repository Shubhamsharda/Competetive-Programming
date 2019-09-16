# Abiohphobia

import sys
import random
import string

def func(i,len):
	j=i+len
	print('j: ',j)
	if i==j:
		return 0
	elif abs(i-j) == 1 and s[i]==s[j]:
		return 0
	elif (i,len) in store:
		return store[(i,len)]
	elif s[i]==s[j]:
		print('1')
		return func(i+1,len-2)
	else:
		print('2')
		store[(i,len)]=min(1+func(i+1,len-1),1+func(i,len-1))
		return store[(i,len)]

n=int(input())
s=str(input())
# s='dcddcdcscc'
if len(s)>10:
	sys.setrecursionlimit(3*len(s))

store={}
a=0
b=len(s)-1
	# print('called for func(',a,',',b,')')
print(func(a,len(s)-1))
	# print('store is :',store)
# for i in range(1,10000):
	# s = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(i)])
	# store={}
	# a=0
	# b=len(s)-1
	# print('s: ',s,'i: ',a,'j: ',b)
	# print(func(a,b))
