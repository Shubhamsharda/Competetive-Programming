
import sys
inp = input().split()
n=int(inp[0])
k=int(inp[1])
lll=input().split()
ls=[int(i) for i in lll]
fstore={}
bstore={}
sys.setrecursionlimit(3*n)
def forward(i):
	res=0
	if i==n-1:
		return ls[n-1]
	elif i==n-2:
		return ls[n-2]+forward(i+1)
	elif i in fstore:
		res=fstore[i]
	else:
		fstore[i]=max(ls[i]+forward(i+1),ls[i]+forward(i+2))
		res=fstore[i]
	return res
def back(j):
	if j==0:
		return ls[0]
	elif j==1:
		return ls[1]+back(j-1)
	elif j in bstore:
		return bstore[j]
	else:
		bstore[j]= max(ls[j]+back(j-1),ls[j]+back(j-2))
		return bstore[j]

a=forward(k-1)-ls[k-1]
b=back(n-1)-ls[n-1]
# print('a:',a)
# print('b:',b)
print(a+b)