
#reapeated string https://www.hackerrank.com/challenges/repeated-string/problem

s=str(input())
n=int(input())

def repeatedString(s, n):
	count=0
	for i in s:
		if i=='a':
			count+=1
	lens=len(s)
	a=n//lens
	counta=count*a
	print('before remainder counta: ',counta)
	remainder=n-a*lens
	print('remainder: ',remainder)
	for i in range(remainder):
		if s[i]=='a':
			counta+=1
	res=printt(s,n)
	ct=0
	for i in res:
		if i=='a':
			ct+=1
	print('repeated string is: ',res,'no of a:',ct,)
	print(counta)

def printt(s,n):
	ss=''
	for i in range(n):
		ss+=s
	return ss[:n]
repeatedString(s,n)
