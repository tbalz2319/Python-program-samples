#classExp
class NumberClass:
	def __init__(self):
		self.value=0
	def addin(self, amount):
		self.value += amount

tbalz = NumberClass()
print tbalz.value
tbalz.addin(19)
print tbalz.value
tbalz.addin(200)
print tbalz.value
