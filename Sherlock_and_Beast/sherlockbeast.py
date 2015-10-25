def largest_decent_num(mytestcases):
	decent_nums=[]
	n=len(mytestcases)
	index=0
	while index<n:
		if mytestcases[index]<3:
			decent_nums.append(-1)
		elif mytestcases[index]==3:
			decent_nums.append(555)
		elif mytestcases[index]==5:
			decent_nums.append(33333)
		else:
			i=0
			while i<1000000:
				y=3
				count=0
				while y<10000000:
					if mytestcases[index]==i+y:
						my_str='5'*y+'3'*i
						my_num=int(my_str)
						decent_nums.append(my_num)
						count+=1
						break
					y+=3
				if count==1:
					break
				i+=5
			if count==0:
				decent_nums.append(-1)
		index+=1

	return decent_nums
			    





		






n=int(input())
testcases=[]
index=0
while index<n:
	testcases.append(int(input()))
	index+=1

list_decent_num=largest_decent_num(testcases)
for num in list_decent_num:
	print (num)



