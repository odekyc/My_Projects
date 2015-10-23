def merge_sort(list_of_arr):

	new_arr_list=[]
	list_arr_len=len(list_of_arr)


	if list_arr_len==1:
		return list_of_arr[0]
	else:
		if list_arr_len%2==1:
			arr_last_list=list_of_arr.pop(list_arr_len-1)

		arr_index=1
		while arr_index<len(list_of_arr):
			
		
			fused_list=[]
				
			len_1=len(list_of_arr[arr_index-1])
			len_2=len(list_of_arr[arr_index])
			num_1=list_of_arr[arr_index-1].pop(0)
			num_2=list_of_arr[arr_index].pop(0)
			while len(fused_list)<len_1+len_2:
				if (num_1>num_2):
					fused_list.append(num_2)
					if len(list_of_arr[arr_index])>0:
						num_2=list_of_arr[arr_index].pop(0)
					else:
						num_2=None

				elif (num_1<num_2):
					fused_list.append(num_1)
					if len(list_of_arr[arr_index-1])>0:
						num_1=list_of_arr[arr_index-1].pop(0)
					else:
						num_1=None
					
				elif (num_1==num_2):
					fused_list.append(num_1)
					fused_list.append(num_2)

					if len(list_of_arr[arr_index])>0:
						num_2=list_of_arr[arr_index].pop(0)
					else:
						num_2=None

					if len(list_of_arr[arr_index-1])>0:
						num_1=list_of_arr[arr_index-1].pop(0)
					else:
						num_1=None


				if num_1==None and num_2==None:
					break
				elif num_1==None and num_2!=None:
					fused_list.append(num_2)
					for num in list_of_arr[arr_index]:
						fused_list.append(num)
				elif num_1!=None and num_2==None:
					fused_list.append(num_1)
					for num in list_of_arr[arr_index-1]:
						fused_list.append(num)
			new_arr_list.append(fused_list)
			arr_index+=2
	if list_arr_len%2==1:
		new_arr_list.append(arr_last_list)
	return merge_sort(new_arr_list)




	


def break_list(arr):
	length=len(arr)
	list_of_arr=[]
	for arr_index in range(length):
		list_of_arr.append([arr[arr_index]])
	return list_of_arr
	
broken_list=break_list([ 98,98, 744,744,744,744, 28, 81, 447,447, 2, 5, 10, 99, 55,55, 55])


print (merge_sort(broken_list))
