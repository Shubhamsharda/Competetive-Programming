
def climbingLeaderboard(scores, alice):
	lens=len(scores)
	lena=len(alice)
	res=[]
	i=lena-1
	j=0
	pos=0
	# print('alice[',i,']:',alice[i],'##','scores[',j,']:',scores[j],'## pos:',pos,'## res:',res)
	while i>=0 and j<lens: # and alice[i]<=scores[-1]:
		# print('before:','alice[',i,']:',alice[i],'##','scores[',j,']:',scores[j],'## pos:',pos,'## res:',res)
		print('i: ',i,' j:',j)
		if j!=0 and scores[j]==scores[j-1]:
			j+=1
			print('--1--')
		elif alice[i]>=scores[j]:
			pos+=1
			res.append(pos)
			i-=1
			j+=1
			print('--2--')		
		else:
			pos+=1
			j+=1
			print('s--3--')		
		print(' pos:',pos,'  res:',res)
		print('-------------------------')
	if i>=0:
		while i>=0:
			if alice[i]==scores[-1]:
				res.append(pos)
			else:
				res.append(pos+1)
			i-=1
	print('pos is :',pos)
	print('i:',i,' j:',j)
	i=0
	# while alice[i]<=scores[-1]:
		# res.append(pos)
		# i+=1
	return res[::-1]			
s=[100 ,100, 50, 40, 40, 20, 10,10,10,9,9,8,1,1]
a=[0,1,5,6 ,25 ,50, 120] 
print(climbingLeaderboard(s,a))