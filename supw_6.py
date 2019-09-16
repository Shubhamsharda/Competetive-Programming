
import sys
import time
start = time.time()

n = int(input().strip())
ls=list(map(int, input().strip().split()))
store=[[-3 for i in range(3)] for j in range(n)]

	
sys.setrecursionlimit(3*n)
def rec(ind,rest):
	
	if rest==3:

		return sys.maxsize
	elif ind==n:

		return 0

	elif store[ind][rest]!=-3:

		return store[ind][rest]
	else:

		store[ind][rest]=min(ls[ind]+rec(ind+1,0),rec(ind+1,rest+1))

		return store[ind][rest]
	

print(rec(0,0))
end=time.time()

print(end-start)
