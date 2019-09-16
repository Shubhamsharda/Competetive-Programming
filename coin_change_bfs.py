

def coinchange(coins,amount):
	if amount==0:
		return 0
	que1=[0]
	que2=[]
	nc=0
	visited=[False]*(amount+1)
	while(len(que1)> 0):
		nc+=1
		s= len(que1)
		for ele in que1:
			for i in coins:
				if ele+i > amount:
					continue
				if ele+i==amount:
					return nc
				if not visited[ele+i]:
					visited[ele+i]=True
					que2.append(ele+i)
		que1,que2=que2,[]
	return -1

print(coinchange([70,177,394,428,427,437,176,145,83,370],7582))
		