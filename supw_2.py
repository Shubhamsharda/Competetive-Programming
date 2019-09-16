from pptree import *




n=int(input())
lll=input().split()
ls=[int(i) for i in lll]
root44=Node('f('+str(n)+')')
minn={}


	
def f(n,root):
	#print_tree(root44)
	if(n==2):
		print('For n= ',n, ' Result is: ',min(ls[0],ls[1],ls[2]))	
		root.name=root.name+'='+str(min(ls[0],ls[1],ls[2]))
		
		
		#return min(ls[0],ls[1],ls[2])
		return 0
		#return ls[2]
	elif(n==1):
		print('For n= ',n, ' Result is: ',min(ls[0],ls[1]))
		root.name=root.name+'='+str(min(ls[0],ls[1]))
		
		
		#return min(ls[0],ls[1])
		#return ls[1]
		return 0
	elif(n==0):
		print('For n= ',n, ' Result is: ',ls[0])
		root.name=root.name+'='+str(ls[0])
		
		return 0
		#return ls[0]
	else:

		result=0
		try:
			result=minn[n]
		except KeyError:
			child1=Node('f('+str(n-1)+')'+'+'+'ls['+str(n-1)+']: '+str(ls[n-1]),root)
			child2=Node('f('+str(n-2)+')'+'+'+'ls['+str(n-2)+']: '+str(ls[n-2]),root)
			child3=Node('f('+str(n-3)+')'+'+'+'ls['+str(n-3)+']: '+str(ls[n-3]),root)			
			minn[n]=min(f(n-1,child1)+ls[n-1],f(n-2,child2)+ls[n-2],f(n-3,child3)+ls[n-3])
			result=minn[n]
			
		print('For n= ',n, ' Result is: ',result)
		root.name=root.name+'='+str(result)
		
		
		return result
#sys.setrecursionlimit(3*n)
print(f(n,root44))
print_tree(root44)
print(ls)
#print(minn)
		