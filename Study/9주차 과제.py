class BankAccount:
    def __init__(self, name, balance=0):
        if balance<0:
            balance=0
        self.name = name
        self.balance = balance
        
    def __str__(self):
        return self.name + "," + str(self.balance)

    def show_balance(self):
        return self.balance
        
    def deposit(self, amount):
        if amount>=0:
            self.balance = self.balance+amount
            return self.balance
        else:
            print("입금이 불가능합니다.")
        
    def withdraw(self, amount):
        if amount>=0 and amount<=self.balance:
            self.balance = self.balance-amount
            return self.balance
        else:
            print("출금이 불가능합니다.")


ba=BankAccount('San',10)
ba.show_balance()
ba.deposit(10)
ba.deposit(100)
ba.deposit(-10)
ba.__str__()
ba.withdraw(10)
ba.withdraw(1000)
ba.__str__()
ba.show_balance()

