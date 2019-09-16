def printit(n,c):
	for i in range(n):
		if i in c:
			print('#',end='  ')
		else:
			print(' ',end='  ')
	print()
	for i in range(n):
		if i>9 and i!=0:
			print(i,end=' ')
		else:
			print(i,end='  ')
def flatlandSpaceStations(n, c):
    if n==len(c):
        return 0
    c.sort()
    maxx=c[0]-0
    for i in range(len(c)-1):
        diff=c[i+1] -c[i]
        if diff//2 > maxx:
            maxx=diff//2
    if n - c[-1] -1  >maxx:
        maxx= n - c[-1] -1
    return maxx
	
printit(20,[13, 1 ,11 ,10 ,6])	
print(flatlandSpaceStations(20,[13, 1 ,11 ,10 ,6]))

