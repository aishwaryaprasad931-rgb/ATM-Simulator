# Simple ATM Simulator

correct_pin = "1234"
balance = 5000.00


def check_balance():
    print(f"\nYour current balance is: ₹{balance:.2f}")


def deposit_money():
    global balance

    amount = float(input("Enter amount to deposit: ₹"))

    if amount <= 0:
        print("Please enter a valid amount.")
    else:
        balance += amount
        print(f"₹{amount:.2f} deposited successfully.")


def withdraw_money():
    global balance

    amount = float(input("Enter amount to withdraw: ₹"))

    if amount <= 0:
        print("Please enter a valid amount.")

    elif amount > balance:
        print("Insufficient balance.")

    else:
        balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")


def atm_menu():
    while True:
        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("===============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit_money()

        elif choice == "3":
            withdraw_money()

        elif choice == "4":
            print("\nThank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    print("================================")
    print("       WELCOME TO ATM")
    print("================================")

    attempts = 3

    while attempts > 0:
        pin = input("Enter your 4-digit PIN: ")

        if pin == correct_pin:
            print("\nPIN verified successfully!")
            atm_menu()
            break

        else:
            attempts -= 1
            print("Incorrect PIN.")

            if attempts > 0:
                print(f"Attempts remaining: {attempts}")
            else:
                print("Too many incorrect attempts.")
                print("Your account is temporarily blocked.")


if __name__ == "__main__":
    main()