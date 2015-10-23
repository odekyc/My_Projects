def quicksort(listoflist):

	finallist=[]
	count=0
	for i in range(len(listoflist)):
		if (len(listoflist[i])==1):
			count+=1
			finallist.extend(partition(listoflist[i]))
		else:
			finallist.extend(partition(listoflist[i]))
			

	if (count>=1):
		return combine(finallist)
	else:	
		return quicksort(finallist)

def partition(mylist):
	part_list=[]
	smallerlist=[]
	biggerlist=[]
	mid_index=int(len(mylist)/2)
	countsamemid=0
	for i in range(len(mylist)):
		if(mylist[i]<mylist[mid_index]):
			smallerlist.append(mylist[i])
		elif (mylist[i]>mylist[mid_index]):
			biggerlist.append(mylist[i])
		elif (mylist[i]==mylist[mid_index]):
			countsamemid+=1

	

	if (countsamemid>0):
		x=0
		while (x<countsamemid):
			smallerlist.append(mylist[mid_index])
			x+=1
	elif (countsamemid==0):
		smallerlist.append(mylist[mid_index])

	
	part_list.append(smallerlist)
	if (biggerlist!=[]):
		part_list.append(biggerlist)


	return part_list

def combine(listoflist):
	combined=[]
	for i in range(len(listoflist)):
		for x in range(len(listoflist[i])):
			combined.append(listoflist[i][x])

	return combined


print (quicksort([[4, 2, 5, 8,0, 6 , 8, 6, 17, 20,3 ,0,0,0,0]]))

def assertion(actualAnswer, expectedAnswer):
    print("Your answer:    " + str(actualAnswer))
    print("Expected answer: " + str(expectedAnswer))
    print(actualAnswer == expectedAnswer)

assertion(quicksort([[4, 2, 5, 8, 6]]), [2, 4, 5, 6, 8])
