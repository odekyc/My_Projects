class Views:
	def __init__(self):
		self.userrole=None
		self.ownname=None
		self.ownpassword=None
		self.newuserchoice=None
		self.newusername=None
		self.newuserpassword=None
		self.clientname=None
		self.clientpassword=None
		self.action=None
		self.clientbalance=None
		self.accounttype=None
		self.clientamount=None
		self.otherclientname=None
		self.clientaccountnum=None
		self.clientaccountnum2=None
		self.accountnum=None
		self.accountnum2=None
		self.amount=None
		self.neworexuser=None
		self.chosenbankername=None
		self.newcreateaccountnum=None
		self.logoutchoice=None
		
	def role(self):
		self.userrole=input ("Please enter whether you are a banker or client, enter 'b' for banker, enter 'c' for client :")
		self.userrole.lower()
		if(self.userrole=='b'):
			self.ownname=input("please enter your banker username: ")
			self.ownpassword=input("please enter your banker password: ")
			
		elif(self.userrole=='c'):
			self.ownname=input("please enter your client username: ")
			self.ownpassword=input("please enter your client password: ")
			
		elif(self.userrole!='c' and self.role!='b'):
			print ("you didn't enter a valid input, please try again! ")
			return self.role()
			


	def createusermenu(self):
		print ("if you are a banker, you can create your own new account, if you are a client, you need to have a banker open an account for you!")
		self.newuserchoice=input("please enter if you are a banker or a client, enter 'b' for banker, enter 'c' for client : ")
		if (self.newuserchoice=='b'):
			self.newusername=input("if you are a banker- enter your new banker username : ")
			self.newuserpassword=input("if you are a banker- enter your new banker password : ")

			

		elif (self.newuserchoice=='c'):
			print ("you can't create your own new account, you need a banker to help you with it.")
			return self.role()

		elif (self.newuserchoice!='c' and self.newuserchoice!='b'):
			print ("invalid input, please try again!")
			return self.createusermenu()


	def firstmenu(self):
		self.neworexuser=input("please enter whether you are a new or existing user, enter 'n' for new user, enter 'e' for existing user : ")
		self.neworexuser.lower()
		if (self.neworexuser!='n' and self.neworexuser!='e'):
			print ("you didn't enter a valid input, please try again!")
			return self.firstmenu()
		elif (self.neworexuser=='n'):
			return self.createusermenu()
		elif (self.neworexuser=='e'):
			return self.role()

	

	def logout(self):

		self.logoutchoice=input("please enter whether you want to log out or not, enter 'y' for yes, 'n' for no : ")
		self.logoutchoice.lower()
		if (self.logoutchoice!='y' and self.logoutchoice!='n'):
			print ("invalid response, please enter again! ")
			return self.logout()

		elif (self.logoutchoice=='y'):
			return True

		elif (self.logoutchoice=='n'):
			return False

	def whattodo(self):
	
		if (self.userrole=='b'):
			print ("press 1 to create account for client")
			print ("press 2 to deposit for client")
			print ("press 3 to withdraw for client")
			print ("press 4 to transfer between clients ")
			print ("press 5 to display all of your client's bank accounts")
			self.action=input("please select one from the above choices : ")
			if (self.action!='1' and self.action!='2' and self.action!='3' and self.action!='4' and self.action!='5'):
				print ("you entered an invalid response, please enter again!")
				return self.whattodo()
			elif (self.action=='1' or self.action=='2' or self.action=='3' or self.action=='4' or self.action=='5'):
				self.action+='b'
				return self.getinfo()


		elif (self.userrole=='c'):
			print ("press 1 to deposit into own account")
			print ("press 2 to withdraw from own account")
			print ("press 3 to transfer between your acount and the account for another user")
			print ("press 4 to display all your bank accounts")
			self.action=input("please select one from the above choices : ")
			if (self.action!='1' and self.action!='2' and self.action!='3' and self.action!='4'):
				print ("you entered an invalid response, please enter again!")
				return self.whattodo()
			elif (self.action=='1' or self.action=='2' or self.action=='3' or self.action=='4'):
				self.action+='c'
				return self.getinfo()
			

			
		

	def getinfo(self):
		if (self.action=='1b'):
			self.clientname=input("please enter client username:")
			self.clientpassword=input("please enter client password:")
			self.accounttype=input("please enter the account type of the client :")
			balance=input("please enter the beginning balance for the account you are trying to create : ")
			self.clientbalance=float(balance)
			myaccountnum=input("please enter the account number you want to assign to this new account of your clent's:")
			self.newcreateaccountnum=int(myaccountnum)
		elif (self.action=='2b'):
			self.clientname=input("please enter client username:")
			self.clientamount=input("please enter the amount you want to deposit :")
			self.clientaccountnum=input("please enter the account number you want to make deposit:")


		elif (self.action=='3b'):
			self.clientname=input("please enter client username:")
			self.clientamount=input("please enter the amount you want to withdraw :")
			self.clientaccountnum=input("please enter the account number you want to withdraw from:")
			
		elif (self.action== '4b'):
			self.clientname=input("please enter client username you want to tranfer fund from:")
			
			self.otherclientname=input("please enter client username you want to transfer fund to :")
			
			self.clientaccountnum=input("please enter the account number you want to transfer from:")
			self.clientaccountnum2=input("please enter the account number you want to transfer to:")
			self.clientamount=input("please enter the amount you want to transfer :")
		elif (self.action=='5b'):
			self.clientname=input("please enter the client username you want to display all accounts info:")
			
			
		elif (self.action=='1c'):
			self.amount=input("please enter the amount you want to deposit :")
			self.accountnum=input("please enter the account number you want to make deposit:")
		elif (self.action=='2c'):
			self.amount=input("please enter the amount you want to withdraw :")
			self.accountnum=input("please enter the account number you want to withdraw from:")
		elif (self.action=='3c'):
			self.amount=input("please enter the amount you want to transfer :")
			self.otherclientname=input("please enter the username you want to transfer fund to :")
			self.accountnum=input("please enter you account number you want to transfer from:")
			self.accountnum2=input("please enter the other person's account number you want to transfer to:")





