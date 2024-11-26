def show_balance(balance):
    print(f"Your balance is: ₹{balance:.2f}.")

def deposit():
    while True:
        amount = input("\nEnter an amount to be deposited: ")

        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be greater than 0.")
                continue
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue

        return amount

def withdraw(balance):
    while True:
        amount = input("\nEnter an amount to be withdrawn: ")

        try:
            amount = float(amount)
            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount > balance:
                print(f"Insufficient funds. Your balance is ₹{balance}")
            else:
                return amount
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    balance = 0

    while True:
        print("\n**** Banking System ****")
        choice = input("Enter your choice - 1 to Show Balance, 2 for Deposit, 3 for Withdrawal, 4 for Exit: ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            deposited_amount = deposit()
            balance += deposited_amount
            print(f"₹{deposited_amount} is deposited successfully!")
        elif choice == '3':
            withdrawn_amount = withdraw(balance)
            balance -= withdrawn_amount
            print(f"₹{withdrawn_amount} is withdrawn successfully!")
        elif choice == '4':
            confirm_exit = input("\nAre you sure you want to exit? (y/n): ")
            if confirm_exit.lower() == 'y':
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    print("Thank you! have a nice day! :)")

if __name__ == "__main__":
    main()