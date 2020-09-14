def dict(key, val):
	if len(key) > len(val):
		while len(key) > len(val):
			val.append(None)
		else:
			return { key:value for key,value in zip(key, val) }

key=[1,2,3,4]
val=[1,2,3]
print(dict(key,val))