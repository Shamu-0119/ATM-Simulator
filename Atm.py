balance = 20000
password = 12345

print("Welcome to the My ATM :) ")
input("press Enter to Continue")
pin = int(input("Enter your pin "))
active = True
if pin == password:
    print(" *************************************")
    while active:
        print(" 1: Account information ")
        print(" 2: Check balance ")
        print(" 3: Withdraw ")
        print(" 4: Deposit ")
        print(" 5: Exit ")

        option = int(input(" What would you like to do: "))
        print(" ******************************")

        # check account information..........:)
        if option == 1:
            print(" Name: Shamu Gollapudi ")
            print(" Account_no.: 1275489293 ")
            print(" Validity: 12/24 ")
            print(" ********************************** ")

        # Check balance
        elif option == 2:
            print(" Balance: Rs " + str(balance))
            print("**********************************")

        # Withdraw amount
        elif option == 3:
            print(" Total amount available for withdrawal is: Rs " + str(balance))
            while True:
                withdraw = int(input(" Withdraw: Rs "))
                if withdraw > balance:
                    print(" Cannot withdraw more than available balance ")
                    continue
                balance = balance-withdraw
                break
            print("*******************************************")

        # Deposit
        elif option == 4:
            deposit = int(input(" How much would you like to deposit: Rs "))
            print(" You Deposit " + str(deposit) + " Rs ")
            balance = balance+deposit
        # Exit
            print("************************************************")

        elif option == 5:
            print(" Thank you for your visit to My ATM :) ")
            print(" HAVE A GOOD DAY :) ")
            break
    else:
        print("Enter correct Password ")
