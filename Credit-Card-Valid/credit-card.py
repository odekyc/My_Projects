class CreditCard:
	def __init__(self, card_number):
  		self.card_number = card_number
  		self.valid = self.validate()
  		self.card_type = self.determine_card_type()
  		


#Create and add your method called `determine_card_type` to the CreditCard class here:
	def determine_card_type(self):
		if (self.valid==True):

			if (self.card_number[0]=='4'):
				return "VISA"
			elif (self.card_number[0]=='5'):
				if (self.card_number[1]=='1' or self.card_number[1]=='2' or self.card_number[1]=='3' or self.card_number[1]=='4' or self.card_number[1]=='5'):
					return "MASTERCARD"
				else:
					return "INVALID"
			elif (self.card_number[0]=='3' and (self.card_number[1]=='4' or self.card_number[1]=='7')):
				return "AMEX"	
			elif (self.card_number[0]=='6' and self.card_number[1]=='0' and self.card_number[2]=='1' and self.card_number[3]=='1'):
				return "DISCOVER"
			else:
				return "INVALID"
		else:
			return "INVALID"




#Create and add your method called `check_length` to the CreditCard class here:
	def check_length(self):
		length=len(self.card_number)
		if (length==16):
			if(self.card_number[0]=='4'):
				return True
			elif (self.card_number[0]=='5'):
				if (self.card_number[1]=='1' or self.card_number[1]=='2' or self.card_number[1]=='3' or self.card_number[1]=='4' or self.card_number[1]=='5'):
					return True
				else:
					return False
			elif (self.card_number[0]=='6' and self.card_number[1]=='0' and self.card_number[2]=='1' and self.card_number[3]=='1'):
				return True
		elif (length==15 and self.card_number[0]=='3'):
		 		if(self.card_number[1]=='4' or self.card_number[1]=='7'):
		 			return True
		 		else:
		 			return False
		else:
			return False

#Create and add your method called 'validate' to the CreditCard class here:
	def validate(self):
		length=len(self.card_number)
		mynumberlist=[]
		if (self.check_length()==True):
		
			for i in range(length):
				mynumberlist.append(int(self.card_number[i]))

			mynumberlist.reverse()
		
			for j in range(1,length, 2):
				mynumberlist[j]*=2
			
		
			mynewcardstring="".join(["%s" % el for el in mynumberlist])
		

			cardnumsum=0
			for m in range(len(mynewcardstring)):
				cardnumsum+=int(mynewcardstring[m])
			
		
			if(cardnumsum%10==0):
				return True
			else:
				return False
		else:
			return False






mycreditc=CreditCard("4329876355493470")
print ("mycreditc cardtype:"+ mycreditc.determine_card_type())
print ("mycreditc validate: "+ str(mycreditc.valid))
print ("mycreditc length:"+str(mycreditc.check_length()))
print ("mycreditc[0]:"+ mycreditc.card_number[0])




#do not modify assert statements

cc = CreditCard('9999999999999999')

assert cc.valid == False, "Credit Card number cannot start with 9"
assert cc.card_type == "INVALID", "99... card type is INVALID"

cc = CreditCard('4440')

assert cc.valid == False, "4440 is too short to be valid"
assert cc.card_type == "INVALID", "4440 card type is INVALID"

cc = CreditCard('5515460934365316')

assert cc.valid == True, "Mastercard is Valid"
assert cc.card_type == "MASTERCARD", "card_type is MASTERCARD"

cc = CreditCard('6011053711075799')

assert cc.valid == True, "Discover Card is Valid"
assert cc.card_type == "DISCOVER", "card_type is DISCOVER"

cc = CreditCard('379179199857686')

assert cc.valid == True, "AMEX is Valid"
assert cc.card_type == "AMEX", "card_type is AMEX"

cc = CreditCard('4929896355493470')

assert cc.valid == True, "Visa Card is Valid"
assert cc.card_type == "VISA", "card_type is VISA"

cc = CreditCard('4329876355493470')

assert cc.valid == False, "This card does not meet mod10"
assert cc.card_type == "INVALID", "card_type is INVALID"

cc = CreditCard('339179199857685')

assert cc.valid == False, "Validates mod10, but invalid starting numbers for AMEX"
assert cc.card_type == "INVALID", "card_type is INVALID"