flag='false'
switch=False
def pr(*args):
	if switch==True:
		for i in args:
			print(i,end=' ')
		print()

def coinChange(coins, amount) :
	def pr(*args):
		if switch==True:
			for i in args:
				print(i,end=' ')
			print()
	store={}
	def func(am):
		pr('called func(',am,')')
		global flag
		if am in store:
			pr('store accessed')
			return store[am]
		elif am in coins:
			return 1
		elif am==0:
			return 0
		else:
			ls=[]
			for i in coins:
				if am >= i:
					r=func(am-i)
					pr('func(',am-i,') returned: ',r)
					ls.append( 1+r)
			if len(ls)==0 :
				pr('list is empty for func(',am,')')
				return 9999999
			store[am]=min(ls)
			return store[am]
	res=func(amount)
	pr(res)
	pr('store:',store)
	if res>=9999999:
		return -1
	return res
print(coinChange([70,177,394,428,427,437,176,145,83,370],7582))