from trader_models import Stock
from trader_models import Tuser
from trader_views import Tviews
from bank_models import User
from bank_models import Client
from bank_models import Banker
from bank_models import userlist
from bank_models import usernamedic
from create_db import Database
from trader_models import tusernum
from trader_models import tuserlist
from trader_models import tusernamedic
from trader_models import tmodeldatabase
import wrapper

class Tcontroller:
	def __init__(self):
		self.mytview=Tviews()
		self.newuser=[]
		self.usernum=0
		self.logname=None
		self.logpassword=None
		self.mymarkit=wrapper.Markit()
		self.username=None

	def createTusers(self):
		
		global tusernum
		tdatabase.connect()
		tdatabase.cursor()
		content=tdatabase.curs.execute("SELECT * FROM Clients")
		myresult=content.fetchall()
		for row in myresult:
			tuserlist.append(Tuser(row[1],row[2]))
			tusernamedic[row[1]]=tuserlist[tusernum]
			tusernum+=1
		tdatabase.commit()
		tdatabase.close_connection()

	def createownclient(self,myusername,password):
		self.username=myusername
		global tusernum
		tdatabase.connect()
		tdatabase.cursor()
		count=0

		for key in tusernamedic:
			if (key==myusername):
				count+=1
		if (count==0):
			tuserlist.append(Tuser(myusername,password))
			tusernamedic[myusername]=tuserlist[tusernum]
			tusernum+=1
			tdatabase.curs.execute("INSERT INTO Clients(Username, Password)"" VALUES(?,?)", (myusername, password))
		tdatabase.commit()
		tdatabase.close_connection()
		

	def checkaccountnum(self):
		
		tmodeldatabase.connect()
		tmodeldatabase.cursor()
		mystring="SELECT * FROM Client_Accounts WHERE Client_Username='{}'".format(self.username)
		content=tmodeldatabase.curs.execute(mystring)
		myresult=content.fetchall()
		count=0
		for row in myresult:
			if (row[1]==self.mytview.buysellaccountnum):
				count+=1
		tmodeldatabase.commit()
		tmodeldatabase.close_connection()
		if (count==0):
			print("you don't have any account with this account number, please enter a valid account number : ")
			return self.mytview.getaccountnum()
		elif (count>0):
			print ("the system has found your account!")


	def stockvalid(self):
		if (self.mymarkit.company_search(self.mytview.stockname)==False):
			print ("please check your stockname input, stockname cannot be found")
			return self.mytview.enterstock()

	def createtuserstock(self):
		tdatabase.connect()
		tdatabase.cursor()
		mystring="SELECT * FROM Portfolio WHERE Username ='{}'".format(self.username)
		content=tdatabase.curs.execute(mystring)
		result=content.fetchall()
		for row in result:
			tusernamedic[self.username].stocklist.append(Stock(row[2],row[3]))
			tusernamedic[self.username].stockdic[row[2]]=tusernamedic[self.username].stocklist[tusernamedic[self.username].stocknum]
			tusernamedic[self.username].stocknum+=1
		tdatabase.commit()
		tdatabase.close_connection()


	def userchoice(self):
		self.mytview.getchoice()
		self.createtuserstock()

		if (self.mytview.choice=='b'):
			stockisnew=True
			for key in tusernamedic[self.username].stockdic:
				if (key==self.mytview.stockname):
					stockisnew=False
			if (stockisnew==True):
				self.stockvalid()
				self.mytview.getaccountnum()
				self.checkaccountnum()
				tusernamedic[self.username].buy(self.mytview.stockname, self.mytview.stockshares, self.mytview.buysellaccountnum)
			elif (stockisnew==False):
				self.mytview.getaccountnum()
				self.checkaccountnum()
				tusernamedic[self.username].buy(self.mytview.stockname, self.mytview.stockshares, self.mytview.buysellaccountnum)
		elif (self.mytview.choice=='s'):
			self.mytview.getaccountnum()
			self.checkaccountnum()
			tusernamedic[self.username].sell(self.mytview.stockname, self.mytview.stockshares, self.mytview.buysellaccountnum)
		elif (self.mytview.choice=='i'):
			companyinfo=self.mymarkit.company_search(self.mytview.companyname)
			print ("below are the company's most updated information: ")
			print (companyinfo)
			stocksymbol=companyinfo[0]['Symbol']
			quote=self.mymarkit.get_quote(stocksymbol)
			print ("below are the company's most updated stock quote information: ")
			print (quote)
		elif (self.mytview.choice=='v'):
			self.userdashboard()


	def userdashboard(self):
		if (self.mytview.viewchoice=='p'):
			for key in userdic[self.mytview.username].stockdic:
				print ("stockname : "+userdic[self.mytview.username].stockdic[key].stockname)
				print ("stock shares : "+str(userdic[self.mytview.username].stockdic[key].shares))

		elif (self.mytview.viewchoice=='ae'):
			print (userdic[self.mytview.username].amountearn)

		elif (self.mytview.viewchoice=='al'):
			print (userdic[self.mytview.username].amountloss)
		elif (self.mytview.viewchoice=='l'):
			print (userdic[self.mytview.username].liquidcash())



tdatabase=Database('ttrader')
'''
tdatabase.connect()
tdatabase.cursor()

tdatabase.curs.execute("CREATE TABLE 'Transactions' ('id' INTEGER,'Username' VARCHAR,'Transaction_Type' VARCHAR, 'Stockname' VARCHAR, 'Transaction_Shares' INTEGER, 'Transaction_Amount' REAL, 'Transaction_Stock_Price' REAL, 'Transaction_Time' TEXT, PRIMARY KEY ('id'))")
tdatabase.curs.execute("CREATE TABLE 'Portfolio'('id' INTEGER,'Username' VARCHAR,'Stockname' VARCHAR, 'Stock_Shares' INTEGER, PRIMARY KEY ('id'))")

tdatabase.commit()
tdatabase.close_connection()
'''

'''	else:

			tdatabase.connect()
			tdatabase.cursor()
			mystring="SELECT * FROM Portfolio WHERE Username='{}'".format(self.username)
			content=tdatabase.curs.execute(mystring)
			result=content.fetchall()
			count=1
			for row in result:
				if (row[2]==self.mytview.stockname):
					count+=1
			if (count==0):

				tusernamedic[self.username].stocklist.append(Stock(self.mytview.stockname))
				tusernamedic[self.username].stockdic[self.mytview.stockname]=tusernamedic[self.username].stocklist[tusernamedic[self.username].stocknum]
				tusernamedic[self.username].stocknum+=1
				tdatabase.curs.execute("INSERT INTO Portfolio(Username, Stockname, Stock_Shares)"" VALUES(?,?,?)", (self.username,self.mytview.stockname, self.mytview.stockshares ))
			tdatabase.commit()
			tdatabase.close_connection()'''


