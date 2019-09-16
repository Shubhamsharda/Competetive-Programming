

def QuickSort(A):                                                        #Normal Quicksort
	pivot=int((len(A)-1)/2)
	print('pivot index is : ',pivot,'Actual pivot is:  ',A[pivot])
	for i in range(0,len(A)-1):
		print('i= ',i,'A[i]= ',A[i])
		i=0
		j=len(A)-1
		k=0
		while(k<20):
			k+=1
			while(A[i]<A[pivot]):
				print('i is : ', i, 'A[i] is: ',A[i])
				i+=1
			print('The last i is: ',i,'A[i] is: ',A[i])
			while(A[j]>A[pivot]):
				print('j is :',j,'A[j] is: ',A[j])
				j-=1
			print('The last j is: ',j,'A[j] is: ',A[j])
			print('now swapping A[i] and A[j]')
			if (pivot==i):
				pivot=j
				print('pivot changed!: ',pivot)
			elif (pivot==j):
				print('pivot changed!: ',pivot)
				pivot=i
			temp=A[i]
			A[i]=A[j]
			A[j]=temp
			print('swap complete')
			print('new array is: ',A)
			
def QuickSort2(A):                                           #Normal Quicksort
	print('A: ',A)
	if(len(A)==1 or A==[]):
		return A
	pivot=len(A)-1
	left=[]
	right=[]
	for i in range(len(A)):
		if i != pivot:
			if(A[i]<A[pivot]):
				left.append(A[i])
			else:
				right.append(A[i])
	print('left: ',left)
	print('right: ',right)
	if left==[]:
		return [A[pivot]] + QuickSort2(right)
	elif right==[]:
		return QuickSort2(left) + [A[pivot]]
	else:	
		return QuickSort2(left) + [A[pivot]] + QuickSort2(right)
	
def QuickSort3(A):                                                           #in-place Quicksort
	print('Array before run',A)

	l=0
	r=len(A)-1
	if (len(A)==1 or A==[]):
		return A
	pivot = A[int(len(A)/2)]
	print('pivot is: ',pivot)
	while l<r:
		while A[l] < pivot:
			l+=1
		while A[r] > pivot:
			r-=1
		temp=A[l]
		A[l]=A[r]
		A[r]=temp
		print('Array after swap: ',A)
	if l==r:
		return QuickSort3(A[:l]) + [A[l]] + QuickSort3(A[r+1:])
		
def QuickSort4(A):                                                        #inplace Quicksort
	print('Array before run',A)

	l=0
	r=len(A)-1
	if (len(A)==1 or A==[]):
		return A
	pivot = int(len(A)/2)
	print('pivot is: ',A[pivot])
	while l<r:
		while A[l] < A[pivot]:
			l+=1
		while A[r] > A[pivot]:
			r-=1
		if(pivot==l):
			pivot=r
		elif(pivot==r):
			pivot=l
		temp=A[l]
		A[l]=A[r]
		A[r]=temp
		print('Array after swap: ',A)
		print('pivot after swap: ',A[pivot])
	if l==r:
		return QuickSort4(A[:l]) + [A[l]] + QuickSort4(A[r+1:])
		
			
A=[22,77,44,23,90,23]
print(QuickSort4(A))
		

		
			