
printswitch=False;
def pr(*args):  # for printing using a switch
	if printswitch:
		for i in args:
			print(i,' ',end='')
		print('')
	
t=int(input()) 
res=[] #final result stored here
for i in range(t):  #taking in test cases
	count=0
	noOfTables,noOfOrders = map(int,input().split())
	orders=list(map(int,input().split()))
	dicc={}
	for index in range(len(orders)):  # making a hash map of nearest order element for each order
		if orders[index] not in dicc:
			dicc[orders[index]]=[index]
		else:
			dicc[orders[index]].append(index)
	tableOccupancy={}
	for ind in range(len(orders)):
		pr('tc=',i,' order=',orders[ind],' ind:',ind,'tableOccupancy: ',tableOccupancy,'noOftables:',noOfTables)
		if noOfTables>0:
			if orders[ind] in tableOccupancy:
				pr('debug 1')
				dicc[orders[ind]].remove(ind)
			else:
				pr('debug 2')
				dicc[orders[ind]].remove(ind)
				tableOccupancy[orders[ind]]=dicc[orders[ind]]
				count+=1
				noOfTables-=1
		else:
			if orders[ind] in tableOccupancy:
				pr('debug 3')
				dicc[orders[ind]].remove(ind)
				tableOccupancy[orders[ind]]=dicc[orders[ind]]
			else:
				pr('debug 4-------------------------------------------------------------')
				nulllistfound=False
				for k,v in tableOccupancy.items():
					if len(v)==0:
						tableOccupancy.pop(k)
						dicc[orders[ind]].remove(ind)
						tableOccupancy[orders[ind]]=dicc[orders[ind]]
						count+=1
						nulllistfound=True
						break
				if nulllistfound:
					pr('debug 5')
					continue
				else:
					pr('debug 6')
					ordertoremove=max(tableOccupancy,key=lambda k: tableOccupancy[k][0] )
					tableOccupancy.pop(ordertoremove)
					dicc[orders[ind]].remove(ind)
					tableOccupancy[orders[ind]]=dicc[orders[ind]]
					count+=1
	res.append(count)
for k in res:
	print(k)
				
	
	