def cancel_class(lista, listb, num):
	result_list=[]
	index=0
	while index<num:
		ontime_students=0

		for elements in listb[index]:
			if int(elements)<=0:
				ontime_students+=1

		if ontime_students>=int(lista[index][1]):
			result_list.append('NO')
		else:
			result_list.append('YES')
		index+=1
	return result_list

n=int(input())

count=0
list1=[]
list2=[]
while count<n:
	list1.append(input().split(' '))
	list2.append(input().split(' '))
	count+=1

class_cancel_list=cancel_class(list1, list2, n)

for element in class_cancel_list:
	print (element)