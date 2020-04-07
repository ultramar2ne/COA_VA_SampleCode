class Account:
    def __init__(self, num, name, money):
        self.id = num
        self.Name = name
        self.money = int(money)

    def deposit(self):
        depmoney = input("입금액: ")
        self.money = self.money + int(depmoney)
        print("입금완료\n")

    def withdraw(self):
        withmoney = int(input("출금액: "))
        if withmoney <= self.money:
            self.money = self.money - int(withmoney)
            print("출금완료")
            print("출금 후 잔액 : ", self.money)
            print("\n")
        else:
            print("잔액이 부족합니다.\n")

    def infoprint(self):
        print("계좌ID : ", self.id)
        print("이름 : ", self.Name)
        print("잔액 : ", self.money)
        print("\n")

class App:
    def __init__(self):
        print("COALA Bank\n")
        self.accountlist = []

    def searchID(self):
        ID = input("계좌ID : ")
        for account in self.accountlist:
            if account.id == ID:
                return self.accountlist.index(account)
        return -1

    def info(self):
        for account in self.accountlist:
            account.infoprint()

    def run(self, key):
        if int(key) == 1:
            print("[입 금]")
            accountID = input("계좌ID : ")
            name = input("이름 : ")
            money = input("입금액 : ")
            tmp = Account(accountID, name, money)
            self.accountlist.append(tmp)
            return True

        elif int(key) == 2:
            idx = self.searchID()
            if idx != -1:
                self.accountlist[idx].deposit()
            else:
                print("없는 계좌번호입니다.\n")

            return True

        elif int(key) == 3:
            idx = self.searchID()
            if idx != -1:
                self.accountlist[idx].withdraw()
            else:
                print("없는 계좌번호입니다.")
            return True

        elif int(key) == 4:
            self.info()
            return True

        elif int(key) == 5:
            return False

        else:
            print("Wrong Selection\n")
            return True

    def command(self):
        cmd = True
        while cmd:
            print("----- Menu -----")
            print("1. 계좌개설")
            print("2. 입금")
            print("3. 출금")
            print("4. 계좌정보 전체 출력")
            print("5. 프로그램종료")
            key = input("선택: ")
            cmd = self.run(key)


if __name__ == "__main__":
        app = App()
        app.command()
