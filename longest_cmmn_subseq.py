

a=[1 ,2 ,3 ,4 ,1]
b=[3, 4 ,1, 2, 1, 3,3,5,4]

# print(ls)
def longestCommonSubsequence(a, b):
	lena=len(a)
	lenb=len(b)
	ls=[[-3 for j in range(lenb)] for i in range(lena)]
	def subseq(i,j):
		if i==lena-1:
			if a[i] in b[j:]:
				ls[i][j]=1
				return ls[i][j]
			else:
				ls[i][j]=0
				return ls[i][j]  #Doubt?
		elif j==lenb-1:
			if b[j] in a[i:]:
				ls[i][j]=1
				return ls[i][j]
			else:
				ls[i][j]=0
				return ls[i][j]
		elif ls[i][j]!=-3:
			return ls[i][j]
		else:
			if a[i]==b[j]:
				ls[i][j]=1+subseq(i+1,j+1)
				return ls[i][j]
			else:
				ls[i][j]=max(subseq(i+1,j),subseq(i,j+1))
				return ls[i][j]
	print(ls)
	return subseq(0,0)
print(longestCommonSubsequence(a,b))

