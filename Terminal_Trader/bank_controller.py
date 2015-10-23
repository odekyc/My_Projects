from bank_views import Views
from bank_models import usernamedic
from bank_models import usernum
from bank_models import User
from bank_models import Banker
from bank_models import Client
from bank_models import Account
from create_db import Database
from create_db import CSV
from bank_models import userlist
from trader_models import Tuser
from trader_views import Tviews
from trader_models import wrapper
from trader_models import Stock
from trader_controller import Tcontroller

bankerlist=[]
bankernamedic={}
bankernum=0



class Controller:
	def __init__(self):
		self.mymenu=Views()
		self.myclientcsv=CSV('clientlist')
		self.mybankercsv=CSV('bankerlist')
		self.mytradercontrol=Tcontroller()

	def checkownnameandpass(self):
		self.mymenu.firstmenu()
		if (self.mymenu.neworexuser=='n'):
			return self.createnewuser()
		elif (self.mymenu.neworexuser=='e'):

			countfound=0
			countwrongpass=0
			if (self.mymenu.userrole=='b'):
				self.mybankercsv.openreader()
				with self.mybankercsv.file:
					self.mybankercsv.dictreader()
					for row in self.mybankercsv.reader:
						print (row)
						if (self.mymenu.ownname==row['Username'] and self.mymenu.ownpassword==row['Password']):
							countfound+=1
						elif (self.mymenu.ownname==row['Username'] and self.mymenu.ownpassword!=row['Password']):
							countwrongpass+=1
					if (countfound==0 and countwrongpass==0 ):
						print ("you are not an existing user in our bank, please create a new banker account first!")
						return self.createnewuser()

					elif (countfound==0 and countwrongpass >0 ):
						print ("you entered the wrong banker account password, please reenter your banker account username and password!")
						return self.checkownnameandpass()
					elif (countfound>0 and countwrongpass==0):
						print ("you are now logged into your banker account!")
						return self.actions()
			elif (self.mymenu.userrole=='c'):
				self.myclientcsv.openreader()
				with self.myclientcsv.file:
					self.myclientcsv.dictreader()
					for row in self.myclientcsv.reader:
						if (self.mymenu.ownname==row['Username'] and self.mymenu.ownpassword==row['Password']):
							countfound+=1
						elif (self.mymenu.ownname==row['Username'] and self.mymenu.ownpassword!=row['Password']):
							countwrongpass+=1
					if (countfound==0 and countwrongpass==0 ):
						print ("you are not an existing user in our bank, please have a banker create an account for youn first!")
						return self.checkownnameandpass()

					elif (countfound==0 and countwrongpass >0 ):
						print ("you entered the wrong client account password, please reenter your client account username and password!")
						return self.checkownnameandpass()
					elif (countfound>0 and countwrongpass==0):
						print ("you are now logged into your client account!")
						return self.actions()

		


	def checkclientname(self):
		if (self.mymenu.action=='1c' or self.mymenu.action=='2c'  or self.mymenu.action=='4c' or self.mymenu.action=='1b' or self.mymenu.action=='5c'):
			return True
		elif (self.mymenu.action=='3c'):
			return self.checkothername()
		else:
			countfound=0
			self.myclientcsv.openreader()
			with self.myclientcsv.file:
				self.myclientcsv.dictreader()
				for row in self.myclientcsv.reader:
					if (self.mymenu.clientname==row['Username'] ):
						countfound+=1
			
				if (countfound==0):
					print ("the client username is not an existing client in our bank!")
					return False

				elif (countfound>0):
					print ("your client is found in our database!")
					if (self.mymenu.action=='4b'):
						return self.checkothername()
					elif (self.mymenu.action!='4b' and self.mymenu.action!='3c' and self.mymenu.action!='1c' and self.mymenu.action!='2c' and self.mymenu.action!='1b' and self.mymenu.action!='5c'):
						return True


		
	def checkothername(self):
		countfound=0
		self.myclientcsv.openreader()
		with self.myclientcsv.file:
			self.myclientcsv.dictreader()
			for row in self.myclientcsv.reader:
				if (self.mymenu.otherclientname==row['Username'] ):
					countfound+=1
			
			if (countfound==0):
				print ("the client username is not an existing client in our bank!")
				return False

			elif (countfound>0):
				print ("your client is found in our database!")
				return True

		
	def createnewuser(self):

		if (self.mymenu.newuserchoice=='b'):
			countfound=0
			self.mybankercsv.openreader()
			with self.mybankercsv.file:
				self.mybankercsv.dictreader()
				for row in self.mybankercsv.reader:
					
					if (self.mymenu.newusername==row['Username'] ):
						countfound+=1
				if (countfound>0):
					print ("this banker name already exists in our system, try to log in as an existing user!")
					return self.checkownnameandpass()
				elif (countfound==0):
					bankerlist.append(Banker(self.mymenu.newusername, self.mymenu.newuserpassword))
					global bankernum
					bankernamedic[self.mymenu.newusername]=bankerlist[bankernum]
					bankernum+=1
					self.mybankercsv.openwriter()
					with self.mybankercsv.file:
						self.mybankercsv.dictwriter()
						self.mybankercsv.writer.writerow({'Username':self.mymenu.newusername, 'Password':self.mymenu.newuserpassword})
						self.mybankercsv.close()
					mydatabase.connect()
					mydatabase.cursor()
					mydatabase.curs.execute("INSERT INTO Bankers(Username, Password, Time_Account_Created)"" VALUES(?,?,?)", (bankernamedic[self.mymenu.newusername].username, bankernamedic[self.mymenu.newusername].password, bankernamedic[self.mymenu.newusername].time_created))
					mydatabase.commit()
					mydatabase.close_connection()

					print ("your new banker account has been successfully created, please log in as an existing user now. your username is "+self.mymenu.newusername)	
					return self.checkownnameandpass()


	def actions(self):
		self.mymenu.whattodo()
		mycheckclient=self.checkclientname()
		while(mycheckclient==False):
			self.mymenu.getinfo()

		if (self.mymenu.action=='1b'):
			
			bankernamedic[self.mymenu.ownname].createaccount(self.mymenu.accounttype, self.mymenu.clientbalance, self.mymenu.clientname, self.mymenu.clientpassword, self.mymenu.newcreateaccountnum)
			mydatabase.connect()
			mydatabase.cursor()
			mydatabase.curs.execute("INSERT INTO Clients(Username, Password, Time_Account_Created)"" VALUES(?,?,?)", (self.mymenu.clientname, self.mymenu.clientpassword, usernamedic[self.mymenu.clientname].time_created))
			mydatabase.curs.execute("INSERT INTO Client_Accounts(Accountnumber, Balance, Account_Type, Client_Username)"" VALUES(?,?,?,?)", (self.mymenu.newcreateaccountnum, self.mymenu.clientbalance, self.mymenu.accounttype, self.mymenu.clientname))
			mydatabase.commit()
			mydatabase.close_connection()
			

			mylogout=self.mymenu.logout()
			if (mylogout==False):
				return self.actions()
			elif (mylogout==True):
				return self.checkownnameandpass()
		elif (self.mymenu.action=='2b'):
			
			clientnewbal=bankernamedic[self.mymenu.ownname].deposit(float(self.mymenu.clientamount),self.mymenu.clientname ,int(self.mymenu.clientaccountnum) )
			
			mydatabase.connect()
			mydatabase.cursor()
			mydatabase.curs.execute("UPDATE Client_Accounts SET Balance= ? WHERE Accountnumber=?",(clientnewbal, int(self.mymenu.clientaccountnum)))
			mydatabase.commit()
			mydatabase.close_connection()
			mylogout=self.mymenu.logout()
			if (mylogout==False):
				return self.actions()
			elif (mylogout==True):
				return self.checkownnameandpass()

		elif (self.mymenu.action=='3b'):
		
			clientnewbal=bankernamedic[self.mymenu.ownname].withdraw(float(self.mymenu.clientamount),self.mymenu.clientname ,int(self.mymenu.clientaccountnum))
			mydatabase.connect()
			mydatabase.cursor()
			mydatabase.curs.execute("UPDATE Client_Accounts SET Balance= ? WHERE Accountnumber=?",(clientnewbal, int(self.mymenu.clientaccountnum)))
			mydatabase.commit()
			mydatabase.close_connection()

			mylogout=self.mymenu.logout()
			if (mylogout==False):
				return self.actions()
			elif (mylogout==True):
				return self.checkownnameandpass()
		elif (self.mymenu.action=='4b'):
			iuser=bankernamedic[self.mymenu.ownname]
			clientnewbal=iuser.transfer(float(self.mymenu.clientamount), self.mymenu.clientname, self.mymenu.otherclientname, int(self.mymenu.clientaccountnum), int(self.mymenu.clientaccountnum2))
			otherusernewbal=usernamedic[self.mymenu.otherclientname].accountsdic[int(self.mymenu.clientaccountnum2)].balance
			mydatabase.connect()
			mydatabase.cursor()
			mydatabase.curs.execute("UPDATE Client_Accounts SET Balance= ? WHERE Accountnumber=?",(clientnewbal, int(self.mymenu.clientaccountnum)))
			mydatabase.curs.execute("UPDATE Client_Accounts SET Balance= ? WHERE Accountnumber=?",(otherusernewbal, int(self.mymenu.clientaccountnum2)))
			mydatabase.commit()
			mydatabase.close_connection()

			mylogout=self.mymenu.logout()
			if (mylogout==False):
				return self.actions()
			elif (mylogout==True):
				return self.checkownnameandpass()
		elif (self.mymenu.action=='5b'):
			iuser=bankernamedic[self.mymenu.ownname]
			iuser.displayuseraccounts(self.mymenu.clientname)
			mylogout=self.mymenu.logout()
			if (mylogout==False):
				return self.actions()
			elif (mylogout==True):
				return self.checkownnameandpass()

		elif (self.mymenu.action=='6b'):
			self.mytradercontrol.createTusers()
			self.mytradercontrol.createownclient(self.mymenu.clientname, self.mymenu.clientpassword)
			self.mytradercontrol.userchoice()
		elif (self.mymenu.action=='1c'):
			iuser=usernamedic[self.mymenu.ownname]
			mynewbal=iuser.deposit(float(self.mymenu.amount), int(self.mymenu.accountnum))
			mydatabase.connect()
			mydatabase.cursor()
			mydatabase.curs.execute("UPDATE Client_Accounts SET Balance= ? WHERE Accountnumber=?",(mynewbal, int(self.mymenu.accountnum)))
			mydatabase.commit()
			mydatabase.close_connection()

			mylogout=self.mymenu.logout()
			if (mylogout==False):
				return self.actions()
			elif (mylogout==True):
				return self.checkownnameandpass()
		elif(self.mymenu.action=='2c'):
		 	iuser=usernamedic[self.mymenu.ownname]
		 	mynewbal=iuser.withdraw(float(self.mymenu.amount), int(self.mymenu.accountnum))
		 	mydatabase.connect()
		 	mydatabase.cursor()
		 	mydatabase.curs.execute("UPDATE Client_Accounts SET Balance=? WHERE Accountnumber=?",(mynewbal, int(self.mymenu.accountnum)))
		 	mydatabase.commit()
		 	mydatabase.close_connection()
		 	mylogout=self.mymenu.logout()
		 	if (mylogout==False):
		 		return self.actions()
		 	elif (mylogout==True):
		 		return self.checkownnameandpass()
			
		elif(self.mymenu.action=='3c'):
			iuser=usernamedic[self.mymenu.ownname]
			mynewbal=iuser.transfer( float(self.mymenu.amount),self.mymenu.otherclientname , int(self.mymenu.accountnum),int(self.mymenu.accountnum2))
			otherusernewbal=usernamedic[self.mymenu.otherclientname].accountsdic[int(self.mymenu.accountnum2)].balance
			mydatabase.connect()
			mydatabase.cursor()
			mydatabase.curs.execute("UPDATE Client_Accounts SET Balance= ? WHERE Accountnumber=?",(mynewbal, int(self.mymenu.accountnum)))
			mydatabase.curs.execute("UPDATE Client_Accounts SET Balance= ? WHERE Accountnumber=?",(otherusernewbal, int(self.mymenu.accountnum2)))
			mydatabase.commit()
			mydatabase.close_connection()

			mylogout=self.mymenu.logout()
			if (mylogout==False):
				return self.actions()
			elif (mylogout==True):
				return self.checkownnameandpass()

		elif (self.mymenu.action=='4c'):
			iuser=usernamedic[self.mymenu.ownname]
			iuser.displayaccounts()
			mylogout=self.mymenu.logout()
			if (mylogout==False):
				return self.actions()
			elif (mylogout==True):
				return self.checkownnameandpass()
		elif (self.mymenu.action=='5c'):
			self.mytradercontrol.createownclient(self.mymenu.ownname,self.mymenu.ownpassword)
			self.mytradercontrol.userchoice()

