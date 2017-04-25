class BankAccount(object):
    def deposit(self):
        self.balance = balance
    def withdraw(self):
        self


class SavingsAccount(BankAccount):
    def __init__(self):
        self.balance = 500

    def deposit(self, amount):
        if amount < 0:
            return 'Invalid Amount'
        else:
            self.balance += amount
            return self.balance

    def withdraw(self, withdraw_amount):
        if self.balance - withdraw_amount < 500:
            return 'Cannot withdraw beyond the minimum account balance'

        if withdraw_amount > self.balance:
            return 'Cannot withdraw beyond the current account balance'

        if withdraw_amount < 0:
            return 'Invalid withdraw amount'
        else:
            self.balance -= withdraw_amount
            return self.balance


class CurrentAccount(BankAccount):
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount < 0:
            return 'Invalid Amount'
        else:
            self.balance += amount
            return self.balance

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            return "Cannot withdraw beyond the current account balance"
        if withdraw_amount < 0:
            return 'Invalid withdraw amount'
        else:
            self.balance -= withdraw_amount
            return self.balance

