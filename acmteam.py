

def acmTeam(topic):
	def func(a,b,m):
		c=0
		for i in range(m):
			if a[i]=='1' or b[i]=='1':
				c+=1
		return c
	maxx=0
	count=0
	for i in range(len(topic)):
		for j in range(i+1,len(topic)):
			r=func(topic[i],topic[j],m)
			if r == maxx:
				count+=1
			elif r>maxx:
				count=1
				maxx=r
	return [maxx,count]
	
m=5
print(acmTeam(['10101'
,'11100',
'11010',
'00101']))