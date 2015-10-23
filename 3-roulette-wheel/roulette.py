from random import randint

print ("this is a roulette game, we are going to explain the rules a little bit :")
print ("the rule of the roulette game is, choose at random to bet on which space of the American roulette wheel the ball is going to land on! if, after the wheel spins, the ball indeed lands on one of the spaces of your bet places on, you win the game and is rewarded with a sum of money!")
print ("depending on the number of spaces you place bet on, your payout, if the ball really lands on one of the spaces you bet on, is payout=(36/n)-1")
print ("the spaces on an American roulette wheel includes : 0, 00, and the numbers 1-36")
print ("below we will introduce you to your choices of bet in American roulette and what to enter for the selection of your bet choice on this platform :")
print ("0 [enter 0]")
print ("00 [enter 00]")
print ("Straight: any single number from 1-36 [enter strai]")
print ("Row:0,00 [enter row]")
print ("Split: any two horizontally adjacent numbers, e.g. 1,2 or 30,31 [enter split]")
print ("Basket: 0 1 2 [enter bask]")
print ("Street: any three horizontally adjacent numbers, e.g. 1,2,3 or 20,21,22 [enter str]")
print ("Corner: any four horizontally adjacent numbers, e.g. 3,4,5,6 [enter corn]")
print ("Top Line: 0 00 1 2 3 [enter tl]")
print ("Six Line: any six horizontally adjacent numbers,e.g. 3,4,5,6,7,8 [enter sl]")
print ("1st Dozen: 1 through 12 [enter doz1]")
print ("2nd Dozen: 13 through 24 [enter doz2]")
print ("3rd Dozen: 25 through 36 [enter doz3]")
print ("Odd: all odd numbers 1,3,5,7,9,11,13......[enter odd]")
print ("Even: all even numbers 2,4,6,8,10,12,14.....[enter ev]")
print ("Red: all red spaces on the wheel 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 [enter red]")
print ("Black: all black spaces on the wheel 2, 4, 6, 8, 10, 11,13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35 [enter black]")
print ("1-18 [enter 1-18]")
print ("19-36 [enter 19-36]")
class Roulette:
	def __init__(self):
		self.betchoice=None
		self.mybetlist=[]
		self.mybetnum=None
		self.winnum=None


	def Bet_Choice(self):
		self.mybetlist=[]
		self.betchoice=input("Please enter, based on the above info, what is your bet selection: ")
		if (self.betchoice!='0' and self.betchoice!='00' and self.betchoice!='strai' and self.betchoice!='row' and self.betchoice!='split' and self.betchoice!='bask' and self.betchoice!='str' and self.betchoice!='corn' and self.betchoice!='tl' and self.betchoice!='sl' and self.betchoice!='doz1' and self.betchoice!='doz2' and self.betchoice!='doz3' and self.betchoice!='odd' and self.betchoice!='ev' and self.betchoice!='red' and self.betchoice!='black' and self.betchoice!='1-18' and self.betchoice!='19-36'):
			print ("wrong input, please enter your bet selection again")
			return self.Bet_Choice()
		elif (self.betchoice=='0'):
			self.mybetnum=int(self.betchoice)
		elif (self.betchoice=='00'):
			self.mybetnum=37
		elif (self.betchoice=='strai'):
			self.mybetnum=int(input("Please enter an integer between 1-36:"))
			if (self.mybetnum not in range(1,37)):
				print ("wrong input, please enter your bet selection again")
				return self.Bet_Choice()
		elif (self.betchoice=='row'):
			self.mybetlist.append(0)
			self.mybetlist.append(37)
		elif (self.betchoice=='split'):
			print ("please enter two adjacent numbers:")
			firstnum=int(input("please enter first number:"))
			secnum=int(input("please enter second number:"))
			self.mybetlist.append(firstnum)
			self.mybetlist.append(secnum)
			validity=self.Betlist_Validity()
			if (validity==False):
				print ("wrong input, please enter your bet selection again")
				return self.Bet_Choice()

		elif (self.betchoice=='bask'):
			self.mybetlist.append(0)
			self.mybetlist.append(1)
			self.mybetlist.append(2)
		elif (self.betchoice=='str'):
			print ("please enter three adjacent numbers:")
			firstnum=int(input("please enter first number:"))
			secnum=int(input("please enter second number:"))
			thirdnum=int(input("please enter third number:"))
			self.mybetlist.append(firstnum)
			self.mybetlist.append(secnum)
			self.mybetlist.append(thirdnum)
			validity=self.Betlist_Validity()
			if (validity==False):
				print ("wrong input, please enter your bet selection again")
				return self.Bet_Choice()
		

		elif (self.betchoice=='corn'):
			print ("please enter four adjacent numbers:")
			firstnum=int(input("please enter first number:"))
			secnum=int(input("please enter second number:"))
			thirdnum=int(input("please enter third number:"))
			fournum=int(input("please enter fourth number:"))
			self.mybetlist.append(firstnum)
			self.mybetlist.append(secnum)
			self.mybetlist.append(thirdnum)
			self.mybetlist.append(fournum)
			validity=self.Betlist_Validity()
			if (validity==False):
				print ("wrong input, please enter your bet selection again")
				return self.Bet_Choice()
		
		elif (self.betchoice=='tl'):
			self.mybetlist.append(0)
			self.mybetlist.append(37)
			self.mybetlist.append(1)
			self.mybetlist.append(2)
			self.mybetlist.append(3)
		elif (self.betchoice=='sl'):
			print ("please enter six adjacent numbers:")
			firstnum=int(input("please enter first number:"))
			secnum=int(input("please enter second number:"))
			thirdnum=int(input("please enter third number:"))
			fournum=int(input("please enter fourth number:"))
			fifnum=int(input("please enter fifth number:"))
			sixnum=int(input("please enter sixth number:"))
			self.mybetlist.append(firstnum)
			self.mybetlist.append(secnum)
			self.mybetlist.append(thirdnum)
			self.mybetlist.append(fournum)
			self.mybetlist.append(fifnum)
			self.mybetlist.append(sixnum)
			validity=self.Betlist_Validity()
			if (validity==False):
				print ("wrong input, please enter your bet selection again")
				return self.Bet_Choice()
		
			
		elif (self.betchoice=='doz1'):
			self.mybetlist.append(1)
			self.mybetlist.append(2)
			self.mybetlist.append(3)
			self.mybetlist.append(4)
			self.mybetlist.append(5)
			self.mybetlist.append(6)
			self.mybetlist.append(7)
			self.mybetlist.append(8)
			self.mybetlist.append(9)
			self.mybetlist.append(10)
			self.mybetlist.append(11)
			self.mybetlist.append(12)
		elif (self.betchoice=='doz2'):
			self.mybetlist.append(13)
			self.mybetlist.append(14)
			self.mybetlist.append(15)
			self.mybetlist.append(16)
			self.mybetlist.append(17)
			self.mybetlist.append(18)
			self.mybetlist.append(19)
			self.mybetlist.append(20)
			self.mybetlist.append(21)
			self.mybetlist.append(22)
			self.mybetlist.append(23)
			self.mybetlist.append(24)
		elif (self.betchoice=='doz3'):
			self.mybetlist.append(25)
			self.mybetlist.append(26)
			self.mybetlist.append(27)
			self.mybetlist.append(28)
			self.mybetlist.append(29)
			self.mybetlist.append(30)
			self.mybetlist.append(31)
			self.mybetlist.append(32)
			self.mybetlist.append(33)
			self.mybetlist.append(34)
			self.mybetlist.append(35)
			self.mybetlist.append(36)
		elif (self.betchoice=='odd'):
			self.mybetlist.append(1)
			self.mybetlist.append(3)
			self.mybetlist.append(5)
			self.mybetlist.append(7)
			self.mybetlist.append(9)
			self.mybetlist.append(11)
			self.mybetlist.append(13)
			self.mybetlist.append(15)
			self.mybetlist.append(17)
			self.mybetlist.append(19)
			self.mybetlist.append(21)
			self.mybetlist.append(23)
			self.mybetlist.append(25)
			self.mybetlist.append(27)
			self.mybetlist.append(29)
			self.mybetlist.append(31)
			self.mybetlist.append(33)
			self.mybetlist.append(35)
			
		elif (self.betchoice=='ev'):
			self.mybetlist.append(2)
			self.mybetlist.append(4)
			self.mybetlist.append(6)
			self.mybetlist.append(8)
			self.mybetlist.append(10)
			self.mybetlist.append(12)
			self.mybetlist.append(14)
			self.mybetlist.append(16)
			self.mybetlist.append(18)
			self.mybetlist.append(20)
			self.mybetlist.append(22)
			self.mybetlist.append(24)
			self.mybetlist.append(26)
			self.mybetlist.append(28)
			self.mybetlist.append(30)
			self.mybetlist.append(32)
			self.mybetlist.append(34)
			self.mybetlist.append(36)
		elif (self.betchoice=='red'):
			self.mybetlist.append(1)
			self.mybetlist.append(3)
			self.mybetlist.append(5)
			self.mybetlist.append(7)
			self.mybetlist.append(9)
			self.mybetlist.append(12)
			self.mybetlist.append(14)
			self.mybetlist.append(16)
			self.mybetlist.append(18)
			self.mybetlist.append(19)
			self.mybetlist.append(21)
			self.mybetlist.append(23)
			self.mybetlist.append(25)
			self.mybetlist.append(27)
			self.mybetlist.append(30)
			self.mybetlist.append(32)
			self.mybetlist.append(34)
			self.mybetlist.append(36)
		elif (self.betchoice=='black'):
			self.mybetlist.append(2)
			self.mybetlist.append(4)
			self.mybetlist.append(6)
			self.mybetlist.append(8)
			self.mybetlist.append(10)
			self.mybetlist.append(11)
			self.mybetlist.append(13)
			self.mybetlist.append(15)
			self.mybetlist.append(17)
			self.mybetlist.append(20)
			self.mybetlist.append(22)
			self.mybetlist.append(24)
			self.mybetlist.append(26)
			self.mybetlist.append(28)
			self.mybetlist.append(29)
			self.mybetlist.append(31)
			self.mybetlist.append(33)
			self.mybetlist.append(35)
		elif (self.betchoice=='1-18'):
			self.mybetlist.append(1)
			self.mybetlist.append(2)
			self.mybetlist.append(3)
			self.mybetlist.append(4)
			self.mybetlist.append(5)
			self.mybetlist.append(6)
			self.mybetlist.append(7)
			self.mybetlist.append(8)
			self.mybetlist.append(9)
			self.mybetlist.append(10)
			self.mybetlist.append(11)
			self.mybetlist.append(12)
			self.mybetlist.append(13)
			self.mybetlist.append(14)
			self.mybetlist.append(15)
			self.mybetlist.append(16)
			self.mybetlist.append(17)
			self.mybetlist.append(18)
		elif (self.betchoice=='19-36'):
			self.mybetlist.append(19)
			self.mybetlist.append(20)
			self.mybetlist.append(21)
			self.mybetlist.append(22)
			self.mybetlist.append(23)
			self.mybetlist.append(24)
			self.mybetlist.append(25)
			self.mybetlist.append(26)
			self.mybetlist.append(27)
			self.mybetlist.append(28)
			self.mybetlist.append(29)
			self.mybetlist.append(30)
			self.mybetlist.append(31)
			self.mybetlist.append(32)
			self.mybetlist.append(33)
			self.mybetlist.append(34)
			self.mybetlist.append(35)
			self.mybetlist.append(36)

	def Betlist_Validity(self):
		self.mybetlist.sort()
		mylen=len(self.mybetlist)
		if (self.betchoice=='split'):
			

			if (mylen!=2):
				return False
			else:
				adjcount=0
				for index in range(1,mylen):
					if(self.mybetlist[index]==self.mybetlist[index-1]+1):
						adjcount+=1

				if (adjcount==mylen-1):
					return True
				elif (adjcount<mylen-1):
					return False



		elif (self.betchoice=='str'):
			if (mylen!=3):
				return False
			else:
				adjcount=0
				for index in range(1,mylen):
					if(self.mybetlist[index]==self.mybetlist[index-1]+1):
						adjcount+=1

				if (adjcount==mylen-1):
					return True
				elif (adjcount<mylen-1):
					return False


		elif (self.betchoice=='corn'):
			if (mylen!=4):
				return False
			else:
				adjcount=0
				for index in range(1,mylen):
					if(self.mybetlist[index]==self.mybetlist[index-1]+1):
						adjcount+=1

				if (adjcount==mylen-1):
					return True
				elif (adjcount<mylen-1):
					return False

		elif (self.betchoice=='sl'):
			if (mylen!=6):
				return False
			else:
				adjcount=0
				for index in range(1,mylen):
					if(self.mybetlist[index]==self.mybetlist[index-1]+1):
						adjcount+=1

				if (adjcount==mylen-1):
					return True
				elif (adjcount<mylen-1):
					return False



	def Odd_A_Winning(self):
		if (self.betchoice=='0'):
			return "Odds against winning for your bet: 37 to 1"
		elif (self.betchoice=='00'):
			return "Odds against winning for your bet: 37 to 1"
		elif (self.betchoice=='strai'):
			return "Odds against winning for your bet: 37 to 1"
		elif (self.betchoice=='row'):
			return "Odds against winning for your bet: 18 to 1"
		elif (self.betchoice=='split'):
			return "Odds against winning for your bet: 18 to 1"
		elif (self.betchoice=='bask'):
			return "Odds against winning for your bet: 11.667 to 1"
		elif (self.betchoice=='str'):
			return "Odds against winning for your bet: 11.667 to 1"
		elif (self.betchoice=='corn'):
			return "Odds against winning for your bet: 8.5 to 1"
		elif (self.betchoice=='tl'):
			return "Odds against winning for your bet: 6.6 to 1"
		elif (self.betchoice=='sl'):
			return "Odds against winning for your bet: 5.33 to 1"
		elif (self.betchoice=='doz1'):
			return "Odds against winning for your bet: 2 1/6 to 1"
		elif (self.betchoice=='doz2'):
			return "Odds against winning for your bet: 2 1/6 to 1"
		elif (self.betchoice=='doz3'):
			return "Odds against winning for your bet: 2 1/6 to 1"
		elif (self.betchoice=='odd'):
			return "Odds against winning for your bet: 1 1/9 to 1"
		elif (self.betchoice=='ev'):
			return "Odds against winning for your bet: 1 1/9 to 1"
		elif (self.betchoice=='red'):
			return "Odds against winning for your bet: 1 1/9 to 1"
		elif (self.betchoice=='black'):
			return "Odds against winning for your bet: 1 1/9 to 1"
		elif (self.betchoice=='1-18'):
			return "Odds against winning for your bet: 1 1/9 to 1"
		elif (self.betchoice=='19-36'):
			return "Odds against winning for your bet: 1 1/9 to 1"

	def Generate_Winnum(self):
		self.winnum=randint(0,37)
		return "after the wheel spin, the ball lands at number "+str(self.winnum)

	def Win_Result(self):
		if (self.betchoice=='0'):
			if (self.winnum==0):
				return "YOU WIN! your payout is 35 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='00'):
			if (self.winnum==37):
				return "YOU WIN! your payout is 35 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='strai'):
			if (self.winnum==self.mybetnum):
				return "YOU WIN! your payout is 35 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='row'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 17 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='split'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 17 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='bask'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 11 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='str'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 11 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='corn'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 8 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='tl'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 6 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='sl'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 5 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='doz1'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 2 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='doz2'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 2 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='doz3'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 2 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='odd'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 1 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='ev'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 1 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='red'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 1 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='black'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 1 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='1-18'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 1 to 1"
			else:
				return "SORRY BUT YOU LOSE!"
		elif (self.betchoice=='19-36'):
			if self.winnum in self.mybetlist:
				return "YOU WIN! your payout is 1 to 1"
			else:
				return "SORRY BUT YOU LOSE!"



myroulette=Roulette()

myroulette.Bet_Choice()
print (myroulette.Odd_A_Winning())
print (myroulette.Generate_Winnum())
print (myroulette.Win_Result())
