def fun(k):
	return k[1]
n=int(input())
ls=[]
for i in range(n):
	a=input().split()
	a=[int(i) for i in a]
	ls.append([a,-1,i+1])

orig=input().split()
orig=[int(i) for i in orig]
for i in range(n):
	ls[i][1]=min(abs(orig[0]-ls[i][0][0]) + abs(orig[1]-ls[i][0][1]) , abs(orig[0]-ls[i][0][2]) + abs(orig[1]-ls[i][0][3]))

ls.sort(key=lambda x: (x[1], x[2]))
res=''
for k in ls:
	res+=str(k[2])+' '
print(res.strip(),end='')
