import Bank
from Bank import *

if __name__ == '__main__':
    main()
    option = int(input("Enter your option "))

    while True:
        match option:
            case 1:
                Bank.addAccount()
            case 2:
                Bank.removeAccount()
            case 3:
                Bank.displayParticularAccount()
            case 4:
                Bank.depositAmount()
            case 5:
                Bank.withdrawalAmount()
            case 6:
                Bank.displayListOfClients()
            case 7:
                Bank.displayAverageBalance()
            case 8:
                Bank.displayTotalBalance()
            case 9:
                print("yalla...Bish Bish....Good Bye...!!!")
                quit()
            case _:
                default()
        main()
        option = int(input("Enter your option "))
