class Account:


    def __init__(self, account_owner, account_balance=0):
        self.account_owner = account_owner
        self.account_balance = account_balance


    def __str__(self):
        return f'Account owner: {self.account_owner}, Account balance: ${self.account_balance}'

    def deposit(self, deposit_add):
        self.deposit_add = deposit_add
        self.account_balance = self.account_balance + deposit_add
        return f'Deposit Accepted, Deposit Saldo: ${self.account_balance}'

    def withdraw(self, deposit_withdraw):
        self.deposit_withdraw = deposit_withdraw
        if self.deposit_withdraw <= self.account_balance:
            self.deposit_saldo = self.account_balance + deposit_withdraw
            return f'Withdrawal Accepted'
        else:
            return f'Funds Unavailable!'

# 1. Instantiate the class
acct1 = Account('Jose', 100)

# 2. Print the object
print(acct1) # Account owner:   Jose   \\\   Account balance: $100

# 3. Show the account owner attribute
print(acct1.account_owner)  # 'Jose'

# 4. Show the account balance attribute
print(acct1.account_balance) # 100

# 5. Make a series of deposits and withdrawals
print(acct1.deposit(50)) # Deposit Accepted

print(acct1.withdraw(75)) # Withdrawal Accepted
print(acct1.deposit_saldo)
# 6. Make a withdrawal that exceeds the available balance
print(acct1.withdraw(500)) # Funds Unavailable!