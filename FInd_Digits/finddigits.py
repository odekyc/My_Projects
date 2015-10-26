def digits_evenly_divide(num_list):
	index=0
	divisible_list=[]
	while index<len(num_list):
		num=int(num_list[index])
		num_digits=len(num_list[index])
		subindex=0
		divisible_count=0
		while subindex<num_digits:
			digit=int(num_list[index][subindex])
			subindex+=1
			if digit!=0:
				if num%digit==0:
					divisible_count+=1
		divisible_list.append(divisible_count)
		index+=1
	return divisible_list




n=int(input())
index=0
num_list=[]

while index<n:
	num_list.append(input())
	index+=1

result_list=digits_evenly_divide(num_list)
for num in result_list:
	print (num)
