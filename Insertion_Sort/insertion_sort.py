def insertion_sort(arr):

   
	i=0
	while (i < len(arr)):
		insertvalue=arr.pop(i)
		
		x=0
		count=0
		repeatnum=0
		while (x<len(arr)):
			if (insertvalue > arr[x]):
				count+=1
			elif(insertvalue==arr[x]):
				repeatnum+=1
			x+=1

		if (count > 0 and count!=i and repeatnum==0):
			arr.insert(count, insertvalue)
		elif (count >0 and count!=i and repeatnum>0):
			arr.insert(count,insertvalue)
			i+=1
		else:
			arr.insert(i, insertvalue)
			i+=1
				
	
		

	return arr

myarr=[8,56,56,10,42,42,99,16,72]
print (insertion_sort(myarr))





assert insertion_sort([5,19,4,1,36,99,2]) == sorted([5,19,4,1,36,99,2])
assert insertion_sort(["Greg", "Armen", "Ken"]) == sorted(["Greg", "Armen", "Ken"])
