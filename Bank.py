from Account import Account
from texttable import Texttable

bankAccount = []


def addAccount():
    i = 1
    ans = 'y'
    print("==================\nAdd a bank account\n==================")
    while ans == 'y':
        accountType = input("Which type of account would you like to open (S: Saving / C: Chequing)? ").lower()
        while accountType != 'c' and accountType != 's':
            print("Incorrect Value.., please try again!")
            accountType = input("Type Here: ")

        if accountType == 's':
            print()
            print("\t\t**** Generating Saving Account ****\n")
            print(f"======= Client No.{i}")
            accID = Account.getAccountID()
            print(f"Account No. {accID}")
            accType = Account.getAccountType(accountType)
            print(f"Account type: {accType}")
            fName = input("Enter Client first name? ")
            lName = input("Enter Client last name? ")
            age = int(input("Enter Client age? "))
            balance = Account.getInitDepositValue(accountType)

            client = Account(accID, accType, fName, lName, age, balance)
            bankAccount.append(client)

            print(client)

            i += 1

        elif accountType == 'c':
            print()
            print("\t\t**** Generating chequing Account ****\n")
            print(f"======= Client No.{i}")

            accID = Account.getAccountID()
            print(f"Account No. {accID}")
            accType = Account.getAccountType(accountType)
            print(f"Account type: {accType}")
            fName = input("Enter Client first name? ")
            lName = input("Enter Client last name? ")
            age = int(input("Enter Client age? "))
            balance = Account.getInitDepositValue(accountType)

            client = Account(accID, accType, fName, lName, age, balance)
            bankAccount.append(client)

            print(client)
            i += 1
        ans = input("Would you like to add another client..? Press( y or n return to Main Menu) ").lower()
        if ans == 'n':
            print()


def removeAccount():
    ans = 'y'
    while ans == 'y':
        accID = int(input("Enter Client account number: "))
        for acc in bankAccount:
            if accID == acc.getAccNum:
                bankAccount.remove(acc)
                print(f"successfully.., Account No. {str(accID)} has been removed")
            else:
                print(f"Error! Account No. {str(accID)} not found")
        ans = input("Would you like to remove another client..? Press( y or n return to Main Menu) ").lower()
        if ans == 'n':
            print()


def displayParticularAccount():
    ans = 'y'
    while ans == 'y':
        accID = int(input("Enter Client account number: "))
        for acc in bankAccount:
            if accID == acc.getAccNum:
                print(acc)
            else:
                print(f"Error! Account No. {str(accID)} not found")
        ans = input("Would you like to remove another client..? Press( y or n return to Main Menu) ").lower()
        if ans == 'n':
            print()


def depositAmount():
    ans = 'y'
    while ans == 'y':
        accID = int(input("Enter Client account number: "))
        for acc in bankAccount:
            if accID == acc.getAccNum:
                deposit = float(input("Enter Amount to deposit? "))
                while deposit < 1:
                    print("Incorrect Amount.., please try again!")
                    deposit = float(input("Type Here: "))
                print("Deposit successfully...!")
                acc.setBalance += deposit
            else:
                print(f"Error! Account No. {str(accID)} not found")
        ans = input("Would you like to remove another client..? Press( y or n return to Main Menu) ").lower()
        if ans == 'n':
            print()


def withdrawalAmount():
    ans = 'y'
    while ans == 'y':
        accID = int(input("Enter Client account number: "))
        for acc in bankAccount:
            if accID == acc.getAccNum:
                withdraw = float(input("Enter Amount to withdraw? "))
                while withdraw > acc.getBalance and withdraw < 1:
                    print("Incorrect Amount.., please try again!")
                    withdraw = float(input("Type Here: "))
                print("Withdraw successfully...!")
                acc.setBalance -= withdraw
            else:
                print(f"Error! Account No. {str(accID)} not found")
        ans = input("Would you like to remove another client..? Press( y or n return to Main Menu) ").lower()
        if ans == 'n':
            print()


def displayListOfClients():
    i = 1
    j = 1
    table = Texttable()
    heading = ["Account No.", "Account Type", "Client First Name", "Client Last Name", "Client Age", "Balance"]
    # x = [[]]
    bankAccount.sort(key=lambda a: a.getBalance)

    print("Ascending Order by Balance")
    table.header(heading)
    for acc in bankAccount:
        print(acc)

    bankAccount.sort(key=lambda x: x.getBalance, reverse=True)
    print("Descending Order by Balance")
    for acc_ in bankAccount:
        print(acc_)


def displayAverageBalance():
    sum = 0
    for acc in bankAccount:
        sum += acc.getBalance
    print("Average balance:", sum / len(bankAccount))


def displayTotalBalance():
    sum = 0
    for acc in bankAccount:
        sum += acc.getBalance
    print("Total balance:", sum)


def default():
    print("Unknown selection..!")

    returnKey = input("return to Main Menu.... enter (R)").lower()
    if returnKey == "R":
        main()


def main():
    print("""
=========================== Banking Management System ============================
1.	Add a bank account.
2.	Remove a bank account.
3.	Display the information of a particular client’s account.
4.	Apply a deposit to a particular account.
5.	Apply a withdrawal from a particular account.
6.	Display the list of clients according to their balance.
7.	Display the average balance value of the accounts.
8.	Display the total balance value of the accounts.
9.	Exit the application.
=========================== +-+-+-+-+-+-+-+-+-+-+-+ =============================
            """)
