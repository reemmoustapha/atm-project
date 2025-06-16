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
        print("your balance is: ")
    
    elif choice == 2:
        deposite_amount = float(input("enter your deposite amount: "))
        if deposite_amount >0:
            balance = balance + deposite_amount
            print(str(deposite_amount) + "$" + "deposited. new balance is" + str(balance) +"$")

        else:
           print("deposite amount must be positive")
        
    elif choice == 3:
        withdraw_amount = float(input("enter your withdraw amount: "))
        if withdraw_amount < balance:
           balance = balance - withdraw_amount
           print(str(withdraw_amount) + "$" + "withdrawn. new balance is" + str(balance) +"$")
        else:
            print("invalid withdrawal amount")
    
    elif choice == 4:
        print("thank you for using the ATM")

    
        
    
        



    

        
    

    