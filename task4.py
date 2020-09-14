array =  list(map(int, input().split())) 

for i in range(len(array)):   
	print(array[(i + 1) % len(array)] + array[(i + len(array) - 1) % len(array)], end=' ' ) 