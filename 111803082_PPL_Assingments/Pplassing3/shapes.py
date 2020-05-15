import turtle
class circle():
	def __init__(self,a):
		self.__radius = a
	def get_radius(self):
		return self.__radius
	def set_radius(self,x):
		self.__radius=x
	def get_circum(self):
		return (self.__radius)*2*3.14
	def get_area(self):
		return ((self.__radius)**2)*3.14
	def draw(self) :
        	turtle.circle(self.__radius)

c1=circle(40)
x=c1.get_radius()
print("The radius of circle is{}:".format(x))
y=c1.get_area()
print("The area of circle is:{}".format(y))
c1.draw()

class triangle():
	def __init__(self,a=3):
		self.__no_of_sides = a
	def sides(self,b,c,d):
		self.__s1=b
		self.__s2=c
		self.__s3=d
		sides=[self.__s1,self.__s2,self.__s3]
		return sides
	def get_perimeter(self):
		return (self.__s1+self.__s2+self.__s3)
t1=triangle()
li=t1.sides(5,12,13)
print("The sides of triangle are:{}".format(li))

class equitri():
	def __init__(self,a=3):
		self.__no_of_sides = a
	def sides(self,b):
		self.__s1=b
		self.__s2=b
		self.__s3=b
		sides=[self.__s1,self.__s2,self.__s3]
		return sides
	def get_perimeter(self):
		return (3*self.__s1)
	def get_area(self):
		return(0.43301*self.__s1)
	def get_ia(self,ia=60):
		self.__internalangle=ia
		return self.__internalangle
	def draw(self) :
		turtle.forward(self.__s1)
		for i in range(0,2) :
		    turtle.right(-120)
		    turtle.forward(self.__s1)
		turtle.right(-120)
et1=equitri()
li1=et1.sides(50)
print("The sides of equilateraltriangle are:{}".format(li1))
g=et1.get_area()
print("The area of equilateraltriangle is {}".format(g))
v=et1.get_ia()
print ("The internal angle of a equilateraltriangle is:{}".format(v))
et1.draw()	
	

	

class square():
	def __init__(self,a=4):
		self.__no_of_sides=a
	def side(self,side):
		self.__side=side
	def get_area(self):
		return((self.__side)**2)
	def get_perimeter(self):
		return ((self.__side)*4)
	def draw(self) :
		turtle.goto(self.__side,0)
		turtle.goto(self.__side,self.__side)
		turtle.goto(0,self.__side)
		turtle.goto(0,0)
s1=square()
s1.side(50)
u=s1.get_area()
print("The area of square is {}".format(u))
s1.draw()

class rectangle():
	def __init__(self,a=4):
		self.__no_of_sides=a
	def sides(self,length,breadth):
		self.__len=length
		self.__bread=breadth
	def get_area(self):
		return((self.__len)*(self.__bread))
	def get_perimeter(self):
		return(2*((self.__len)+(self.__bread)))
	def draw(self) :
		turtle.goto(self.__len,0)
		turtle.goto(self.__len,self.__bread)
		turtle.goto(0,self.__bread)
		turtle.goto(0,0)
r1=rectangle()
r1.sides(100,120)
z=r1.get_perimeter()
print("The perimeter of rectangle is {}".format(z))
r1.draw()

class ellip():
	def __init__(self,a=10,b=2):
		self.__major=a
		self.__minor=b
	def get_area(self):
		return ((self.__major)*(self.__minor)*3.14)

class pentagon():
	def __init__(self,a=5):
		self.__no_of_sides=a
	def get_side(self):
		self.__side=120
	def get_ia(self,ia=108):
		self.__internalangle=ia
		return self.__internalangle
	def style(self):
		self.__sty="symmetrical"
		return self.__sty
	def draw(self) :
		turtle.forward(120)
		for i in range(0,4) :
		    turtle.right(-72)
		    turtle.forward(120)
		turtle.right(-72)
p1=pentagon()
w=p1.get_ia()
print ("The internal angle of a pentagon is:{}".format(w))
p1.draw()

class hexagon():
	def __init__(self,a=6):
		self.__no_of_sides=a
	def get_side(self,side=120):
		self.__side=side
	def get_ia(self,ia=120):
		self.__internalangle=ia
		return self.__internalangle
	def style(self):
		self.__sty="symmetrical"
		return self.__sty
	def draw(self) :
		turtle.forward(120)
		for i in range(0,5) :
		    turtle.right(-60)
		    turtle.forward(120)
		turtle.right(-60)
h1=hexagon()
b=h1.get_ia()
print ("The internal angle of a hexagon is:{}".format(b))
h1.draw()	
	

class heptagon():
	def __init__(self,a=7):
		self.__no_of_sides=a
	def get_side(self,side=120):
		self.__side=side
	def get_ia(self,ia=128.57):
		self.__internalangle=ia
		return self.__internalangle
	def style(self):
		self.__sty="symmetrical"
		return self.__sty
	def draw(self) :
		turtle.forward(120)
		for i in range(0,6) :
		    turtle.right(-51.43)
		    turtle.forward(120)
		turtle.right(-51.43)
H1=heptagon()
k=H1.get_ia()
print ("The internal angle of a heptagon is:{}".format(k))
H1.draw()

class octagon():
	def __init__(self,a=8):
		self.__no_of_sides=a
	def get_side(self,side=120):
		self.__side=side
	def get_ia(self,ia=135):
		self.__internalangle=ia
		return self.__internalangle
	def style(self):
		self.__sty="symmetrical"
		return self.__sty
	def draw(self) :
		turtle.forward(120)
		for i in range(0,7) :
		    turtle.right(-45)
		    turtle.forward(120)
		turtle.right(-45)
o1=octagon()
m=o1.get_ia()
print ("The internal angle of a pentagon is:{}".format(m))
o1.draw()	
		
		
	
