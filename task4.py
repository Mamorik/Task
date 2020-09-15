def sumElem(li): 
	lis = []
	for i in range(len(li)): 
		lis.append(li[(i + 1) % len(li)] + li[(i + len(li) - 1) % len(li)])
	return lis

li=[1,3,5,6,10]
print(sumElem(li))
