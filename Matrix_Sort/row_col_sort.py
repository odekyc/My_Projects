myfile=open('testmatrix.txt','r')
split_matrix=myfile.read().splitlines()
print (split_matrix)
new_matrix=[]
for row in range(len(split_matrix)):
	new_matrix.append(split_matrix[row].split(' '))

print (new_matrix)
rowsum_matrix=[]

for row in range(len(split_matrix)):
	rowsum=0
	for i in range(len(new_matrix[row])):
		rowsum+=int(new_matrix[row][i])
	rowsum_matrix.append(rowsum)

print (rowsum_matrix)

colsum_matrix=[]
for col in range (len(new_matrix[row])):
	colsum=0
	for row in range(len(split_matrix)):
		colsum+=int(new_matrix[row][col])
	colsum_matrix.append(colsum)

print (colsum_matrix)
mydict=dict()

for row in range(len(split_matrix)):
	rowsum=0
	for i in range(len(new_matrix[row])):
		rowsum+=int(new_matrix[row][i])
	mydict.update({rowsum:new_matrix[row]})
print (mydict)

listrowsum=sorted(mydict.keys())
print (listrowsum)

for key in listrowsum:
	print (mydict[key])
dictcolsum={}
listcols=[[] for x in range(len(new_matrix[0]))]
for col in range(len(new_matrix[row])):
	colsum=0
	for row in range (len(split_matrix)):
		colsum+=int(new_matrix[row][col])
		listcols[col].append(new_matrix[row][col])

	dictcolsum.update({colsum:listcols[col]})
print (listcols)
print (dictcolsum)
listcolsum=sorted(dictcolsum.keys())
print (listcolsum)
listsortedcols=[[] for x in range(len(split_matrix))]

	
for y in range(len(split_matrix)):	
	
	for i in range(len(listcolsum)):
			
		listsortedcols[y].append(dictcolsum[listcolsum[i]][y])

print (listsortedcols)