
#highway bypass
import sys

inp=input().split()
r=int(inp[0])
c=int(inp[1])
d=int(inp[2])

if r>3 and c>3:
	sys.setrecursionlimit(r*c)
ls=[]
# store=[]
# for i in range(r):
	# a1=[]
	# for j in range(c):
		# a2=[]
		# for k in range(d):
			# a3=[]
			# for l in range(2):
				# a3.append(-4)
			# a2.append(a3)
		# a1.append(a2)
	# store.append(a1)

# print(store)
store={}
		
for i in range(r):
	io=input().split()
	lss=[int(j) for j in io]
	ls.append(lss)
# print(ls)

def f(a,b,step,dir):
	if a>r-1 or b>c-1 or ls[a][b]==0:
		return 0
	elif a==r-1 and b==c-1:
		return 1
	elif (a,b,step,dir) in store:
		return store[(a,b,step,dir)]
	else:
		x=0
		if dir=='right':
			if step<d:
				x=(x+f(a,b+1,step+1,'right'))%20011
			x=(x+f(a+1,b,1,'down'))%20011
			store[(a,b,step,dir)]=x
		else:
			if step<d:
				x=(x+f(a+1,b,step+1,'down'))%20011
			x=(x+f(a,b+1,1,'right'))%20011
			store[(a,b,step,dir)]=x
			
		return x
		
		
print(f(0,0,0,'down'))