mydatabase=Database('banksoft')
mydatabase.connect()
mydatabase.cursor()
resultclient=mydatabase.curs.execute("SELECT * FROM Clients")
rows = resultclient.fetchall()
for eachrow in rows:
	userlist.append(Client(eachrow[1], eachrow[2]))
	global usernum
	usernamedic[eachrow[1]]=userlist[usernum]
	
	usernum+=1

resultbanker=mydatabase.curs.execute("SELECT * FROM Bankers")
bankerrows=resultbanker.fetchall()
for eachrow in bankerrows:
	bankerlist.append(Banker(eachrow[1], eachrow[2]))

	bankernamedic[eachrow[1]]=bankerlist[bankernum]
	bankernum+=1

resultaccounts=mydatabase.curs.execute("SELECT * FROM Client_Accounts")
accountsrows=resultaccounts.fetchall()
for eachrow in accountsrows:
	usernamedic[eachrow[4]].accountslist.append(Account(eachrow[2], eachrow[3], eachrow[1]))
	myaccountindex=usernamedic[eachrow[4]].accountindexnum
	usernamedic[eachrow[4]].accountsdic[eachrow[1]]=usernamedic[eachrow[4]].accountslist[myaccountindex]
	usernamedic[eachrow[4]].accountindexnum+=1



