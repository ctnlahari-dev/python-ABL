balance = 5000

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")

choice = int(input("Enter your choice: "))

if choice == 1:
    amount = float(input("Enter deposit amount: "))

    if amount > 0:
        balance = balance + amount
        print("Updated Balance: Rs.", balance)
    else:
        print("Invalid amount")

elif choice == 2:
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid amount")
    elif amount <= balance:
        balance = balance - amount
        print("Updated Balance: Rs.", balance)
    else:
        print("Insufficient balance")

elif choice == 3:
    print("Current Balance: Rs.", balance)

else:
    print("Invalid choice")
