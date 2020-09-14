def write(num): 
	i = 0 
	arr = []
	while i <= num:
		j=1
		while j <= i: 
			arr.append(str(i))
			j+=1
			if len(arr) == num: 
				return arr
		i+=1

res = write(7)
print(','.join(res))

