def insertion_sort(my_list):
	break_pos=1
	#the break position is the position in the list that breaks our list into two portions, one is the unsorted portion, another is the sorted portion
	start_unsorted=break_pos
	#for the unsorted portion of our list, we start from the position start_unsorted in our unsorted portion
	while (break_pos<len(my_list)):
		insert_num=my_list.pop(break_pos)
		i=0
		while i<break_pos:
			if my_list[i]>insert_num:
				my_list.insert(i,insert_num)
				i+=2
				break
			elif (i==break_pos-1) and my_list[i]<insert_num:
				my_list.insert(i+1, insert_num)
				i+=1
			else:
				i+=1

		break_pos+=1


		

	return my_list

			
print (insertion_sort([5,19,4,1,36,99,2]))




assert insertion_sort([5,19,4,1,36,99,2]) == sorted([5,19,4,1,36,99,2])
assert insertion_sort(["Greg", "Armen", "Ken"]) == sorted(["Greg", "Armen", "Ken"])
