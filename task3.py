import random 

class Cat:

	def __init__(self, count,boy = 0,girl = 0): 
		while boy + girl < count:
			boy = random.randint(0,count)
			girl = random.randint(0,count - boy)
		self._count = count
		self._boy = boy
		self._girl = girl

	def __display_info(self):
		print(self.__str__())

	def __str__(self):
		return "Общее кол-во котят: {} \t Мальчиков: {} \t Девочек: {}".format(self._count, self._boy, self._girl) 

cat = Cat(25)  
print(cat)
print("Кол-во мальчиков",cat._boy)
print("Кол-во девочек ",cat._girl)