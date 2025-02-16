class BankAccount:
    def __init__(self,id,balance,name,age):
        self.id = id
        self.balance = balance
        self.name = name
        self.age = age

    def withdraw(self,amount):
        if amount >= self.balance:
            print("YOU ARE WITHDRAWING TO MUCH MONEY!!!!!!!!!!!")
        else:
            print("YOU CAN WITHDRAW!!!!!!!!")
            self.balance -= amount
        print(f"You withdraw {amount}.Account balance is {self.balance}")

my_account = BankAccount(id="080877",balance=99999999999999999999999999999999,name="ISAAC POON",age=10)
print(f"Intitial balance is {my_account.balance}")
my_account.withdraw(999999999999999999998)