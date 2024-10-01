# Simple Banking System

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Successfully withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account holder: {self.account_holder}, Balance: ${self.balance}")

# Function to display the menu
def display_menu():
    print("\n=== Simple Banking System ===")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")
    print("===============================")

# Main function to run the banking system
def main():
    accounts = {}
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            name = input("Enter account holder's name: ")
            accounts[name] = BankAccount(name)
            print(f"Account created for {name}!")
            
        elif choice == "2":
            name = input("Enter account holder's name: ")
            if name in accounts:
                amount = float(input("Enter deposit amount: "))
                accounts[name].deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            name = input("Enter account holder's name: ")
            if name in accounts:
                amount = float(input("Enter withdrawal amount: "))
                accounts[name].withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            name = input("Enter account holder's name: ")
            if name in accounts:
                accounts[name].check_balance()
            else:
                print("Account not found.")

        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose again.")

# Run the banking system
if __name__ == "__main__":
    main()
