#example showing classes and OOP in python
class Employee:
	'All employees will use this class'
	empCount = 0

	def __init__(self, name, salary, sex):
		self.name = name
		self.salary = salary
		self.sex = sex
		Employee.empCount += 1

	def displayCount(self):
		print "Total Employee %d" % Employee.empCount

	def displayEmployee(self):
		print "Name : ", self.name,  ", Salary: ", self.salary, ", Sex: ", self.sex

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000, "female")
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000, "male")
emp3 = Employee("Paco", 110000, "male")

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print "Total Number of Employee's %d" % Employee.empCount
