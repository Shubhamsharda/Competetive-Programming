
import heapq
n=int(input())
inp=input().split()
ls=[int(j) for j in inp]
ls2=[k for k in range(1,n+1)]


# res=[]
# for j in range(n):
	# # print(ls2)
	# heap=[]
	# for i in range(n):
		# heapq.heappush(heap,-1*( ls[i]+ls2[i]))
	# # res.append(-1*heapq.heappop(heap))
	# print(str(-1*heapq.heappop(heap))+' ',end='')
	# # ls2=ls2[j+1:] + ls2[:j+1]
	# a=ls2[0]
	# ls2=ls2[1:]
	# ls2.append(a)
	# print('j=',j)
# for i in res:
	# print(str(i)+' ',end='')
	
res=[ls[i-1]+i for i in range(1,n+1)]
print(res)
localmax=[]
for i in range(len(res)):
	print('i=',i)
	if i==0:
		if res[i]>res[i+1]:
			localmax.append(res[i])
	elif i==len(res)-1:
		if res[i]>res[i-1]:
			localmax.append(res[i])	
	else:
		if res[i]>res[i-1] and res[i]>res[i+1]:
			localmax.append(res[i])
print(localmax)
	