from functools import wraps

class Laptop:
	def __init__(self,mname,memory,price):
		print("New Object Created")
		self.mname = mname
		self.memory =  memory
		self.price = price

	def display(self):
		print(f"Company Name : {self.mname}")
		print(f"Memory : {self.memory}")
		print(f"Price : {self.price}")

	def discount(self,dis):
		dis_price = ((100 - dis)/100)*self.price
		return dis_price


l1 = Laptop('Lenovo',16,190000)
l2 = Laptop('apple',16,520000)
l3 =Laptop('Dell',16,150034)

# Laptop.display(l1)
# print(f"Discount in {l1.mname} : {l1.discount(40)}")

# l2.display()

# print(f"Discount in {l2.mname} :  {Laptop.discount(l2,50)}")