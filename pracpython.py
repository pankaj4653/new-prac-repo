from functools import wraps

class Car:
	num=0
	dis =10

	def __init__(self,comp,model,price,seat,year,typ):
		Car.num+=1
		print(f"This is __init__")
		self.comp = comp
		self.model = model
		self.price = price
		self.seat = seat
		self.year = year
		self.typ = typ

	@classmethod
	def constructor_given(cls,str):
		comp,model,price,seat,year,typ = str.split(",")
		return cls(comp,model,price,seat,year,typ)

	def display(self):
		print("This is the detail of the car")
		print(f"Manufacturing Company : {self.comp}")
		print(f"Model : {self.model}")
		print(f"Price : {self.price}")
		print(f"Seat : {self.seat}")
		print(f"Year of Manyfacturing : {self.year}")
		print(f"Type of Car : {self.typ}")

	@classmethod
	def display_total(cls):
		print(f"Total number of cars : {cls.num} and class name is {cls.__name__}")

	@staticmethod
	def hello(str1):
		print(f"hello everyone {str1}")

	def discount(self):
		p = self.price
		print(self.dis)
		p = ((100-self.dis)/100)*p
		return p
    
    
		



c1 = Car.constructor_given("Tata,Indigo,559000,4,2005,luv")
# c2 = Car("Hyundai","I10Grand",657188,4,2011,"luv")
# c3 = Car("Suzuki","Baleno",789233,4,2013,"luv")
# Car.display_total()
#print(c1.__dict__)
#c1.dis = 30
#print(c2.__dict__)
#Car.display_total()
#print(f"Num : {Car.num}")

#print(Car.discount(c1))
#print(Car.discount(c2))
c1.display()
Car.hello("World")
#Car.display_total()

