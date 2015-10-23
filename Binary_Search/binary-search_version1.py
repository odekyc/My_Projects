def binary_search(dataset, value):
	

	mid_index=int(len(dataset)/2)
	actualindex=mid_index
	while (len(dataset)>0):
		if (dataset[mid_index]>value):
			dataset=dataset[:mid_index]
			mid_index=int(len(dataset)/2)
			actualindex-=(len(dataset)-mid_index)
		elif (dataset[mid_index]<value):
			
			dataset=dataset[mid_index:]
			mid_index=int(len(dataset)/2)
			actualindex+=mid_index
		elif (dataset[mid_index]==value):
			return "the value is at index number :" +str(actualindex) +" of your list"
	if (len(dataset)==0):
		return False	


##sample dataset
arr = [1,3,9,11,23,44,66,88,102,142,188,192,239,382,492,1120,1900,2500,4392,5854,6543,8292,9999,29122]

test = [1,2,3,4,5,6]
print (binary_search(arr, 382))