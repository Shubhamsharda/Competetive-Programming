#input gathering
#codechef question link: https://www.codechef.com/ZCOPRAC/problems/ZCO15002/
input_arr=input().split(' ')
input_arr=[int(i) for i in input_arr]
n=input_arr[0]
k=input_arr[1]
arr=input().split(' ')
arr=[int(i) for i in arr]

count=0  #to count no of pairs
arr.sort()
count1=0
i=0
j=0
while i<n and j<n:
	count1+=1
	#print('---start---',count1)
	# print('i= ',i,'j= ',j)
	# print(arr)
	#print('answer= ',count)
	if arr[j]-arr[i]>=k:
		count+=n-j
		i+=1
	else:
		j+=1
print(count)
