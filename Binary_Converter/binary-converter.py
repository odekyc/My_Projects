decimal_num=input("Enter a decimal number and I shall change it to binary number : ")
binary_num=input("Enter a binary number and I shall return its decimal counterpart : ")
mydecnum=int(decimal_num)

def decimal_to_binary(num):
	binarynumlist=[]
	
	for i in range(32,-1,-1):
		if ((2**i)<=num):
			break
	
	for x in range(i, -1, -1):
		if ((2**x)>num):
			binarynumlist.append(0)
			
			
		elif ((2**x)<=num):
			num-=2**x
			binarynumlist.append(1)

	for y in range(len(binarynumlist)):
		binarynumlist[y]=str(binarynumlist[y])
	binarynumstring="".join(binarynumlist)

	return int(binarynumstring)		
	
    

print (decimal_to_binary(mydecnum))

def binary_to_decimal(num):
	
	binarynum=int(num)
	decimalnum=0
	for i in range(32):
		
		
		decimalnum+=round((2**i)*(binarynum%10))
		
		binarynum=round(binarynum/10)
		
	return decimalnum

print (binary_to_decimal(binary_num))





	

	


	


assert binary_to_decimal(0) == 0, "0 to decimal should return 0"
assert binary_to_decimal(1011) == 11, "1011 to decimal should return 11"
assert binary_to_decimal(101011) == 43, "101011 to decimal should return 43"
assert binary_to_decimal(101011101) == 349, "101011101 to decimal should return 349"

assert decimal_to_binary(0) == 0, "0 to binary should return 0"
assert decimal_to_binary(5) == 101, "5 to binary should return 101"
assert decimal_to_binary(10) == 1010, "10 to binary should return 1010"
assert decimal_to_binary(113) == 1110001, "113 to binary should return 1110001"
