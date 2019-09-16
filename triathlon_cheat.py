list=[]
for i in range(int(input())):
	a,b,c=map(int,input().split())
	list.append([a,b+c])
list.sort(key=lambda x:x[1])
list=list[::-1]
print(list)
mintime=0
comptime=0
for i in list:
	comptime+=i[0]
	time=comptime+i[1]
	if time>mintime:
		mintime=time
print(mintime)
# list=[]
# n=int(input())
# for i in range(n):
	# a,b,c=map(int,input().split())
	# list.append([a,b+c])
# list.sort(key=lambda x:x[1])
# mintime=0
# comptime=0
# for i in list:
	# comptime+=i[0]
	# temptime=comptime+i[1]
	# if temptime>mintime:
		# mintime=temptime
# print(mintime)

