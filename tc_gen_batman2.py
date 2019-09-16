
# test case generator

import random
ii=random.randint(0,20)
print(ii)
for x in range(ii):
	j=[]
	abc=random.randint(1,20)
	for k in range(0,abc):
		xyz=random.randint(1,100)
		# j=j+(str(xyz) + ' ')
		if xyz not in j:
			j.append(xyz)
	ss=''
	for qq in j:
		ss+=str(qq) + ' '
	ss=ss[:-1]
	print(len(j))
	print(ss)
  