mydatabase.commit()
mydatabase.close_connection()
print (usernum)
print (bankernum)
for key in usernamedic:
	print (usernamedic[key].accountindexnum)


mycontroller=Controller()

mycontroller.checkownnameandpass()
'''
mydatabase.connect()
mydatabase.cursor()
mydatabase.curs.execute("DROP TABLE Clients")
mydatabase.curs.execute("DROP TABLE Bankers")
mydatabase.curs.execute("DROP TABLE Client_Accounts")
mydatabase.curs.execute("CREATE TABLE 'Clients' ('id' INTEGER,'Username' VARCHAR,'Password' VARCHAR, 'Time_Account_Created' TEXT, PRIMARY KEY ('id'))")
mydatabase.curs.execute("CREATE TABLE 'Bankers' ('id' INTEGER,'Username' VARCHAR,'Password' VARCHAR, 'Time_Account_Created' TEXT, PRIMARY KEY ('id'))")
mydatabase.curs.execute("CREATE TABLE 'Client_Accounts' ('id' INTEGER,'Accountnumber' INTEGER,'Balance' REAL, 'Account_Type' VARCHAR, 'Client_Username' VARCHAR, PRIMARY KEY ('id'))")
mydatabase.curs.execute("INSERT INTO Clients(Username, Password, Time_Account_Created)"" VALUES(?,?,?)", (clientelva.username, clientelva.password, clientelva.time_created))
mydatabase.curs.execute("INSERT INTO Clients(Username, Password, Time_Account_Created)"" VALUES(?,?,?)", (clientdavid.username, clientdavid.password, clientdavid.time_created))
mydatabase.curs.execute("INSERT INTO Bankers(Username, Password, Time_Account_Created)"" VALUES(?,?,?)", (bankersuper.username, bankersuper.password, bankersuper.time_created))
mydatabase.curs.execute("INSERT INTO Client_Accounts(Accountnumber, Balance, Account_Type, Client_Username)"" VALUES(?,?,?,?)", (elvaaccount1.accountnum, elvaaccount1.balance, elvaaccount1.type, clientelva.username))
mydatabase.curs.execute("INSERT INTO Client_Accounts(Accountnumber, Balance, Account_Type, Client_Username)"" VALUES(?,?,?,?)", (elvaaccount2.accountnum, elvaaccount2.balance, elvaaccount2.type, clientelva.username))
mydatabase.curs.execute("INSERT INTO Client_Accounts(Accountnumber, Balance, Account_Type, Client_Username)"" VALUES(?,?,?,?)", (davidaccount1.accountnum, davidaccount1.balance, davidaccount1.type, clientdavid.username))
mydatabase.curs.execute("INSERT INTO Client_Accounts(Accountnumber, Balance, Account_Type, Client_Username)"" VALUES(?,?,?,?)", (davidaccount2.accountnum, davidaccount2.balance, davidaccount2.type, clientdavid.username))
mydatabase.curs.execute("INSERT INTO Client_Accounts(Accountnumber, Balance, Account_Type, Client_Username)"" VALUES(?,?,?,?)", (davidaccount3.accountnum, davidaccount3.balance, davidaccount3.type, clientdavid.username))
mydatabase.commit()
mydatabase.close_connection()
result=mydatabase.curs.execute("SELECT Username FROM Clients")
row = result.fetchone();
'''
		
