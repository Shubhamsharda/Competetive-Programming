
#delivery man
# https://www.codechef.com/problems/TADELIVE#

ls=input().split()
n=int(ls[0])
x=int(ls[1])
y=int(ls[2])
def func(x):
	return x[1]

andy=input().split()
andy=[int(i) for i in andy]
bob=input().split()
bob=[int(i) for i in bob]
diff=[(i,abs(andy[i]-bob[i])) for i in range(len(andy))]
diff.sort(key=func,reverse=True)
# print(diff)
andyc=0
bobc=0
amount=0
for ele in diff:
	if andy[ele[0]] > bob[ele[0]]:
		if andyc<x:
			andyc+=1
			amount+=andy[ele[0]]
		else:
			bobc+=1
			amount+=bob[ele[0]]
	elif andy[ele[0]] < bob[ele[0]]:
		if bobc <y:
			bobc+=1
			amount+=bob[ele[0]]
		else:
			andyc+=1
			amount+=andy[ele[0]]
	else:
		if andyc <x:
			andyc+=1
			amount+=andy[ele[0]]
		else:
			bobc+=1
			amount+=bob[ele[0]]
print(amount)