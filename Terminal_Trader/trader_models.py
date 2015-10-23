import sqlite3
from create_db import Database
import sys
sys.path.insert(0, '/home/elva/byteacademy/ba-week3-day3/exercises/1-your-first-api')
import wrapper

tuserlist=[]
tusernamedic={}
tusernum=0

tmodeldatabase=Database('banksoft')

class Stock:
	def __init__(self, stockname, stockshares):
		self.stockname=stockname
		self.shares=stockshares
		
		self.markit=wrapper.Markit()
		self.stockprice=self.currentprice()
		self.lastbuyprice=None
		self.lastsellprice=None
		
		
	def currentprice(self):
		mycompanyinfo=self.markit.company_search(self.stockname)
		stocksymbol=mycompanyinfo[0]['Symbol']
		cprice=self.markit.get_quote(stocksymbol)['LastPrice']

		return cprice






class Tuser:
	def __init__(self,username,password):
		self.balance=None
		self.username=username
		self.password=password
		self.stockdic={}
		self.stocklist=[]
		self.amountearn=0
		self.amountloss=0
		self.stocknum=0

	

	def buy(self, stockname,sharenum, accountnum):
		tmodeldatabase.connect()
		tmodeldatabase.cursor()
		sharenum=int(sharenum)

		mystring="SELECT * FROM Client_Accounts WHERE Client_Username='{}'".format(self.username)
		content=tmodeldatabase.curs.execute(mystring)
		myresult=content.fetchall()
		

		if (self.balance<sharenum* self.stockdic[stockname].stockprice):
			print ("cannot process transaction-not enough money in account")
		else:
			self.balance-=sharenum*self.stockdic[stockname].stockprice
			self.stockdic[stockname].shares+=sharenum
			self.stockdic[stockname].lastbuyprice=self.stockdic[stockname].stockprice
			print ("buy transaction successfully processed, updated shares : "+str(self.stockdic[stockname].shares))

	def sell(self, stockname, sharenum, accountnum):
		sharenum=int(sharenum)
		stockindic=False

		for key in self.stockdic:
			if (self.stockdic[stockname]):
				stockindic=True

		if (stockindic==False ):
			print ("cannot process transaction-stock not in your portfolio")
		elif (stockindic):
			if (self.stockdic[stockname].shares<sharenum):
				print ("cannot process transaction-not enough shares in portfolio")

			elif (self.stockdic[stockname].shares>=sharenum):
				self.balance+=sharenum*self.stockdic[stockname].stockprice
				self.stockdic[stockname].shares-=sharenum
				self.stockdic[stockname].lastsellprice=self.stockdic[stockname].stockprice
				if (self.stockdic[stockname].lastsellprice>self.stockdic[stockname].lastbuyprice):
					amountearn+=(self.stockdic[stockname].lastsellprice-self.stockdic[stockname].lastbuyprice)*sharenum
				elif (self.stockdic[stockname].lastsellprice<self.stockdic[stockname].lastbuyprice):
					amountloss+=(self.stockdic[stockname].lastbuyprice-self.stockdic[stockname].lastsellprice)*sharenum
				print ("sell transaction successfully processed, updated shares : "+str(self.stockdic[stockname].shares))
	def liquidcash(self):

		return self.balance


'''class Superuser(User):
	def leaderboard(self):
		earninglist=[]
		for key in userdic:'''










