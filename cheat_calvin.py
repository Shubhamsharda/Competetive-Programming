n,k=map(int,input().split())
a=[int(i) for i in input().split()]
forward=[0]*n

backward=[0]*n
backward[0]=a[0]
backward[1]=a[0]+a[1]

for i in range(2,n):
    backward[i]=a[i]+max(backward[i-1],backward[i-2])


for i in range(k,n):
    forward[i]=a[i]+max(forward[i-1],forward[i-2])
maximum = -float('inf')
for i in range(k-1,n):
    maximum=max(maximum,forward[i]+backward[i]-a[i])
print(maximum)