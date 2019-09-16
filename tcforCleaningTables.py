# tc_for_cleaningTableProb
import random
# tccount=random.randrange(1,100)
tccount=10
print(tccount)
for i in range(tccount):
	n=random.randrange(1,200)
	# n=random.randrange(1,7)
	m=random.randrange(1,400)
	# m=random.randrange(1,10)
	print(n,' ',m)
	st=''
	for j in range(m):
		st+=str(random.randrange(1,200))+' '
	print(st.rstrip())