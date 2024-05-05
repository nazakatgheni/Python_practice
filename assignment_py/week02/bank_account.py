
class BankAccount:
    all_accounts = []
    
    #construction
    def __init__(self, name, balance = 0, reward = 0, interest = 0):
        self.name = name
        self.balance = balance
        self.reward = reward
        self.interest = interest
        self.is_rewarded_member = False
        BankAccount.all_accounts.append(self)
    
    #method
    def display_account_info(self):
        if self.is_rewarded_member == True:
            print(f"Hi,{self.name}, your account balance is {self.balance}, you earned {self.reward} reward.")
        else:
            print(f"Hi, {self.name}, your account balance is {self.balance}.")
        return self
    
    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name}, you are successfully deposit, your deposit amount is {amount}.")
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{self.name}, your withdraw is successful , your withdraw amount is {amount}.")
            return self
        else:
            print("Insufficient funds.")
            return self
    
    def yield_interest(self):
        earned_interest = self.balance * (self.interest / 100)
        self.balance += earned_interest
        print(f"Hi, {self.name}, you have yield {self.interest} interest.")
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            return(f"Here is account info: {cls.all_accounts}")

    
    #Creating Account
account1 = BankAccount("Jessica",36900, interest=1.6)
account2 = BankAccount("Amy",6700, interest=0.85)
    
    #deposit and withdraw 
account1.deposit(500).deposit(2500).deposit(50000).withdraw(10000).yield_interest().display_account_info()
    
account2.deposit(30000).deposit(5000).withdraw(230).withdraw(50).withdraw(163).withdraw(389).yield_interest().display_account_info()

print(BankAccount.print_all_accounts())