'''clientelva=Client('elvacccc','helloworld')
userlist.append(clientelva)
usernamedic['elvacccc']=userlist[0]
elvaaccount1=Account(4000.86, 'checking',58869751 )
elvaaccount2=Account(2000.35, 'saving', 56886833 )
usernamedic['elvacccc'].accountslist.append(elvaaccount1)
myaccountnum=58869751
usernamedic['elvacccc'].accountsdic[myaccountnum]=usernamedic['elvacccc'].accountslist[usernamedic['elvacccc'].accountindexnum]
usernamedic['elvacccc'].accountindexnum+=1
usernamedic['elvacccc'].accountslist.append(elvaaccount2)
myaccountnum=56886833
usernamedic['elvacccc'].accountsdic[myaccountnum]=usernamedic['elvacccc'].accountslist[usernamedic['elvacccc'].accountindexnum]
usernamedic['elvacccc'].accountindexnum+=1
clientdavid=Client('davidbbbb','davidpassword')
davidaccount1=Account(5336.01,'checking',59667398 )
davidaccount2=Account(400.68,'saving',54331238 )
davidaccount3=Account(9000.97,'retirement',81609873 )
userlist.append(clientdavid)
usernamedic['davidbbbb']=userlist[1]
usernamedic['davidbbbb'].accountslist.append(davidaccount1)
myaccountnum=59667398
usernamedic['davidbbbb'].accountsdic[myaccountnum]=usernamedic['davidbbbb'].accountslist[usernamedic['davidbbbb'].accountindexnum]
usernamedic['davidbbbb'].accountindexnum+=1
usernamedic['davidbbbb'].accountslist.append(davidaccount2)
myaccountnum=54331238
usernamedic['davidbbbb'].accountsdic[myaccountnum]=usernamedic['davidbbbb'].accountslist[usernamedic['davidbbbb'].accountindexnum]
usernamedic['davidbbbb'].accountindexnum+=1
usernamedic['davidbbbb'].accountslist.append(davidaccount3)
myaccountnum=81609873
usernamedic['davidbbbb'].accountsdic[myaccountnum]=usernamedic['davidbbbb'].accountslist[usernamedic['davidbbbb'].accountindexnum]
usernamedic['davidbbbb'].accountindexnum+=1

bankersuper=Banker('superbanker','iamsuperb')
bankerlist.append(bankersuper)
bankernamedic['superbanker']=bankerlist[0]
'''
'''mydatabase.connect()
				mydatabase.cursor()
				mydatabase.curs.execute("INSERT INTO Clients(Username, Password, Time_Account_Created)"" VALUES(?,?,?)", (usernamedic[myusername].username, usernamedic[myusername].password, usernamedic[myusername].time_created))
				mydatabase.curs.execute("INSERT INTO Client_Accounts(Accountnumber, Balance, Account_Type, Client_Username)"" VALUES(?,?,?,?)", (usernamedic[myusername].accountsdic[myaccountnum].accountnum, usernamedic[myusername].accountsdic[myaccountnum].balance, usernamedic[myusername].accountsdic[myaccountnum].type, usernamedic[myusername].username))
				mydatabase.commit()
				mydatabase.close_connection()'''
'''
resultclient=mydatabase.curs.execute("SELECT * FROM Clients")
rows = resultclient.fetchall()
for eachrow in rows:
	userlist.append(Client(eachrow[1], eachrow[2]))
	global usernum
	usernamedic[eachrow[1]]=userlist[usernum]
	
	usernum+=1

resultbanker=mydatabase.curs.execute("SELECT * FROM Bankers")
bankerrows=resultbanker.fetchall()
for eachrow in bankerrows:
	bankerlist.append(Banker(eachrow[1], eachrow[2]))

	bankernamedic[eachrow[1]]=bankerlist[bankernum]
	bankernum+=1

resultaccounts=mydatabase.curs.execute("SELECT * FROM Client_Accounts")
accountsrows=resultaccounts.fetchall()
for eachrow in accountsrows:
	usernamedic[eachrow[4]].accountslist.append(Account(eachrow[2], eachrow[3], eachrow[1]))
	myaccountindex=usernamedic[eachrow[4]].accountindexnum
	usernamedic[eachrow[4]].accountsdic[eachrow[1]]=usernamedic[eachrow[4]].accountslist[myaccountindex]
	usernamedic[eachrow[4]].accountindexnum+=1
	'''