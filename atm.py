balance = 500
choice = 0

while choice != 4:
    print("""
    welcome to the ATM
          1. check balance
          2. deposite money
          3. withdraw money
          4. exit
        """)
    choice = int(input("your choice: "))
    if choice == 1:
        print("your balance is: " + str(balance) + "$")
    
    elif choice == 2:
        deposit_amount = float(input("enter your deposit amount: "))
        if deposit_amount >0:
            balance = balance + deposit_amount
            print(str(deposit_amount) + "$" + " deposited. new balance is " + str(balance) +"$")

        else:
           print("deposit amount must be positive")
        
    elif choice == 3:
        withdraw_amount = float(input("enter your withdraw amount: "))
        if withdraw_amount < balance:
           balance = balance - withdraw_amount
           print(str(withdraw_amount) + "$" + "withdrawn. new balance is" + str(balance) +"$")
        else:
            print("invalid withdrawal amount")
    
    elif choice == 4:
        print("thank you for using the ATM")

    else:
        print ("Invalid choice")
        
    
        



    

        
    

    