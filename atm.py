# At the ATM you can deposit and withdraw money. You can also check balance.

balance = 50000

# Starting menu
"""Variables and input"""
# String manipulation /n /t //
print("Good morning//Good afternoon//Good evening, welcome to the ATM (print a random quote)\n")
print("We accept the following cards: maestro, mastercard, debit card")
print("Enter your card!")

# Enter pincode
print("\nPlease enter your pincode")
user_name = input("Pincode: ")

# Choice
print("\nWhat do you want to do:")
choice = input("Enter ('W' for withdrawal, 'D' for deposit, 'B' balance or 'C' for cancel) ").lower()
if choice == "w":
    # Withdrawal (choice amount)
    withdrawal_amount = int(input("What amount do you want to withdrawal: "))
    balance -= withdrawal_amount
elif choice == "d":
    deposit_amount = int(input("What amount do you want to deposit: "))
    balance += deposit_amount
elif choice == "b":
    print(f"Your balance: EUR {balance}")
elif choice == "c":
    print("Please wait for main menu")
else:
    print("Wrong button, please try again!")


# Wait
print("Please wait")

# Take out debit card
print("Please take out your debit card.")

# processing the money
print("Please wait, your withdrawal is being processed.")

# Take out money
print("Please take out your money.")

# receipt
receipt = input("Do you want a receipt? Press 'Y' or 'N' ").lower()
if receipt == "y":
    print("Please wait for receipt.")

# ready
print("Good buy! Till next time.")

"""Numbers"""
balance = 50000

# Deposit
balance += 1500
print(balance)

# Withdrawal
balance -= 25000
print(balance)

# Checking current balance
print(f"Your balance: EUR {balance}")

# What if the balance is not sufficient to withdraw?
print("Withdrawal is not possible, you have insufficient funds")

# Withdrawal
# Ask for denominations

# Error: show message and number of company which can be called

# Maintenance

# Keep track of the current amount of bills. If almost empty send message to fill

