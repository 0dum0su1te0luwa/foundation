class BankAccount:
    def __init__ (self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'deposit was succesful\nbalance:{self.balance}')

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
        elif amount <= self.balance:
            self.balance = self.balance - amount
            print(f'withdrwal of {amount} was succesful\nbalance:{self.balance}')
    
    def get_balance(self):
        return self.balance

# Build a simple BankAccount class. Don't look up the syntax—try to write it from memory.

# Requirements

# Create a class called BankAccount with:

# Attributes:

# owner
# balance — default should be 0

# Methods:

# deposit(amount)
# Adds amount to the balance.
# Prints the new balance.
# withdraw(amount)
# Subtracts amount from the balance.
# If the amount is greater than the balance, print "Insufficient funds" instead.
# get_balance()
# Returns the current balance.