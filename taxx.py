a=map(int,input().split())
slab=[0]
for i in a:
	slab.append(i)
# slabs1={}
# for i in range(len(slabs)-1):
	# slab1[i]=(slab[i]+1,slab[i+1])
	
b=map(int,input().split())
percentage=[0]
for i in b:
	percentage.append(i)
rebate=int(input())
minnmaxx={}
for j in range(len(slab)-1):
	minnmaxx[j+1]=((slab[j]+1)*percentage[j]/100,slab[j+1]*percentage[j]/100)
tax=map(int,input().split())
salarysum=0
for i in tax:
	print('tax:',i)
	for j in minnmaxx:
		if (i ) >=minnmaxx[j][0] and i <= minnmaxx[j][1]:
			print('found',minnmaxx[j][0],minnmaxx[j][1])
			salarysum+=i*100/percentage[j-1]+rebate
			break
		elif (i) >= minnmaxx[len(slab)-1][1]:
			print('found gt',minnmaxx[len(slab)-1][1])
			salarysum+=i*100/percentage[-1] +rebate
			break
print(percentage)
print(slab)
print(minnmaxx)


print(salarysum)
