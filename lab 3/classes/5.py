class Account:
    def __init__(self, owner):
        self.owner = owner  # Set account owner
        self.balance = 0  # Initialize balance

    def deposit(self, amount):
        self.balance += amount  # Increase balance by deposit amount
        print("Deposited:", amount, ". New balance:", self.balance)  # Show new balance

    def withdraw(self, amount):
        if amount > self.balance:  # Check if there are sufficient funds
            print("Insufficient funds!")  # Notify if not enough money
        else:
            self.balance -= amount  # Decrease balance by withdrawal amount
            print("Withdrew:", amount, ". New balance:", self.balance)  # Show new balance

# Example Usage
account = Account("Alice")  # Create an account for Alice
account.deposit(100)  # Deposit $100
account.withdraw(50)  # Withdraw $50
account.withdraw(60)  # Attempt to withdraw $60 (should fail)
