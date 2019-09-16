
n=int(input())
ls=[]
for i in range(n):
	tmp=[]
	for j in range(n):
		tmp.append(input())
	ls.append(tmp)
i=0
j=0
store={}
def paths(i,j):
	if i==n-1 and j==n-1:
		return 1
	elif i>n-1 or j>n-1:
		return 0
	elif (i,j) in store:
		return store[(i,j)]
	else:
		store[(i,j)]=paths(i+1,j) + paths(i,j+1)
		return store[(i,j)]

print(paths(0,0))