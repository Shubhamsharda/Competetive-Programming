
import sys



n = int(input().strip())
ls=list(map(int, input().strip().split()))
store=[[-3 for i in range(2)] for j in range(n)]
store2=[[-3 for i in range(2)] for j in range(n)]


	
sys.setrecursionlimit(3*n)

def rec(ind,rest):
	if rest==2:

		return sys.maxsize
	elif ind==n:
		# if rest=1:
			# return 0
		# else:
			# return 

		return 0
	elif store[ind][rest]!=-3:

		return store[ind][rest]
	else:


		store[ind][rest]=min(ls[ind]+rec(ind+1,0),rec(ind+1,rest+1))

		return store[ind][rest]
		
def rec2(ind,rest):
	if rest==2:

		return sys.maxsize
	elif ind==n:
		if rest==1:
			
			return sys.maxsize
		elif(rest==0):
			
			return 0 

		return 0
	elif store2[ind][rest]!=-3:

		return store2[ind][rest]
	else:


		store2[ind][rest]=min(ls[ind]+rec2(ind+1,0),rec2(ind+1,rest+1))

		return store2[ind][rest]
		
result1=rec(0,0)
result2=rec2(0,0)
print(min(result1,result2))
