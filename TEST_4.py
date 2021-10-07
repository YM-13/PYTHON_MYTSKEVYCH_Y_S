class BankAccount:

    def __init__(self, client_id, client_first_name, client_last_name, balance=0.0):
        self.client_id = client_id
        self.client_first_name = client_first_name
        self.client_last_name = client_last_name
        self.balance = balance

    def add(self, bal):
        return self.balance + bal

    def withdraw(self, bal):
        return self.balance - bal

per_1 = BankAccount('12345', 'Yurii', 'Mytsck', 2)
#per_1.add(113)
print(per_1.client_last_name)
print(per_1.add(113))
