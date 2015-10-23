import sqlite3
import datetime
import random
from createdbcsv import Database
from createdbcsv import CSV


usernamedic={}
userlist=[]
usernum=0


class Account:
	def __init__(self,begbalance, atype, accountnum):
		self.balance=begbalance
		
		self.accountnum=accountnum
		self.type=atype






class User:
	def __init__(self,username,password):
		self.username=username
		
		self.password=password
		self.time_created=datetime.datetime.now()
		self.accountslist=[]
		self.accountsdic={}
		self.accountindexnum=0

	def joinbankdate(self):

		return self.time_created
		

class Client(User):


	def __init__(self, username, password):
		self.permitlev="medium"
		super().__init__(username, password)



	def deposit(self, amount, myaccountnum):
	
		self.accountsdic[myaccountnum].balance+=amount
		print ("deposit completed- your new balance for this account is : "+str(self.accountsdic[myaccountnum].balance))
		return self.accountsdic[myaccountnum].balance
	

	def withdraw(self, amount, myaccountnum):
		
		if (amount>self.accountsdic[myaccountnum].balance):
			print ("withdraw cannot be completed- not enough balance")
		elif (amount<=self.accountsdic[myaccountnum].balance):
			self.accountsdic[myaccountnum].balance-=amount
			print ("withdraw completed- your new balance for this account is : "+str(self.accountsdic[myaccountnum].balance))
			return self.accountsdic[myaccountnum].balance

		

	def transfer(self,  amount , otherusername, ownaccountnum, otheraccountnum):
		
		if (amount>self.accountsdic[ownaccountnum].balance):
			print ("transfer cannot be completed- not enough balance")
		elif (amount<=self.accountsdic[ownaccountnum].balance):
			self.accountsdic[ownaccountnum].balance-=amount
			usernamedic[otherusername].accountsdic[otheraccountnum].balance+=amount
			print ("transfer completed- your new balance for this account is : "+str(self.accountsdic[ownaccountnum].balance))
			return self.accountsdic[ownaccountnum].balance
	def displayaccounts(self):
		for key in self.accountsdic:
			print ("for your "+self.accountsdic[key].type+" account with account number : "+str(self.accountsdic[key].accountnum))
			print ("your balance for this account is : " + str(self.accountsdic[key].balance))

class Banker(User):

	def __init__(self, username, password):
		self.permitlev="high"
		self.username=username
		
		self.password=password
		self.time_created=datetime.datetime.now()
		self.mycsv=CSV('clientlist')



	def createaccount(self, atype,begbalance, myusername, mypassword, myaccountnum):
		countfound=0
		self.mycsv.openreader()
		with self.mycsv.file:
			self.mycsv.dictreader()
			for row in self.mycsv.reader:
				if (myusername==row['Username'] ):
					countfound+=1
			if (countfound>0):
				print ("this client name already exists in our system, please try to log in as an existing client!")
				
			elif (countfound==0):
				userlist.append(Client(myusername, mypassword))
				global usernum
				usernamedic[myusername]=userlist[usernum]
				
				self.mycsv.openwriter()
				with self.mycsv.file:
					self.mycsv.dictwriter()
					self.mycsv.writer.writerow({'Username':myusername, 'Password':mypassword})
					self.mycsv.close()
					usernamedic[myusername].accountslist.append(Account(begbalance,atype, myaccountnum))
					myaccountindex=usernamedic[myusername].accountindexnum

					usernamedic[myusername].accountsdic[myaccountnum]=userlist[usernum].accountslist[myaccountindex]
					usernum+=1
					usernamedic[myusername].accountindexnum+=1
				
				print ("your new client account has been successfully created, please log in as an existing user now. your username is "+myusername)	
					

		


	def deposit(self, amount, username, myaccountnum):
	
		usernamedic[username].accountsdic[myaccountnum].balance+=amount
		print ("deposit completed- your new balance for this account is : "+str(usernamedic[username].accountsdic[myaccountnum].balance))
		return usernamedic[username].accountsdic[myaccountnum].balance
	

	def withdraw(self, amount, username, myaccountnum):
		
		if (amount>usernamedic[username].accountsdic[myaccountnum].balance):
			print ("withdraw cannot be completed- not enough balance")
		elif (amount<=usernamedic[username].accountsdic[myaccountnum].balance):
			usernamedic[username].accountsdic[myaccountnum].balance-=amount
			print ("withdraw completed- your new balance for this account is : "+str(usernamedic[username].accountsdic[myaccountnum].balance))
			return usernamedic[username].accountsdic[myaccountnum].balance
	def transfer(self, amount, fromusername, tousername, fromaccountnum, toaccountnum):
	
		
		if (amount>usernamedic[fromusername].accountsdic[fromaccountnum].balance):
			print ("transfer cannot be completed- not enough balance")
		elif (amount<=usernamedic[fromusername].accountsdic[fromaccountnum].balance):
			usernamedic[fromusername].accountsdic[fromaccountnum].balance-=amount
			usernamedic[tousername].accountsdic[toaccountnum].balance+=amount
			print ("transfer completed- your new balance for the account number "+str(fromaccountnum)+ " is : "+str(usernamedic[fromusername].accountsdic[fromaccountnum].balance))
			print ("your new balance for the account number "+str(toaccountnum)+ " is : "+str(usernamedic[tousername].accountsdic[toaccountnum].balance))
			return usernamedic[fromusername].accountsdic[fromaccountnum].balance
	def displayuseraccounts(self, username):
		for key in usernamedic[username].accountsdic:
			print ("for client username "+usernamedic[username].username+" account type " +usernamedic[username].accountsdic[key].type+" account with account number : "+str(usernamedic[username].accountsdic[key].accountnum))
			print ("the balance for this account is : " + str(usernamedic[username].accountsdic[key].balance))



