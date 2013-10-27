#Below we are demonstrating subclassing in python and also inheritance, encapsulation and Polymorphism

class Person:
	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self): # Behavior methods
		return self.name.split()[-1] # self is implied subject
	def giveRaise(self, percent): #encapsulation
		self.pay = int(self.pay * (1 + percent)) # Must change here only
	def __str__(self):
		return'[Person: %s, %s]' % (self.name, self.pay)
class Manager(Person): #This shows inherhitance (subclassing)
    #The original giveRaise method is called here from Super class Person
    #However it is being modifed because managers also get a 10 % raise on top of their bonus
	def giveRaise(self, percent, bonus=.10):
		Person.giveRaise(self, percent + bonus) 

if __name__ == '__main__':
	bruce = Person('Bruce Smith')
	sue = Person('Sue Jones', job='dev', pay=100000)
	print(bruce.name, bruce.pay)
	print(sue.name, sue.pay)
	print(bruce.lastName(), sue.lastName()) # Use the new methods
	sue.giveRaise(.10) # instead of hardcoding
	print(sue.pay)
	#The below query will use the __str__ method and display something useful
	print(sue)
	Tony = Manager('Tony Macelli', 'mgr', 50000) #Here we created a new object Tony who is a manager
	print(Tony.lastName())
	print(Tony)
	Tony.giveRaise(.10) #The manager object Tony will be given a normal 10% raise with special 10% manager special
	print(Tony)
	#We will now demonstrate Polymorphism in ACTION
	print('--All three raises at once!!')
	for object in (bruce, sue, Tony):
		object.giveRaise(.10)
		print(object)
