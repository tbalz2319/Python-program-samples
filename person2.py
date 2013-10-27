#below we are adding the __str__ overload method for printing objects as our third method

class Person:
	def __init__(self, name, job=None, pay=0):
		self.name = name
		self.job = job
		self.pay = pay
	def lastName(self): # Behavior methods
		return self.name.split()[-1] # self is implied subject
	def giveRaise(self, percent):
		self.pay = int(self.pay * (1 + percent)) # Must change here only
	def __str__(self):
		return'[Person: %s, %s]' % (self.name, self.pay)

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
