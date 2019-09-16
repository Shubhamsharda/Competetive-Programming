
import sys
import heapq

def runningMedian(a):
	res=[]
	h=[]
	heapq.heapify(h)
	hls=[]
	for i in range(len(a)):
		heapq.heappush(h,a[i])
		
		hls=list(h)
		print('heap:',hls)
		if i%2==0:
			mid=(0+i)//2
			res.append(float(hls[mid]))
		else:
			mid=(0+i)//2
			res.append(float((hls[mid]+hls[mid+1])/2))
	return res

a=[10,4,6,8,3,1]	
print(runningMedian(a))
