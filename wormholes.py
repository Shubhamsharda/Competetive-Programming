n,x,y = list(map(int, input().split()))
contests=[]
for i in range(0,n):
	s,e=list(map(int, input().split()))
	contests.append([s,e])
vtime=list(map(int, input().split()))
wtime=list(map(int, input().split()))

vtime.sort() #nlogn
wtime.sort() #nlogn
def func(x):
	return x[0]
sorted(contests,func) #nlogn
i=len(vtime)
j=0
min=0
while i>=0 or j<len(wtime):
	if vtime[i] < wtime[j]:
		for k in range(0,len(contests)):
			if contests[k][0] >= vtime[i]:
				if contests[k][1]<=wtime[j]:
					min=wtime[j]-vtime[i]
					break;
				else:
					
			else:
				
	else:
		i-=1
			
				

