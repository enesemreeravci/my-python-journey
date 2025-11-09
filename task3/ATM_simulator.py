
print("\nWelcome to the Virtual ATM!\n")

balance = 1000

while True:
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit\n")
    choose = int(input("Choose an option: "))
    if (choose == 1):
      print("Your balance is $", balance)
    elif (choose == 2):
       deposit = int(input("Enter amount to deposit: "))
       balance += deposit
       print("Deposit successfull! Your new balance is $",balance)
    elif (choose == 3):
        withdraw = int(input("Enter amount to withdraw: "))
        balance -= withdraw
        print("Withdraw successfull! Your new balance is $",balance)
    elif(choose == 4):
       print("Program is turning off! See you!")
       break
    else:
       print("Please review your choose")