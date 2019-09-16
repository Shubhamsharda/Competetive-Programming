
#rent

import sys	
def f(ls,i,prev):
	print('called: ',ls,i,prev)
	def findnext(ii,end,p):
		origi=ii
		ind=i+1
		mid=(ii+end)//2
		while((ii-end)>=1 or end-ii >=1):
			# print(ii,end)
			if ls[mid][0]>ls[p][1] and mid>ind:
				ind=mid
				end=mid-1
			else:
				ii=mid+1
			mid=(ii+end)//2
		return ind
	def findnext(ii,end,p):
		res=ii+1
		for i in range(end):
			if ls[p][1]<ls[i][0]:
				if 
	if (i,prev) in store:
		# print('store accessed')
		return store[i,prev]
	elif i==len(ls):
		# print('end this')
		return 0
	else:
		
		if prev is not None:
			# print('1')
			a=findnext(i,len(ls)-1,prev)
			b=findnext(i,len(ls)-1,i)
			print('for ',i,' b is ',b)
			print('for ',prev,' a is ',a)
			# print('a:',a)
			if a>i:
				if ls[i][0]>=ls[prev][1]:
					store[(i,prev)]=max(ls[i][2]+f(ls,b,i),f(ls,a,prev))
				else:
					
					store[(i,prev)]=f(ls,a,prev)
				return store[(i,prev)]
		else:
			# print('2')
			store[(i,prev)]=max(ls[i][2]+f(ls,i+1,i),f(ls,i+1,prev))
			return store[(i,prev)]
	
t=int(input())
res=[]
for i in range(t):
	n=int(input())
	l1=[]
	for j in range(n):
		inp=input().split(' ')
		l2=[int(k) for k in inp]
		l1.append(l2)
	def sortfirst(val): 
		return val[0]
	l1.sort(key=sortfirst)
	store={}
	# print(l1)
	res.append(f(l1,0,None))
for i in res:
	print(i)