

def getMoneySpent(keyboards, drives, b):
	maxx=-1
	for i in keyboards:
		for j in drives:
			if i+j>maxx and i+j<=b:
				maxx=i+j
	return maxx