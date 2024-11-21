def show_balance(balance):
    print("----------------------")
    print(f"Your balance is: ₹{balance:.2f}")
    print("----------------------")

def deposit():
    print("----------------------")
    amount = float(input("Enter an amount to be deposited: "))
    print("----------------------")

    if amount <= 0:
        print("----------------------")
        print("Amount must be greater than 0")
        print("----------------------")
        return 0
    else:
        return amount

def withdraw(balance):
    print("----------------------")
    amount = float(input("Enter an amount to be withdrawn: "))
    print("----------------------")

    if amount > balance:
        print("----------------------")
        print("Insufficient funds")
        print("----------------------")
        amount = 0
    elif amount <= 0:
        print("----------------------")
        print("Amount must be greater than 0")
        print("----------------------")
        amount = 0

    return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("----------------------")
        print("    Banking System")
        print("----------------------")
        print("1.Show Balance \n2.Deposit \n3.Withdraw \n4.Exit")
        print("----------------------")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("----------------------")
            print("This is not a valid choice")
            print("----------------------")

    print("----------------------")
    print("Thank you! have a nice day! :)")

if __name__ == "__main__":
    main()