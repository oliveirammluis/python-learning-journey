class BankAccount:
    def __init__(self, holder, balance = 0):
        self.holder = holder
        self.balance = balance

    def show_balance(self):
        print(f"Account holder: {self.holder}, Balance: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive!")
        else:
            self.balance += amount
            print(f"Account holder {self.holder} deposit {amount}, balance is now: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Insufficient funds! Balance is:{self.balance}")
        else:
            self.balance -= amount
            print(f"Account holder {self.holder} withdraw {amount}, balance is now: {self.balance}")