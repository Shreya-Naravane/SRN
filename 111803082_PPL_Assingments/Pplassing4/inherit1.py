class animals():
	def __init__(self):
		self.__fur="colourfull"
		self.__numeyes=2
		self.__numlegs=4
	def get_legs(self):
		return self.__numlegs
	def set_legs(self,b):
		 self.__numlegs=b
	def get_eyes(self):
		return self.__numeyes
	def walk(self):
		print("We can run or walk on ground")
	def get_fur(self):
		return self.__fur
	def set_fur(self,a):
		self.__fur=a
class cat(animals):
	def __init__(self):
		animals.__init__(self)
	def set_legs(self,x):
		animals.set_legs(self,x)
	def set_fur(self,m):
		animals.set_fur(self,m)
class lion(cat):
	def __init__(self):
		cat.__init__(self)
	def set_legs(self,y):
		cat.set_legs(self,y)
	def set_fur(self,n):
		cat.set_fur(self,n)
class tiger(cat):
	def __init__(self):
		cat.__init__(self)
	def set_legs(self,y):
		cat.set_legs(self,y)
	def set_fur(self,n):
		cat.set_fur(self,n)
class leopard(cat):
	def __init__(self):
		cat.__init__(self)
	def set_legs(self,y):
		cat.set_legs(self,y)
	def set_fur(self,n):
		cat.set_fur(self,n)
class cheetah(cat):
	def __init__(self):
		cat.__init__(self)
	def set_legs(self,y):
		cat.set_legs(self,y)
	def set_fur(self,n):
		cat.set_fur(self,n)
class snowleopard(cat):
	def __init__(self):
		cat.__init__(self)
	def set_legs(self,y):
		cat.set_legs(self,y)
	def set_fur(self,n):
		cat.set_fur(self,n)
class blackpanther(cat):
	def __init__(self):
		cat.__init__(self)
	def set_legs(self,y):
		cat.set_legs(self,y)
	def set_fur(self,n):
		cat.set_fur(self,n)
class jaguar(cat):
	def __init__(self):
		cat.__init__(self)
	def set_legs(self,y):
		cat.set_legs(self,y)
	def set_fur(self,n):
		cat.set_fur(self,n)
class puma(cat):
	def __init__(self):
		cat.__init__(self)
	def set_legs(self,y):
		cat.set_legs(self,y)
	def set_fur(self,n):
		cat.set_fur(self,n)
l1=lion()
l1.set_legs(4)
l1.set_fur("lion has sandy colour")
x=l1.get_fur()
print(x)
t1=tiger()
t1.set_legs(4)
t1.set_fur("tiger has black and yellow colour")
x=t1.get_fur()
print(x)
c1=cheetah()
c1.set_legs(4)
c1.set_fur("cheetah has tan and black colour")
x=c1.get_fur()
print(x)
sl1=snowleopard()
sl1.set_legs(4)
sl1.set_fur("snow leopard has white colour")
x=sl1.get_fur()
print(x)
p1=blackpanther()
p1.set_legs(4)
p1.set_fur("Black panther has black colour")
x=p1.get_fur()
print(x)


		
		
		
		
		
		
		

