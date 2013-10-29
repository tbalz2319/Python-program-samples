class BankAccount:
	def __init__(self):
		self.balance = 0

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

	def deposit(self, amount):
		self.balance += amount
		return self.balance

a = BankAccount()
deposited = a.deposit(100)
c = a.withdraw(40)
print(c)
print 'if %s is deposited into an account and %s is taken out' % (deposited,c)
print 'The account will be left with a balace of $ %s' % a.balance
		
class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print 'Sorry, minimum balance must be maintained.'
        else:
            BankAccount.withdraw(self, amount)
