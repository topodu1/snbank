#Simple Banking System with FileSystem
#Temitope Odulate
#topeodulate@gmail.com

#I chose to define the functions and just run the whole program with three functions
import random


def staff_login():

    print("Welcome to the Staff Login Portal, We require your username and password to login")
    staff_details = True
    while staff_details:
        staff_username = str(input("what is your username: "))
        staff_pwd = str(input("what is your password: "))

        file = open("staff.txt", "r")
        for row in file:
            field = row.split(",")
            username = str(field[0])
            password = str(field[1])

            if staff_username == username and staff_pwd == password:
                print("Login Successful!!!")
                print("Welcome " + username)
                print("Please enter 1 through 3 for the corresponding action")

                staff_details = False
                break
        else:
            print("oops, that was incorrect")
            print("please try again")




def staff_options():
    while True:

        print("1 > Create New Bank Account")
        print("2 > Check Account Details")
        print("3 > logout")
        staff_select = int(input("> "))
        if staff_select == 1:
            print("Please enter the following details: ")
            acct_name = input(str("Account Name> "))
            open_bal = str(input("Opening Balance> "))
            acct_type = input(str("Account Type> "))
            acct_email = input(str("Account Email> "))
            acct_num = str(random.randint(00000, 50000))
            print(f" {acct_name}'s Account number is {acct_num}")
            customer_info = open("customer.txt", "a")
            customer_info.write(acct_name)
            customer_info.write(",")
            customer_info.write(open_bal)
            customer_info.write(",")
            customer_info.write(acct_type)
            customer_info.write(",")
            customer_info.write(acct_email)
            customer_info.write(",")
            customer_info.write(acct_num)
            customer_info.write("\n")
            customer_info.close()
            print("New Bank Account Created and Saved. ")
        if staff_select == 2:
            while True:
                print("Please Account Number to check details: ")
                accountnum = str(input("> "))
                file_check = open("customer.txt", "r")
                for row in file_check:
                    field = row.split(",")
                    acc_name = str(field[0])
                    amount = str(field[1])
                    acc_type = str(field[2])
                    acc_mail = str(field[3])
                    acc_num = str(field[4])
                    laststr = len(acc_num) - 1
                    acc_num = acc_num[0:laststr]
                    if str(accountnum) == acc_num:
                        print(f"Account Name> {acc_name}")
                        print(f"Opening Balance> {amount}")
                        print(f"Account Type> {acc_type}")
                        print(f"Account Email> {acc_mail}")
                        file_check.close()
                        break
                else:
                    print("Invalid Account Number")
                break

        if staff_select == 3:
            break


def simple_bank():
    while True:
        try:
            print("Enter 1 for Staff login: ")
            print("Enter 2 for Close App: ")
            num = int(input("> "))
            if num == 1:
                staff_login()
                staff_options()
            else:
                print("Have a nice day")
                break
        except ValueError:
            print("Invalid Input")


simple_bank()
