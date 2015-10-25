def diagonal_diff(matrix):
	index=0
	sum1=0
	while index<len(matrix):
		sum1+=int(matrix[index][index])
		index+=1

	indexr=0
	indexc=len(matrix)-1
	sum2=0
	while indexr<len(matrix):
		sum2+=int(matrix[indexr][indexc])
		indexc-=1
		indexr+=1
	return abs(sum1-sum2)

n=int(input())
my_matrix=[]
index=0
while index<n:
	my_matrix.append(input().split(' '))
	index+=1

diff=diagonal_diff(my_matrix)
print (diff)