usernum=input("Enter a number up to 4999 (include) and I should convert it to Roman numerals : ")
def to_roman(num):
	length=len(num)
	mynum=list(num)
	
	print (mynum)
	mynum.reverse()

	if (length==1):
		if (mynum[0]=='0'):
			mynum[0]=" "
		elif (mynum[0]=='1'):
			mynum[0]='I'
		elif (mynum[0]=='2'):
			mynum[0]='II'
		elif (mynum[0]=='3'):
			mynum[0]='III'
		elif (mynum[0]=='4'):
			mynum[0]='IV'
		elif (mynum[0]=='5'):
			mynum[0]='V'
		elif (mynum[0]=='6'):
			mynum[0]='VI'
		elif (mynum[0]=='7'):
			mynum[0]='VII'
		elif (mynum[0]=='8'):
			mynum[0]='VIII'
		elif (mynum[0]=='9'):
			mynum[0]='IX'
		else:
			print ("you didn't input the right number at the 1th digit!")
	elif (length==2):
		if (mynum[1]=='0'):
			mynum[1]=' '
		elif (mynum[1]=='1'):
			mynum[1]='X'
		elif (mynum[1]=='2'):
			mynum[1]='XX'
		elif (mynum[1]=='3'):
			mynum[1]='XXX'
		elif (mynum[1]=='4'):
			mynum[1]='XL'
		elif (mynum[1]=='5'):
			mynum[1]='L'
		elif (mynum[1]=='6'):
			mynum[1]='LX'
		elif (mynum[1]=='7'):
			mynum[1]='LXX'
		elif (mynum[1]=='8'):
			mynum[1]='LXXX'
		elif (mynum[1]=='9'):
			mynum[1]='XC'
		else :
			print ("you didn't input the right number at the 10th digit!")
		
		if (mynum[0]=='0'):
			mynum[0]=" "
		elif (mynum[0]=='1'):
			mynum[0]='I'
		elif (mynum[0]=='2'):
			mynum[0]='II'
		elif (mynum[0]=='3'):
			mynum[0]='III'
		elif (mynum[0]=='4'):
			mynum[0]='IV'
		elif (mynum[0]=='5'):
			mynum[0]='V'
		elif (mynum[0]=='6'):
			mynum[0]='VI'
		elif (mynum[0]=='7'):
			mynum[0]='VII'
		elif (mynum[0]=='8'):
			mynum[0]='VIII'
		elif (mynum[0]=='9'):
			mynum[0]='IX'
		else:
			print ("you didn't input the right number at the 1th place!")
	elif(length==3):
		if (mynum[2]=='0'):
			mynum[2]=' '
		elif (mynum[2]=='1'):
			mynum[2]='C'
		elif (mynum[2]=='2'):
			mynum[2]='CC'
		elif (mynum[2]=='3'):
			mynum[2]='CCC'
		elif (mynum[2]=='4'):
			mynum[2]='CD'
		elif (mynum[2]=='5'):
			mynum[2]='D'
		elif (mynum[2]=='6'):
			mynum[2]='DC'
		elif (mynum[2]=='7'):
			mynum[2]='DCC'

		elif (mynum[2]=='8'):
			mynum[2]='DCCC'
		elif (mynum[2]=='9'):
			mynum[2]='CM'
		else:
			print ("you didn't input the right number at the 100th place!")
		if (mynum[1]=='0'):
			mynum[1]=' '
		elif (mynum[1]=='1'):
			mynum[1]='X'
		elif (mynum[1]=='2'):
			mynum[1]='XX'
		elif (mynum[1]=='3'):
			mynum[1]='XXX'
		elif (mynum[1]=='4'):
			mynum[1]='XL'
		elif (mynum[1]=='5'):
			mynum[1]='L'
		elif (mynum[1]=='6'):
			mynum[1]='LX'
		elif (mynum[1]=='7'):
			mynum[1]='LXX'
		elif (mynum[1]=='8'):
			mynum[1]='LXXX'
		elif (mynum[1]=='9'):
			mynum[1]='XC'
		else :
			print ("you didn't input the right number at your 10th digit!")
		if (mynum[0]=='0'):
			mynum[0]=" "
		elif (mynum[0]=='1'):
			mynum[0]='I'
		elif (mynum[0]=='2'):
			mynum[0]='II'
		elif (mynum[0]=='3'):
			mynum[0]='III'
		elif (mynum[0]=='4'):
			mynum[0]='IV'
		elif (mynum[0]=='5'):
			mynum[0]='V'
		elif (mynum[0]=='6'):
			mynum[0]='VI'
		elif (mynum[0]=='7'):
			mynum[0]='VII'
		elif (mynum[0]=='8'):
			mynum[0]='VIII'
		elif (mynum[0]=='9'):
			mynum[0]='IX'
		else:
			print ("you didn't input the right number at the 1th place!")
	elif(length==4):
		if (mynum[3]=='0'):
			mynum[3]=' '
		elif (mynum[3]=='1'):
			mynum[3]='M'
		elif (mynum[3]=='2'):
			mynum[3]='MM'
		elif (mynum[3]=='3'):
			mynum[3]='MMM'
		elif (mynum[3]=='4'):
			mynum[3]='MMMM'
		elif (mynum[3]=='5' or mynum[3]=='6' or mynum[3]=='7' or mynum[3]=='8' or mynum[3]=='9'):
			print ("you entered a number more than 4999")
		else :
			print ("you didn't enter the right number at the 1000th place")
		if (mynum[2]=='0'):
			mynum[2]=' '
		elif (mynum[2]=='1'):
			mynum[2]='C'
		elif (mynum[2]=='2'):
			mynum[2]='CC'
		elif (mynum[2]=='3'):
			mynum[2]='CCC'
		elif (mynum[2]=='4'):
			mynum[2]='CD'
		elif (mynum[2]=='5'):
			mynum[2]='D'
		elif (mynum[2]=='6'):
			mynum[2]='DC'
		elif (mynum[2]=='7'):
			mynum[2]='DCC'

		elif (mynum[2]=='8'):
			mynum[2]='DCCC'
		elif (mynum[2]=='9'):
			mynum[2]='CM'
		else:
			print ("you didn't input the right number at the 100th place!")
		if (mynum[1]=='0'):
			mynum[1]=' '
		elif (mynum[1]=='1'):
			mynum[1]='X'
		elif (mynum[1]=='2'):
			mynum[1]='XX'
		elif (mynum[1]=='3'):
			mynum[1]='XXX'
		elif (mynum[1]=='4'):
			mynum[1]='XL'
		elif (mynum[1]=='5'):
			mynum[1]='L'
		elif (mynum[1]=='6'):
			mynum[1]='LX'
		elif (mynum[1]=='7'):
			mynum[1]='LXX'
		elif (mynum[1]=='8'):
			mynum[1]='LXXX'
		elif (mynum[1]=='9'):
			mynum[1]='XC'
		else :
			print ("you didn't input the right number at your 10th digit!")
		if (mynum[0]=='0'):
			mynum[0]=" "
		elif (mynum[0]=='1'):
			mynum[0]='I'
		elif (mynum[0]=='2'):
			mynum[0]='II'
		elif (mynum[0]=='3'):
			mynum[0]='III'
		elif (mynum[0]=='4'):
			mynum[0]='IV'
		elif (mynum[0]=='5'):
			mynum[0]='V'
		elif (mynum[0]=='6'):
			mynum[0]='VI'
		elif (mynum[0]=='7'):
			mynum[0]='VII'
		elif (mynum[0]=='8'):
			mynum[0]='VIII'
		elif (mynum[0]=='9'):
			mynum[0]='IX'
		else:
			print ("you didn't input the right number at the 1th place!")
	myromannumstring="".join(mynum)
	mynum=myromannumstring.split(' ')
	
	mynum.reverse()
	myromannumstring="".join(mynum)
	print (myromannumstring)




to_roman(usernum)







assert to_roman(11) == "XI", "11 should return XI"
assert to_roman(60) == "LX", "60 should return LX"
assert to_roman(78) == "LXXVIII", "78 should return LXXVIII"
assert to_roman(4) == "IV", "4 should return IV"
assert to_roman(99) == "XCIX", "99 should return XCIX"

# Add your own assert tests below
