
#running median
import heapq


ls=[]
gres=[]
ntc=int(input())
while ntc > 0:
	ls1=[]
	ls2=[]
	heapq.heapify(ls1)
	heapq.heapify(ls2)
	i=int(input())
	while i!=0:
		res=[]
		if i != -1:
			if abs(len(ls1)-len(ls2))<=1:
				if i>(-1*heapq.heappop(ls1)) :
					heapq.heappush(ls2,i)
				else:
					heapq.heappush(ls1,-1*i)
			else:
				if len(ls1)>len(ls2):
					heapq.heappush(ls2,i)
				else:
					heapq.heappush(ls1,-1*i)
		else:
			ress=0
			if len(ls1) ==  len(ls2):
				ress=heapq.heapop(ls1)
			else:
				aa=heapq.heappop(ls1)
				bb=heapq.heappop(ls2)
				if aa>bb:
					ress=bb
				else:
					ress=aa
			res.append(ress)
	gres.append(res)
	
	print(grep)