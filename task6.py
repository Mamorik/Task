def modify_list(li): 
	for i in li: 
		if i % 2 == 1: 
			li.remove(i)
	for i in range(len(li)):
		li[i] = round(li[i] / 2) 

li = [1, 2, 3, 4, 5, 6]
modify_list(li)
print(li)