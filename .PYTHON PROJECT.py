pin = "1234"
balance = 5000

print("===== ATM MANAGEMENT SYSTEM =====")

user_pin = input("Enter your ATM PIN: ")

if user_pin == pin:
    print("Login Successful!")

    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your Balance is:", balance)

        elif choice == "2":
            amount = int(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print("Money Deposited Successfully!")
                print("New Balance:", balance)
            else:
                print("Invalid Amount!")

        elif choice == "3":
            amount = int(input("Enter withdraw amount: "))
            if amount > 0 and amount <= balance:
                balance -= amount
                print("Please collect your money.")
                print("Remaining Balance:", balance)
            else:
                print("Invalid Amount or Insufficient Balance!")

        elif choice == "4":
            print("Thank You for Using ATM!")
            break

        else:
            print("Invalid Choice!")

else:
    print("Incorrect PIN!")