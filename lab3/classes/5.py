class account: 
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw (self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            print("You withdrew", amount, "from the account!")
            print("Balance:", self.balance)
        else:
            print("There is not enough money on the balance")

    def deposit (self, amount):
        self.balance += amount
        print("You deposited", amount, "into your account")
        print("Balance:", self.balance)

a1 = account("Lily", 3000)
a1.withdraw(1000)
a1.deposit(100)
a1.withdraw(3000)
