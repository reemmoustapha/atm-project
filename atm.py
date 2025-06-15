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
    
    if choice == 2:
        deposite = float(input("enter your deposite amount: "))
        if deposite >0:
            balance = balance + deposite
            print(str(deposite) + "$" + "deposited. new balance is" + )
        
    

    