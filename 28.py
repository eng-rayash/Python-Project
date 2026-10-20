class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
    def __str__(self):
        return f"{self.owner}: {self.balance}"
acc = BankAccount("Ali", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc)