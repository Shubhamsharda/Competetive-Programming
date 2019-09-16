

def func(i,sign,prev):
	print(i,sign)
	if i>=n:
		print('1')
		return 0
	elif (i,sign) in store:
		print('2')
		return store[(i,sign)]
	elif ls[i]>0 and sign=='neg':
		print('3')
		return func(i+1,'neg',prev) 
	elif ls[i]<0 and sign == 'pos':
		print('4')
		return func(i+1,'pos',prev)
	elif i!=0 and abs(ls[i])<=abs(ls[prev]):
		print('5')
		return func(i+1,sign,prev)
	else:
		print('heh 6')
		if sign=='pos':
			store[(i,sign)]=1+func(i+1,'neg',i)
			return store[(i,sign)]
		else:
			store[(i,sign)]=1+func(i+1,'pos',i)
			return store[(i,sign)]

store={}		
n=int(input())
ls=input().split()
ls=[int(i) for i in ls]
signchanged=False
i=0
init=None
if ls[0]>0:
	init='pos'
else:
	init='neg'
while(True):
	if ls[i] > 0:
		sig='pos'
	else:
		sig='neg'
	if sig==init:
		i+=1
	else:
		break
maxx=0
for j in range(i+1):
	print('called ',j,init)
	res=func(j,init,j)
	if res>maxx:
		maxx=res

print('result is: ',maxx)
print('store is : ',store)
		
		