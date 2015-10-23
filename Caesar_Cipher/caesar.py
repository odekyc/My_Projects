usermsg=input("Enter a message and I shall convert it to Caesar Cipher: ")
usershiftnum=input("Enter a shift number for the number of shifts for characters in the message, enter a positive number for right shift, enter a negative number for left shift: ")
def caesar(message, shift):
	caesarmessagelist=[]
	for i in range(len(message)):
		asciinum=ord(message[i])
		if (asciinum>=97 and asciinum<=122):
			asciinum+=int(shift)
			if (int(shift)<0 and asciinum<97):
				asciinum=123-(97-asciinum)

			elif (int(shift)>0 and asciinum>122):
				asciinum=(asciinum-122-1)+97
		elif (asciinum>=65 and asciinum<=90):
			asciinum+=int(shift)
			if(int(shift)<0 and asciinum<65):
				asciinum=91-(65-asciinum)
			elif (int(shift)>0 and asciinum>90):
				asciinum=(asciinum-90-1)+65
		else:
			asciinum=asciinum

		caesarmessagelist.append(chr(asciinum))
		caesarstring="".join(caesarmessagelist)
	return caesarstring

def decipher(message, shift):
	deciphermsglist=[]
	for i in range(len(message)):
		asciinum=ord(message[i])
		if (asciinum>=97 and asciinum<=122):
			asciinum-=int(shift)
			if(int(shift)>0 and asciinum<97):
				asciinum=122-(97-asciinum)+1
			elif (int(shift)<0 and asciinum>122):
				asciinum=97+(asciinum-122)-1
		elif (asciinum>=65 and asciinum<=90):
			asciinum-=int(shift)
			if(int(shift)>0 and asciinum<65):
				asciinum=90-(65-asciinum)+1
			elif (int(shift)<0 and asciinum>90):
				asciinum=65+(asciinum-90)-1
		else:
			asciinum=asciinum
		deciphermsglist.append(chr(asciinum))
		decipherstring="".join(deciphermsglist)
	return decipherstring


    
print (caesar(usermsg,usershiftnum))
caesarciphermsg=caesar(usermsg,usershiftnum)
print (decipher(caesarciphermsg, usershiftnum))

test1=caesar("apple", -3)
assert test1=="xmmib", "True:caesar(if (int(shift)<0 and asciinum<97)) "
assert decipher(test1, -3)=="apple", "True: decipher(elif (int(shift)<0 and asciinum>122))"
test2=caesar(" _//$?}< ", -5) 
assert test2==" _//$?}< ", "true: caesar if the asciinum is not within 97-122 or 65-90"
assert decipher(test2, -5)==" _//$?}< ", "true: decipher if the asciinum is not within 97-122 or 65-90 "
test3=caesar("xyz", 4)
assert test3=="bcd", "true: test caesar(elif (int(shift)>0 and asciinum>122):)"
assert decipher(test3,4)=="xyz", "true: decipher (if(int(shift)>0 and asciinum<97):)"
test4=caesar("BEAST", -4)
assert test4=="XAWOP", "true: test caesar(if(int(shift)<0 and asciinum<65))"
assert decipher(test4, -4)=="BEAST", "true: test decipher (elif (int(shift)<0 and asciinum>90):)"
test5=caesar("XRAY",10)
assert test5=="HBKI", "true: test caesar(if(int(shift)>0 and asciinum<65):)"
assert decipher(test5,10)=="XRAY", "true: test decipher(if(int(shift)>0 and asciinum<65):) "
test6=caesar("What the ^^^? Hell+=is your problemzz@!", 10)
assert test6=="Grkd dro ^^^? Rovv+=sc iyeb zbylvowjj@!","true:test caesar(): symbol when concatenated with capital and lowercase letters "
assert decipher(test6, 10)=="What the ^^^? Hell+=is your problemzz@!", "true: decipher(): symbol when concatenated with capital and lowercase letters "

# Add your own assert statements to test your code.