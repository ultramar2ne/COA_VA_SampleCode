class Account:
    def __init__(self,accID, balance,name):
        self.accID = accID
        self.balance = balance
        self.name = name

    def DepositMoney(self, money):
        self.balance += money

    def WithdrawMoney(self, money):
        self.balance -= money

class AccountHandler:
    def ShowMenu(self):
        print("-----Menu-----")
        print("1. 계좌개설")
        print("2. 입    금")
        print("3. 출    금")
        print("4. 계좌정보 전체 출력")
        print("5. 프로그램 종료")

    def MakeAccount(self):
        print()
        print("[계좌개설]")
        id = int(input("계좌ID: " ))
        name = input("이 름: ")
        money = int(input("입금액: "))
        accountList.append(Account(id,money,name))

    def DepositMoney(self):
        print()
        print("[입  금]")
        id = int(input("계좌ID: " ))
        money = int(input("입금액: "))
        for i in range(len(accountList)):
            if (accountList[i].accID == id ):   
                accountList[i].DepositMoney(money)
                print("입금완료")
                break
        print ("존재하지 않는 id 입니다.")

    def WithdrawMoney(self):
        print()
        print("[출  금]")
        id = int(input("계좌ID: " ))
        money = int(input("출금액: "))
        for i in range(len(accountList)):
            if (accountList[i].accID == id):
                accountList[i].WithdrawMoney(money)
                print("출금완료")
                break
        print ("존재하지 않는 id 입니다.")

    def ShowAllAccInfo(self):
        for i in range(len(accountList)):
            print()
            print("계좌ID: %s"%(accountList[i].accID))
            print("이 름: %s"%(accountList[i].name))
            print("잔 액: %s"%(accountList[i].balance))
        print()

accountList = []

class main:
    accountHandler = AccountHandler()

    while(True):
        accountHandler.ShowMenu()
        choice = int(input("선택: "))

        if(choice == 1):
            accountHandler.MakeAccount()

        elif(choice == 2):
            accountHandler.DepositMoney()

        elif(choice == 3):
            accountHandler.WithdrawMoney()

        elif(choice == 4):
            accountHandler.ShowAllAccInfo()

        elif(choice == 5):
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다.")
