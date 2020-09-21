def modify_list(li):
	i = 0
	while i < len(li):
		if li[i] % 2 == 1:
			li.pop(i)
		else:
			li[i] = round(li[i] / 2)
			i += 1
li = [1,2,3,4,5,6,8,8,4,2]
modify_list(li)
print(li)