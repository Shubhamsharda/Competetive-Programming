#input gathering
input_arr=input().split(' ')
input_arr=[int(i) for i in input_arr]
n=input_arr[0]
k=input_arr[1]
arr=input().split(' ')
arr=[int(i) for i in arr]

count=0  #to count no of pairs
arr.sort()
count1=0
for i in range(len(arr)):
	for j in range(i,len(arr)):
		count1+=1
		print('count1,',count1)
		if arr[j]-arr[i] >= k:
			count+=1
print(count)
