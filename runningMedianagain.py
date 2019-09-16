

# Running median again
# https://www.spoj.com/problems/RMID2/

import heapq

def runningMedian(a):
	# switch=True
	maxheap=[]
	minheap=[]
	heapq.heapify(maxheap)
	heapq.heapify(minheap)
	res=[]
	# print('a: ',a)
	
	median=0
	for i in range(len(a)): 
		# print(res)
		# print('median',median)
		if a[i]!=-1:
			if a[i] > median:
				heapq.heappush(minheap,a[i])
				# heapq.heapify(minheap)
			else:
				heapq.heappush(maxheap,-1*a[i])
				# heapq.heapify(maxheap)
			if (len(maxheap)> len(minheap)+1):
				heapq.heappush(minheap,-1*heapq.heappop(maxheap))
			if (len(minheap)> len(maxheap)+1):
				heapq.heappush(maxheap,-1*heapq.heappop(minheap))
				
				
			if len(maxheap) > len(minheap):
				median=float(-1*maxheap[0])
			elif len(maxheap) < len(minheap):
				median=float(minheap[0])
			else:
				median=float(-1*maxheap[0])
			
			# print('maxheap, minheap: ',maxheap,minheap)
			
			# print('---end of loop--')
		else:
			if len(maxheap) > len(minheap):
				res.append(float(-1*heapq.heappop(maxheap)))
			elif(len(maxheap) < len(minheap)):
				res.append(float(heapq.heappop(minheap)))
			else:
				res.append(float(-1*heapq.heappop(maxheap)))
	return res

arr=[]
temp=int(input())
i=0
while(temp):
	arr.append(temp)
	temp=int(input())
	i+=1



print(runningMedian(arr))