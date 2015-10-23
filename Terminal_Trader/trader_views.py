
class Tviews:
	def __init__(self):
		self.traderlogin=None
		self.choice=None
		self.stockname=None
		self.stockshares=0
		self.companyname=None
		self.viewchoice=None
		self.buysellaccountnum=None

		

		

	def getchoice(self):
		print ("please enter what you would like to do-")
		self.choice=input("enter 'b' for buying more shares, enter 's' for selling more shares, 'i' for getting updated stock information 'v' for viewing your portfolio status :")
		self.choice.lower()
		if (self.choice!='b' and self.choice!='s' and self.choice!='i' and self.choice!='v'):
			print ("you didn't enter the right response!")
			return self.getchoice()
		elif (self.choice=='b' or self.choice=='s'):
			return self.enterstock()
		elif (self.choice=='i'):
			return self.getcompanyinfo()
		elif (self.choice=='v'):
			return self.viewownstockinfo()
			
		

	def enterstock(self):
		self.stockname=input("please enter the name of the stock : ")
		self.stockshares=input ("please enter the number of shares of the stock : ")

	def getcompanyinfo(self):
		self.companyname=input("please enter the name of the company, and I should return the updated company's stock information : ")

	def viewownstockinfo(self):
		self.viewchoice=input("please enter 'p' if you want to view your porfolio( list of stocks in it and the shares of each stock), enter 'ae' for amount of money you have earned so far in your account, enter 'al' for amount of money you have lost, enter 'l' for the amount of liquid cash you still have : ")
		self.viewchoice.lower()
		if (self.viewchoice!='p' and self.viewchoice!='ae' and self.viewchoice!='al' and self.viewchoice!='l'):
			print ("you didn't enter the right response!")
			return self.viewownstockinfo()
		else:
			return self.viewchoice

	def getaccountnum(self):
		self.buysellaccountnum=input("Please enter which account number you would like to use for trading stocks:")
