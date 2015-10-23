def binary_search(num_list, max_index, min_index, search_num):
	mid_index=int((max_index+min_index)/2)

	if min_index==max_index and num_list[mid_index]!=search_num:
		return False
	elif max_index<min_index:
		return False
	elif search_num>num_list[mid_index]:
		min_index=mid_index+1
		return binary_search(num_list,max_index,min_index,search_num)
	elif search_num<num_list[mid_index]:
		max_index=mid_index-1
		return binary_search(num_list,max_index,min_index,search_num)
	elif search_num==num_list[mid_index]:
		return True
	
	



##sample dataset
arr = [1,3,9,11,23,44,66,88,102,142,188,192,239,382,492,1120,1900,2500,4392,5854,6543,8292,9999,29122, 29122]
arr_len=len(arr)
print (binary_search(arr, arr_len-1, 0, 29122))

assert binary_search([-30,-30, -23,-15,-15,0,1,8,8],8, 0, 60)==False
assert binary_search([-40,-40,-20,-9,-2],4,0,0)==False
assert binary_search([3,4,7,13,13,13,20],6,0,13)==True
assert binary_search([-1,2,8,9,60,75],5,0,80)==False