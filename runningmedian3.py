

# Running median hackerrank
# https://www.hackerrank.com/challenges/find-the-running-median/problem

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
		
		# print('maxheap, minheap: ',maxheap,minheap)
		if len(maxheap) > len(minheap):
			res.append(float(-1*maxheap[0]))
		elif len(maxheap) < len(minheap):
			res.append(float(minheap[0]))
		else:
			res.append(float((minheap[0] + -1*maxheap[0])/2))
		median=res[-1]
		# print('---end of loop--')
	return res

print(runningMedian([12,4,5,3,8,7]))