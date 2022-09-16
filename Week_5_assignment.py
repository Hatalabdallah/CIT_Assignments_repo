# Using classes, Create a basic banking application with the following features:

# Create a class called BankAccount with the following attributes:

# account_number - a string
# balance - a float
# owner - a string
# type - a string

class BankAccount:

    def __init__(self, account_number, balance, owner, type):
        self.account_number = str(account_number)
        self.balance = float(balance)
        self.owner = str(owner)
        self.type = str(type)

    def __repr__(self):
        return "Account Number: {} \nBalance: {} \nAccount Holder: {} \nAccount Type: {}"\
            .format(self.account_number, self.balance, self.owner, self.type)

# Create a class called Bank with the following attributes:

# name - a string
# accounts - a list of BankAccount objects

class Bank:
    def __init__(self, name, accounts):
        self.name = str(name)
        self.accounts = accounts


    def __repr__(self):
            return "Bank Name: {}".format(self.name)

    def create_account(self, account):
        self.accounts.append(account)

# Create a class called Customer with the following attributes:

# name - a string
# accounts - a list of BankAccount objects

class Customer:

    def __init__(self, name, accounts):

        self.name = str(name)
        self.accounts = accounts

    def __repr__(self):
        return "Customer Name: {}".format(self.name)

    def create_account(self, account):
        self.accounts.append(account)
    


# Create a class called Transactions with the following attributes:

#  1. `account` - a `BankAccount` object
#  2. `amount` - a float
#  3. `type` - a string

class Transactions:

    def __init__(self, ammount, type, account):

        self.ammount = float(ammount)
        self.type = str(type)
        self.account = account


    def show_Transactions(self):

        def deposit(self):

            if self.type == "Deposit":
                ammount = float(input("Enter amount to be deposited: "))
                self.balance += ammount
                print("Amount Deposited: ",ammount)

        def withdraw(self):
            if self.type == "Withdraw":
                ammount = float(input("Enter amount to withdraw: "))
                if self.balance>=ammount:
                    self.balance -= ammount
                    print("You withdraw: ",ammount)
                else:
                    print("Insufficient balance ")


bank = Bank("Stanbic", [])

customer = Customer("Elprofessor", [])

bank_account = BankAccount("12367888A", 1000.0, "Elprofessor", "Current")

bank.create_account(bank_account)

customer.create_account(bank_account)

print(bank)

print(customer)

print(bank_account)

transaction = Transactions(1000.0, "Deposit", bank_account)

transaction.show_Transactions()
