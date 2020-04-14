class Bank:
		
	def Sel_Menu():
		Text='''
		-------Menu-------
		1. Open an account
		2. Make a deposit
		3. Withdrawal
		4. Account info
		5. Quit
		Selection : '''
		Sel_Num = input(Text)
		return Sel_Num
	
	def Open_account():
		print('\n-----Open an account-----')
		Sel_num = input('NormalAccount : 1 \nHighcreditAccount : 2 \nSelection : ')
		
		if Sel_num == '1':
			Account_ID = input('Account ID : ')
			Name = input('Name : ')
			first_deposit = int(input('First Deposit : '))
			info_list.append(NormalAccount(Account_ID, Name, first_deposit))
		elif Sel_num == '2':
			Account_ID = input('Account ID : ')
			Name = input('Name : ')
			first_deposit = int(input('First Deposit : '))
			Rank = input('1 to A, 2 to B, 3 to C : ')
			
			if Rank == '1': 
				Rank = 'A'
			elif Rank == '2': 
				Rank = 'B'
			elif Rank == '3':
				Rank = 'C'
			else:
				print('Wrong selection')
			
			info_list.append(HighcreditAccount(Account_ID, Name, first_deposit, Rank))
	
	def Find_data(data,account_num):
			for i in range(0,len(data)):
				if data[i].Account_ID == account_num:
					return i
					
	def Make_deposit():
		print('\n------Make a deposit------')
		account_num = input('Account ID :')
		Amount = int(input('Deposit amount : '))
		Index = Bank.Find_data(info_list,account_num)
		info_list[Index].Deposit += int(Amount + info_list[Index].Deposit*info_list[Index].Interest_rate)
	
	def Withdrawal():
		print('\n------Withdrawal------')
		account_num = input('Account ID :')
		Amount = -int(input('Withdrawal amount : '))
		
		Index = Bank.Find_data(info_list,account_num)
		info_list[Index].Deposit += int(Amount + info_list[Index].Deposit*info_list[Index].Interest_rate)

	def Print_account():
		for i in range(0,len(info_list)):
			print('\n----------')
			info_list[i].print_info()
			print('----------')

class NormalAccount:
	def __init__(self,Account_ID, Name, Deposit, Interest_rate=0.03):
		self.Account_ID = Account_ID
		self.Name = Name
		self.Deposit = Deposit
		self.Interest_rate = Interest_rate
	
	def print_info(self):
		print('Account ID : '+self.Account_ID)
		print('Name : '+self.Name)
		print('Deposit : '+str(self.Deposit))
		print('Interest rate : '+str(self.Interest_rate))

		
class HighcreditAccount(NormalAccount):
	def __init__(self,Account_ID, Name, Deposit, Rank, Interest_rate=0.03):	
		super().__init__(Account_ID, Name, Deposit, Interest_rate)
		self.Rank = Rank
		if self.Rank == 'A':
			self.Interest_rate += 0.07
		elif self.Rank == 'B':
			self.Interest_rate += 0.04
		elif self.Rank == 'C':
			self.Interest_rate += 0.02
	
	def print_info(self):
		print('Account ID : '+self.Account_ID)
		print('Name : '+self.Name)
		print('Deposit : '+str(self.Deposit))
		print('Rank : '+self.Rank)
		print('Interest rate : '+str(self.Interest_rate))
	
if __name__=='__main__':
	
	info_list=[]
	
	while True:
		Sel_Num = Bank.Sel_Menu()
		
		if Sel_Num == '1':
			Bank.Open_account()
		
		elif Sel_Num == '2':
			Bank.Make_deposit()
		
		elif Sel_Num == '3':
			Bank.Withdrawal()
			
		elif Sel_Num == '4':
			Bank.Print_account()
		
		elif Sel_Num == '5':
			break

		else:
			print('Select the correct number!')
