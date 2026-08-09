# Simple ATM Simulator 

balance = 500

print("===== WELCOME TO ATM =====")

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Your balance is: $", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: $"))
        balance += amount
        print("Deposit successful! ")
        print("New balance: $", balance)

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: $"))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful! ")
            print("New balance: $", balance)
        else:
            print("Insufficient balance! ")

    elif choice == "4":
        print("Thank you for using our ATM. ")
        break

    else:
        print("Invalid choice! Please try again. ")