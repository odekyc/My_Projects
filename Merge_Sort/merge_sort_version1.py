def merge_sort(arr):
	
	
	finallist=[]
	index=0
	while (index<len(arr)):
		if ((index+1)<len(arr)):
			finallist.append(combinelist(arr[index], arr[index+1]))
		elif ((index)==(len(arr)-1) and (index+1)==len(arr)):
			finallist.append(combinelist(arr[index],[] ))

		index+=2
	
	arr2=finallist[:]
	
	if (len(arr2)>1):
		return (merge_sort(arr2))
	elif(len(arr2)==1):
		return arr2


	



				
			




def combinelist(list1, list2):
	combinedl=[]
	index1=0
	index2=0
	if (len(list1)==0 and len(list2)>0):
		combinedl=list2[:]
	elif (len(list2)==0 and len(list1)>0):
		combinedl=list1[:]
	elif (len(list1)>0 and len(list2)>0):
		while (index1<len(list1) and index2<len(list2)):
			if (list1[index1]<list2[index2]):
				combinedl.append(list1[index1])
				index1+=1
			elif (list2[index2]<list1[index1]):
				combinedl.append(list2[index2])
				index2+=1
			elif (list1[index1]==list2[index2]):
				combinedl.append(list1[index1])
				combinedl.append(list2[index2])
				index1+=1
				index2+=1
		if (index1==len(list1) and index2!=len(list2)):
			finalindex=len(combinedl)-1
		
			slicelist2=list2[index2:]
			combinedl=combinedl+slicelist2

		elif (index1!=len(list1) and index2==len(list2)):
			finalindex=len(combinedl)-1
		
			slicelist1=list1[index1:]
			combinedl=combinedl+slicelist1


	return combinedl





def listbreak(arr):

	brokenlist=[[] for x in range(len(arr))]

	for i in range(len(arr)):
		brokenlist[i].append(arr[i])

	return brokenlist


brokenlist=listbreak([98, 744, 28, 81, 447, 447, 2, 5, 10, 99, 55,66])

print (merge_sort(brokenlist))