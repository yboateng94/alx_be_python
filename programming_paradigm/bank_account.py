class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current balance: ${self.account_balance:.2f}")

# Example usage:
if __name__ == "__main__":
    account = BankAccount(100)
    account.deposit(50)
    account.withdraw(75)
    account.display_balance()  # Output: Current balance: $75.00
