

X = "abcdxyz"
Y = "xyzabcd"
from pptree import *

def lcs(i, j, count,root) :  
	if (i == 0 or j == 0) :
		root.name+=':'+str(count)
		return count    
	if (X[i - 1] == Y[j - 1]) :
		child=Node('f('+str(i-1)+','+str(j-1)+')',root)
		count = lcs(i - 1, j - 1, count + 1,child)  
	child2=Node('f('+str(i)+','+str(j-1)+')',root)
	child3=Node('f('+str(i-1)+','+str(j)+')',root)
	count = max(count, max(lcs( i, j - 1, 0,child2),lcs( i - 1, j, 0,child3)))  
	root.name+=':'+str(count)
	return count 
	

n = len(X) 
m = len(Y) 
r=Node('f('+str(n)+','+str(m)+')')
print(lcs(n,m,0,r))
print_tree(r)
