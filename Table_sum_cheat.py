N = int(input())
ls = [int(x) for x in input().split()]
res = [0]*N
max = max(ls)
n = ls.index(max)
v = n
print('ls:',ls)
for i in range(N):
	print('i:',i,'v:',v,'max:',max,'n:',n,'res:',res)
	v = (n+i)%N
	if(ls[v] > max):
		max = ls[v]
	res[N-1-v] = max+N
	max -= 1
print('i:',i,'v:',v,'max:',max,'n:',n,'res:',res)
print(*res)