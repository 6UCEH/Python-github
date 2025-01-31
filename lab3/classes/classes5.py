class bankaccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough on balance!")
        else:
            self.balance -= amount
            print("Withdrawed:", amount)

# Пример использования
account = bankaccount("Nikita", 100)
account.deposit(50)         # Deposited: 50
account.withdraw(30)        # Withdrawed: 30
account.withdraw(200)       # Not enough o n balance!
print("Balance:", account.balance)  # Balance: 120
