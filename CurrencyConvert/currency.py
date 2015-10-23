amount=input("Enter the amount of money in USD : ")
def bills_coins(amount) :
	hundredbills=int(float(amount)/100)
	hundredbillremainder=float(amount)%100
	fiftybills=int(hundredbillremainder/50)
	fiftybillremainder=hundredbillremainder%50
	tenbills=int(fiftybillremainder/10)
	tenbillremainder=fiftybillremainder%10
	fivebills=int(tenbillremainder/5)
	fivebillremainder=tenbillremainder%5
	onebills=int(fivebillremainder/1)
	onebillremainder=fivebillremainder%1
	quarters=int(onebillremainder/0.25)
	quarterremainder=onebillremainder%0.25
	dimes=int(quarterremainder/0.1)
	dimeremainder=quarterremainder%0.1
	print (str(dimeremainder))
	nickels=int(dimeremainder/0.05)
	nickelremainder=dimeremainder%0.05
	pennys=int(round(nickelremainder/0.01, 0))
	print ("hundred bills : "+str(hundredbills))
	print ("fifty bills : "+str(fiftybills))
	print ("ten bills : " +str(tenbills))
	print ("five bills : "+str(fivebills))
	print ("one bills : "+ str(onebills))
	print ("quarters : " + str(quarters))
	print ("dimes : "+str(dimes))
	print ("nickels : "+str(nickels))
	print ("pennys : "+str(pennys))
bills_coins(amount)

