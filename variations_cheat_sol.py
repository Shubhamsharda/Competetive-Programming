def solve(nums, n, k):
	nums = sorted(nums)
	answer = i = j =  0
	count=0
	while i<n and j<n:
		count+=1
		
		print('-----start-----',count)
		print('i=',i,' j=',j)
		print('answer= ',answer)
		print(nums)
		if abs(nums[i]-nums[j]) >= k:
			answer += n-j
			i += 1
		else:
			j += 1
	print(answer)
	
n, k = list(map(int, input().split()))
nums = list(map(int, input().split()))
solve(nums, n, k)