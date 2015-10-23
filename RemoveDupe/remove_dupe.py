mystring="aabbccddeded"
def remove_duplicate(string):
	mylist=[]
	mynewlist=[]
	for ch in string:
		mylist.append(ch)

	number=1
	length=len(mylist)
	while (number< length):
		if(mylist[number]==mylist[number-1]):
			mynewlist.append(mylist[number])
			mylist.pop(number-1)
			length=len(mylist)
		else:
			number+=1
	print ("".join(mylist))
	print ("".join(mynewlist))

remove_duplicate(mystring)