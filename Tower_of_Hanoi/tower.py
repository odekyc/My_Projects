num_disk=int(input("Please enter the number of disks in your Tower of Hanoi game : "))


def game(my_disk_num):
	print ("this game has "+str(num_disk)+" number of disks!")
	print (" each disc is represented by a number. the smaller the number of the disk, it means the size of the disk is smaller. on the contrary, the bigger the number of the disk, it means the disk size is larger!")
	last_dic=my_disk_num
	rod_1=[]
	rod_2=[]
	rod_3=[]
	allrods=[]
	movenum=0
	num=1
	allrods.append(rod_1)
	allrods.append(rod_2)
	allrods.append(rod_3)
	
	while (num<=my_disk_num):
		rod_1.append(num)
		num+=1	

		
	while (movenum<=pow(2,num_disk)-1):
		print (allrods)
			
		if (len(rod_1)>0 and rod_1[0]==1):
			rod_1.remove(1)
			index_wit_1=0
		elif (len(rod_2)>0 and rod_2[0]==1):
			rod_2.remove(1)
			index_wit_1=1
		elif (len(rod_3)>0 and rod_3[0]==1):
			rod_3.remove(1)
			index_wit_1=2

		if (my_disk_num%2==1):
		
			if (index_wit_1==0):
				index_wit_1=2
			else:
				index_wit_1-=1
		elif (my_disk_num%2==0):
			if (index_wit_1==2):
				index_wit_1=0
			else:
				index_wit_1+=1

		allrods[index_wit_1].insert(0,1)
		print (allrods)
		movenum+=1
		if (movenum==pow(2,num_disk)-1):
			break
		if (len(rod_1)>0 and rod_1[0]==2):
			prev_rod_2=rod_1
			rod_1.remove(2)
		elif (len(rod_2)>0 and rod_2[0]==2):
			prev_rod_2=rod_2
			rod_2.remove(2)
		elif (len(rod_3)>0 and rod_3[0]==2):
			prev_rod_2=rod_3
			rod_3.remove(2)


		if len(rod_3)>0 and rod_3[0]>2 and rod_3 is not prev_rod_2:
			rod_3.insert(0,2)
		elif len(rod_2)>0 and rod_2[0]>2 and rod_2 is not prev_rod_2:
			rod_2.insert(0,2)
		elif (rod_2==[] and rod_2 is not prev_rod_2):
			rod_2.insert(0,2)
		elif (rod_3==[] and rod_3 is not prev_rod_2):
			rod_3.insert(0,2)
		elif (rod_1==[] and prev_rod_2 is not rod_1):
			rod_1.insert(0,2)

		elif len(rod_1)>0 and rod_1[0]>2 and rod_1 is not prev_rod_2:
			rod_1.insert(0,2)
				
		print (allrods)
		movenum+=1
		if (len(rod_1)>0 and rod_1[0]==1):
			rod_1.remove(1)
			index_wit_1=0
		elif (len(rod_2)>0 and rod_2[0]==1):
			rod_2.remove(1)
			index_wit_1=1
		elif (len(rod_3)>0 and rod_3[0]==1):
			rod_3.remove(1)
			index_wit_1=2

		if (my_disk_num%2==1):
		
			if (index_wit_1==0):
				index_wit_1=2
			else:
				index_wit_1-=1
		elif (my_disk_num%2==0):
			if (index_wit_1==2):
				index_wit_1=0
			else:
				index_wit_1+=1

		allrods[index_wit_1].insert(0,1)
		print (allrods)
		movenum+=1
		if (movenum==pow(2,num_disk)-1):
			break
		if (len(rod_1)>0 and rod_1[0]==3):
			prev_rod_3=rod_1
			rod_1.remove(3)
			
		elif (len(rod_2)>0 and rod_2[0]==3):
			prev_rod_3=rod_2
			rod_2.remove(3)
				
		elif (len(rod_3)>0 and rod_3[0]==3):
			prev_rod_3=rod_3
			rod_3.remove(3)
			
		if len(rod_3)>0 and rod_3[0]>3 and prev_rod_3 is not rod_3:
			rod_3.insert(0,3)
		elif len(rod_2)>0 and rod_2[0]>3 and prev_rod_3 is not rod_2:
			rod_2.insert(0,3)
		elif (rod_2==[] and rod_2 is not prev_rod_3):
			rod_2.insert(0,3)
		elif (rod_3==[] and rod_3 is not prev_rod_3):
			rod_3.insert(0,3)
		elif (rod_1==[] and rod_1 is not prev_rod_3):
			rod_1.insert(0,3)
		elif len(rod_1)>0 and rod_1[0]>3 and prev_rod_3 is not rod_1:
			rod_1.insert(0,3)
			
		print (allrods)
		movenum+=1
		if (len(rod_1)>0 and rod_1[0]==1):
			rod_1.remove(1)
			index_wit_1=0
		elif (len(rod_2)>0 and rod_2[0]==1):
			rod_2.remove(1)
			index_wit_1=1
		elif (len(rod_3)>0 and rod_3[0]==1):
			rod_3.remove(1)
			index_wit_1=2

		if (my_disk_num%2==1):
		
			if (index_wit_1==0):
				index_wit_1=2
			else:
				index_wit_1-=1
		elif (my_disk_num%2==0):
			if (index_wit_1==2):
				index_wit_1=0
			else:
				index_wit_1+=1

		allrods[index_wit_1].insert(0,1)
		print (allrods)
		movenum+=1
		if (movenum==pow(2,num_disk)-1):
			break
		if (len(rod_1)>0 and rod_1[0]==2):
			prev_rod_2=rod_1
			rod_1.remove(2)
		elif (len(rod_2)>0 and rod_2[0]==2):
			prev_rod_2=rod_2
			rod_2.remove(2)
		elif (len(rod_3)>0 and rod_3[0]==2):
			prev_rod_2=rod_3
			rod_3.remove(2)


		if len(rod_3)>0 and rod_3[0]>2 and rod_3 is not prev_rod_2:
			rod_3.insert(0,2)
		elif len(rod_2)>0 and rod_2[0]>2 and rod_2 is not prev_rod_2:
			rod_2.insert(0,2)
		elif (rod_2==[] and rod_2 is not prev_rod_2):
			rod_2.insert(0,2)
		elif (rod_3==[] and rod_3 is not prev_rod_2):
			rod_3.insert(0,2)
		elif (rod_1==[] and prev_rod_2 is not rod_1):
			rod_1.insert(0,2)
		elif len(rod_1)>0 and rod_1[0]>2 and rod_1 is not prev_rod_2:
			rod_1.insert(0,2)
				
		print (allrods)
		movenum+=1
		if (len(rod_1)>0 and rod_1[0]==1):
			rod_1.remove(1)
			index_wit_1=0
		elif (len(rod_2)>0 and rod_2[0]==1):
			rod_2.remove(1)
			index_wit_1=1
		elif (len(rod_3)>0 and rod_3[0]==1):
			rod_3.remove(1)
			index_wit_1=2

		if (my_disk_num%2==1):
		
			if (index_wit_1==0):
				index_wit_1=2
			else:
				index_wit_1-=1
		elif (my_disk_num%2==0):
			if (index_wit_1==2):
				index_wit_1=0
			else:
				index_wit_1+=1

		allrods[index_wit_1].insert(0,1)

		print (allrods)
		movenum+=1
		if (movenum==pow(2,num_disk)-1):
			break
		if len(rod_1)>0 and rod_1[0] not in [1,2,3] :
			bigdisnum=rod_1.pop(0)
			if (rod_2==[]):
				rod_2.insert(0,bigdisnum)
			elif (rod_3==[]):
				rod_3.insert(0,bigdisnum)
			elif len(rod_2)>0 and rod_2[0]>bigdisnum :
				rod_2.insert(0,bigdisnum)
			elif len(rod_3)>0 and rod_3[0]>bigdisnum :
				rod_3.insert(0,bigdisnum)
			else:
				rod_1.insert(0,bigdisnum)
				if len(rod_2)>0 and rod_2[0] not in [1,2,3, last_dic]:
					prev_rod_bigdic=rod_2	
					bigdisnum=rod_2.pop(0)
					if len(rod_3)>0 and rod_3[0]>bigdisnum and rod_3 is not prev_rod_bigdic:
						rod_3.insert(0,bigdisnum)
					elif len(rod_1)>0 and rod_1[0]>bigdisnum and rod_1 is not prev_rod_bigdic:
						rod_1.insert(0,bigdisnum)
					else:
						rod_2.insert(0,bigdisnum)

				elif len(rod_3)>0 and rod_3[0] not in [1,2,3, last_dic]:
					prev_rod_bigdic=rod_3
					bigdisnum=rod_3.pop(0)
				
					if len(rod_2)>0 and rod_2[0]>bigdisnum and rod_2 is not prev_rod_bigdic:
						rod_2.insert(0,bigdisnum)

					elif len(rod_1)>0 and rod_1[0]>bigdisnum and rod_1 is not prev_rod_bigdic:
						rod_1.insert(0,bigdisnum)
					else:
						rod_3.insert(0,bigdisnum)

		elif len(rod_1)>0 and rod_1[0] in [1,2,3]:
			if len(rod_3)>0 and rod_3[0] not in [1,2,3, last_dic] and len(rod_2)>0 and rod_2[0] not in [1,2,3, last_dic]:
				if (rod_2[0]>rod_3[0]):
					prev_rod_bigdic=rod_3
					bigdisnum=rod_3.pop(0)
					rod_2.insert(0,bigdisnum)
				elif (rod_3[0]>rod_2[0]):
					prev_rod_bigdic=rod_2
					bigdisnum=rod_2.pop(0)
					rod_3.insert(0,bigdisnum)

			elif len(rod_2)>0 and rod_2[0] not in [1,2,3, last_dic] :
				prev_rod_bigdic=rod_2	
				bigdisnum=rod_2.pop(0)
				if len(rod_3)>0 and rod_3[0]>bigdisnum and rod_3 is not prev_rod_bigdic:
					rod_3.insert(0,bigdisnum)
				elif len(rod_1)>0 and rod_1[0]>bigdisnum and rod_1 is not prev_rod_bigdic:
					rod_1.insert(0,bigdisnum)
				else:
					rod_2.insert(0,bigdisnum)
					
						
			elif len(rod_3)>0 and rod_3[0] not in [1,2,3, last_dic] :
				prev_rod_bigdic=rod_3
				bigdisnum=rod_3.pop(0)
				
				if len(rod_2)>0 and rod_2[0]>bigdisnum and rod_2 is not prev_rod_bigdic:
					rod_2.insert(0,bigdisnum)

				elif len(rod_1)>0 and rod_1[0]>bigdisnum and rod_1 is not prev_rod_bigdic:
					rod_1.insert(0,bigdisnum)
				else:
					rod_3.insert(0,bigdisnum)

		elif rod_1==[]:
			if len(rod_2)>0 and rod_2[0] not in [1,2,3, last_dic] :
				bigdisnum=rod_2.pop(0)
				rod_1.insert(0,bigdisnum)
			elif len(rod_3)>0 and rod_3[0] not in [1,2,3, last_dic] :
				bigdisnum=rod_3.pop(0)
				rod_1.insert(0,bigdisnum)
		movenum+=1
		if (movenum==pow(2,num_disk)-1):
			break




			
		


			

			

#	elif (my_disk_num%2==0):	
game(num_disk)





