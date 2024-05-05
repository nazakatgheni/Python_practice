from bank_account import BankAccount

class User():
    
    def __init__(self, name, user_id, email,balance=0, reward = 0):
        self.name = name
        self.id = user_id
        self.email = email
        self.balance = balance
        self.account = BankAccount(name= name, balance=0)
        
    def show_email(self):
        print(f"Hello, {self.name}, your linked email address is {self.email}")
        
    def show_id(self):
        print(f"Hello, You're user ID is {self.id}")
    
    def make_deposit(self, amount):
        self.balance += amount 
        print(f"{self.name}, you are successfully deposit, your deposit amount is {amount}.")
        return self
    
    def make_withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name}, your withdraw is successful , your withdraw amount is {amount}.")
            return self
        else:
            print("Insufficient funds.")
            return self
        
    def display_user_balance(self):
        print(f"Hi {self.name}, Here is your balance: {self.account.balance}.")
        
        
user1 = User("Mominjan", 17, "amomin@gmail.com")
user1.show_id()

user1.make_deposit(500)
user1.make_withdraw(300)