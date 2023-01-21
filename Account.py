import random
from texttable import Texttable

class Account:
    accID = None
    accTy = None
    aTy = None
    initDeposit = None


    def __init__(self, accNum, accType, fName, lName, age, balance):
        self.__accNum = accNum
        self.__accType = accType
        self.__balance = balance
        self.__fName = fName
        self.__lName = lName
        self.__age = age

    def __str__(self):
        table = Texttable()
        table.add_rows([
            ["Account No.", "Account Type", "Client First Name", "Client Last Name", "Client Age", "Balance"],
            [self.__accNum, self.__accType, self.__fName, self.__lName, self.__age, self.__balance],
        ])
        # info = f"Account No.: {str(self.__accNum)}\n" \
        #        f"Account Type: {self.__accType}\n" \
        #        f"Client First Name: {self.__fName}\n" \
        #        f"Client Last Name: {self.__lName}\n" \
        #        f"Client Age: {str(self.__age)}\n" \
        #        f"Balance: {str(self.__balance)}\n"
        return table.draw()

    @property
    def getAccNum(self):
        return self.__accNum

    @property
    def getAccType(self):
        return self.__accType

    @property
    def getBalance(self):
        return self.__balance

    @property
    def getFirstName(self):
        return self.__fName

    @property
    def getLastName(self):
        return self.__lName

    @property
    def getAge(self):
        return self.__age

    @getFirstName.setter
    def setAge(self, value):
        self.__age = value

    @getLastName.setter
    def setLastName(self, value):
        self.__lName = value

    @getFirstName.setter
    def setFirstName(self, value):
        self.__fName = value

    @getAccNum.setter
    def setAccNum(self, value):
        self.__accNum = value

    @getAccType.setter
    def setAccType(self, value):
        self.__accType = value

    @getBalance.setter
    def setBalance(self, value):
        self.__balance = value

    @staticmethod
    def getAccountID() -> int:
        accID = random.randrange(10000, 10099)
        return accID

    @staticmethod
    def getAccountType(accTy: str) -> str:
        accountType = {'Chequing': {'c': 1000}, 'Saving': {'s': 500}}
        for key, value in accountType.items():
            for key2, value2 in value.items():
                if accTy == key2:
                    return key

    @staticmethod
    def getInitDepositValue(aTy: str) -> float:
        accountType = {'Chequing': {'c': 1000}, 'Saving': {'s': 500}}
        for key, value in accountType.items():
            for key2, value2 in value.items():
                if aTy == key2:
                    initDeposit = float(input(f"To complete your registration Please do deposit"
                                              f" {value2}$ ..! "))
                    while initDeposit < value2:
                        print("Incorrect Amount.., please try again!")
                        initDeposit = float(input("Type Here: "))
                    print("Deposit successfully...!")
                    return initDeposit
