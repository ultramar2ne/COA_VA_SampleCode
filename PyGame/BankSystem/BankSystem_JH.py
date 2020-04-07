def Sel_Menu():
	Text='''
	-------Menu-------
	1. Open an account
	2. Make a deposit
	3. Withdrawl
	4. Account info
	5. Quit
	Selection : '''
	Sel_Num=input(Text)
	return Sel_Num

def find_name(info_list,Account_num):
	for i in range(0,len(info_list)):
		if info_list[i].Account_ID == Account_num: return info_list[i].Name
	return 0

def load_data():
	info_list=[]
	
	with open('infofile.txt','r') as f:
		while True:
			line=f.readline()
			
			if line == '':
				break
			
			account_num=''
			user_name=''
			deposit=''
			count=0
			
			for i in range(0,len(line)):
				if line[i]=='/':
					count+=1
				elif count==0:
					account_num+=line[i]
				elif count==1:
					user_name+=line[i]
				elif count==2:
					deposit+=line[i]

			exec("%s%s=bank(\'%s\',\'%s\',\'%s\')" % (user_name, account_num, account_num, user_name, deposit))
			exec("info_list.append(%s%s)" % (user_name,account_num))
			
	return info_list

def save_data(info_list):
	with open('infofile.txt','w') as f:	
		for i in range(0,len(info_list)):
			account_num=info_list[i].Account_ID
			user_name=info_list[i].Name
			deposit=info_list[i].Deposit
			f.write(account_num + '/' + user_name + '/' + deposit + '/' + '\n')

class bank:
	def __init__(self,account_num, user_name, first_deposit):
		self.Account_ID=account_num
		self.Name=user_name
		self.Deposit=first_deposit
	
	def in_out(self, Amount):
		self.Deposit=str(int(self.Deposit)+Amount)

if __name__=='__main__':
	
	info_list=load_data()
	
	while True:
		Sel_Num=Sel_Menu()
		
		if Sel_Num == '1':
			print('-----Open an account-----')
			account_num=input('Account ID : ')
			user_name=input('Name : ')
			first_deposit=input('First Deposit : ')
			exec('%s%s=bank(\'%s\',\'%s\',\'%s\')' % (user_name, account_num, account_num, user_name, first_deposit))
			exec('info_list.append(%s%s)' % (user_name,account_num))
		
		elif Sel_Num == '2':
			print('------Make a deposit------')
			account_num=input('Account ID :')
			Amount=int(input('Deposit amount : '))
			user_name=find_name(info_list, account_num)
			if user_name == 0:
				print('Wrong Account ID')
				pass
			exec('%s%s.in_out(%s)' % (user_name,account_num,Amount))
		
		elif Sel_Num == '3':
			print('------Withdrawal------')
			account_num=input('Account ID :')
			Amount=-int(input('Withdrawal amount : '))
			user_name=find_name(info_list, account_num)
			if user_name == 0:
				print('Wrong Account ID')
				pass
			exec('%s%s.in_out(%s)' % (user_name,account_num,Amount))
			
		elif Sel_Num == '4':
			for i in range(0,len(info_list)):
				print('----------')
				print(info_list[i].Account_ID)
				print(info_list[i].Name)
				print(info_list[i].Deposit)
				print('----------')
		
		elif Sel_Num == '5':
			save_data(info_list)
			break
			
		else:
			print('Select the correct number!')
	save_data(info_list)
