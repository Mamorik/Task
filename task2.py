def getNumber(string): 
	lenght = len(string)
	numbers = [] 
	i = 0 

	while i < lenght: 
		StrInInt = '' 
		Symbol = string[i] 
		while 0 <= int(Symbol) <= 9:
			StrInInt += Symbol
			i += 1
			if i < lenght: 
				Symbol = string[i]
			else:
				break
		i += 1  
		if StrInInt != '': 
			numbers.append(int(StrInInt)) 
	return numbers 

print (getNumber('df355dfgd1gdg15g6d35fg4df6g2'))
