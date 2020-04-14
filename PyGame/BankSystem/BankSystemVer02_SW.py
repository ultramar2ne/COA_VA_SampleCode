class Account:
    # 부모클래스
    def __init__(self, num, name, money):
        self._id = num
        self._name = name
        self._money = int(money)

    def get_id(self):
        return self._id

    def withdraw(self):
        with_money = int(input("출금액: "))
        if with_money <= self._money:
            self._money = self._money - int(with_money)
            print("출금완료")
            print("출금 후 잔액 : ", self._money)
            print("\n")
        else:
            print("잔액이 부족합니다.\n")

    def deposit(self):
        dep_money = input("입금액: ")
        self._money = self._money + int(dep_money)
        print("입금완료\n")

    def info_print(self):
        print("계좌ID : ", self._id)
        print("이름 : ", self._name)
        print("잔액 : ", self._money)
        print("\n")


class NormalAccount(Account):
    # 보통예금계좌 클래스 Account 의 자식 클래스
    def __init__(self, num, name, money, rate):
        super().__init__(num, name, money)
        self._rate = rate

    def deposit(self):
        dep_money = input("입금액: ")
        self._money = int(((1 + self._rate * 0.01) * self._money) + int(dep_money))
        print("잔액 : ", self._money)
        print("입금완료\n")

    def info_print(self):
        print("계좌ID : ", self._id)
        print("이름 : ", self._name)
        print("잔액 : ", self._money)
        print("이자율 : ", self._rate)
        print("\n")


class HighCreditAccount(Account):
    # 신용신뢰계좌 클래스 Account 의 자식 클래스
    def __init__(self, num, name, money, rate, rank):
        super().__init__(num, name, money)
        self._normal_rate = rate  # 기본금리
        self._rank = rank  # 신용등급 A == 1, B == 2, C == 3
        if rank == 1:
            self._abc_rank = "A"
            self._rank_rate = 7  # 우대금리
        elif rank == 2:
            self._abc_rank = "B"
            self._rank_rate = 4  # 우대금리
        elif rank == 3:
            self._abc_rank = "C"
            self._rank_rate = 2  # 우대 금리
        self._real_rate = self._normal_rate + self._rank_rate  # 실제금리

    def deposit(self):
        dep_money = input("입금액: ")
        self._money = int(((1 + self._real_rate * 0.01) * self._money) + int(dep_money))
        print("잔액 : ", self._money)
        print("입금완료\n")

    def info_print(self):
        print("계좌 ID : ", self._id)
        print("이름 : ", self._name)
        print("잔액 : ", self._money)
        print("이자율 : {} % \t  (기본 금리 {}% + 우대금리{}%)".format(self._real_rate, self._normal_rate, self._rank_rate))
        print("신용등급 :", self._abc_rank)
        print("\n")


class App:
    def __init__(self):
        print("COALA Bank\n")
        self.account_list = []

    def search_id(self):
        ID = input("계좌 ID : ")
        for account in self.account_list:
            if ID == account.get_id():
                return self.account_list.index(account)
        return -1

    def info(self):
        for account in self.account_list:
            account.info_print()

    def run(self, key):
        if key == 1:
            print("[계좌 종류 선택]")
            print("1. 보통예금계좌\t 2. 신용신뢰계좌")
            selection = int(input("선택 : "))
            account_id = input("계좌 ID : ")
            name = input("이름 : ")
            money = input("입금액 : ")
            rate = int(input("이자율: "))
            # 계좌 선택
            if selection == 1:
                account = NormalAccount(account_id, name, money, rate)
                self.account_list.append(account)
            elif selection == 2:
                rank = int(input("1toA , 2toB , 3to C"))
                account = HighCreditAccount(account_id, name, money, rate, rank)
                self.account_list.append(account)
            else:
                print("입력이 잘못되었습니다.")
            return True

        elif key == 2:
            idx = self.search_id()
            if idx != -1:
                self.account_list[idx].deposit()
            else:
                print("없는 계좌번호입니다.\n")

            return True

        elif key == 3:
            idx = self.search_id()
            if idx != -1:
                self.account_list[idx].withdraw()
            else:
                print("없는 계좌번호입니다.")
            return True

        elif key == 4:
            self.info()
            return True

        elif key == 5:
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
            key = int(input("선택: "))
            cmd = self.run(key)


if __name__ == "__main__":
    app = App()
    app.command()
