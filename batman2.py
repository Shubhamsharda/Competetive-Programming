
import sys

# ls=[5, 3, 4 ,6 ,1, 2]
	#[2,1,6,4,3,5]
# lsrev=ls[::-1]
# res=[]



# print(l)
# def f(i,prev):
	# # print('f(',i,prev,')')
	# if i>l-1:
		# return 0
	# elif i in store:
		# return store[i]
	# else:
		# if ls[i]>prev:
			# a=1+f(i+1,ls[i])
			# b=f(i+1,prev)
			# if a>b:
				# return a
			# else:
				# return b
		# else:
			# return f(i+1,prev)
# print(f(0,-10000))

def f(i,iprev,dprev):
	# print('f(',i,iprev,dprev,')')
	try:
		if i>=lena:
			return 0
		elif (i,iprev,dprev) in store:
			return store[(i,iprev,dprev)]
		else:
			if ls[i]>iprev and ls[i]<dprev:
				store[(i,iprev,dprev)]= max(1+f(i+1,ls[i],dprev),1+f(i+1,iprev,ls[i]),f(i+1,iprev,dprev))
			elif ls[i]>iprev and ls[i]>dprev:
				store[(i,iprev,dprev)]= max(1+f(i+1,ls[i],dprev),f(i+1,iprev,dprev))
			elif ls[i]<iprev and ls[i]<dprev:
				store[(i,iprev,dprev)]= max(1+f(i+1,iprev,ls[i]),f(i+1,iprev,dprev))
			else:
				store[(i,iprev,dprev)]= f(i+1,iprev,dprev)
			return store[(i,iprev,dprev)]
	except:
		return 0

t=int(input())
l=[]
nlist=[]
for i in range(t):
	n=int(input())
	inp=input().split()
	a=[int(i) for i in inp]
	l.append(a)
	nlist.append(n)
	

for i in range(len(l)):
	store={}
	lena=len(l[i])
	ls=l[i]
	if(len(ls)>5 and nlist[i]>5):
		# print('mdsnvkjdfnvjdfnvkdnvkjdf')
		if (len(l[-1])*len(l[-1]) >10):
			sys.setrecursionlimit(len(l[-1])*len(l[-1]))
	try:
		print(f(0,-10000,sys.maxsize))
	except ValueError:
		print('ValueError occured')
	except EOFError:
		print('Why did you do an EOF on me?')
	except RuntimeError as e:
		print(e.message)
	except:
		print('An error occured.')