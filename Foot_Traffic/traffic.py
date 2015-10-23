traffic_file=open('traffic.txt', 'r')
traffic_content=traffic_file.read().splitlines()
length=len(traffic_content)
traffic_content_I=[]
traffic_content_O=[]

print (traffic_content_I)

for lineindex in range(length):
	visitors=0
	traffic_line=traffic_content[lineindex]
	traffic_list=traffic_line.split(' ')
	traffic_line_I=[]
	traffic_line_O=[]
	if (traffic_list[2]=='I'):
		traffic_line_I.append(traffic_list[0])
		traffic_line_I.append(traffic_list[1])
		traffic_line_I.append(traffic_list[3])
		traffic_content_I.append(traffic_line_I)
	elif (traffic_list[2]=='O'):
		traffic_line_O.append(traffic_list[0])
		traffic_line_O.append(traffic_list[1])
		traffic_line_O.append(traffic_list[3])
		traffic_content_O.append(traffic_line_O)
visitor_room_minspend=[]



for indexi in range(len(traffic_content_I)):
	visitor_room_mindiff_line=[]
	minutediff=minutediff=int(traffic_content_O[indexi][2])-int(traffic_content_I[indexi][2])
	visitor_room_mindiff_line.append(traffic_content_I[indexi][0])
	visitor_room_mindiff_line.append(traffic_content_O[indexi][1])
	visitor_room_mindiff_line.append(minutediff)
	visitor_room_minspend.append(visitor_room_mindiff_line)

visitor_room_minspend.sort()
visitor_room_minspend2=visitor_room_minspend[:]


'''for indexm in range(len(visitor_room_minspend)):
	if(visitor_room_minspend[indexm][1]=='13'):
		print ("visitornum:"+visitor_room_minspend[indexm][0]+"minspend:"+str(visitor_room_minspend[indexm][2]))
	'''
index=0
finallist=[]
while index < len(visitor_room_minspend):
	numvisitors=1
	totalminstay=int(visitor_room_minspend[index][2])
	finallistline=[]
	index2=index+1
	while (index2<len(visitor_room_minspend2)):
		
		if(visitor_room_minspend[index][0]==visitor_room_minspend2[index2][0] and visitor_room_minspend[index][1]==visitor_room_minspend2[index2][1]):
			
			numvisitors=numvisitors
			totalminstay+=int(visitor_room_minspend2[index2][2])
			
			visitor_room_minspend2.pop(index2)
			visitor_room_minspend.pop(index2)
			index2=index2
		elif (visitor_room_minspend[index][0]!=visitor_room_minspend2[index2][0] and visitor_room_minspend[index][1]==visitor_room_minspend2[index2][1]):
			totalminstay+=int(visitor_room_minspend2[index2][2])
			numvisitors+=1
			visitor_room_minspend2.pop(index2)
			visitor_room_minspend.pop(index2)
			
			index2=index2
		elif (visitor_room_minspend[index][0]==visitor_room_minspend2[index2][0] and visitor_room_minspend[index][1]!=visitor_room_minspend2[index2][1]):
			index2+=1
		elif (visitor_room_minspend[index][0]!=visitor_room_minspend2[index2][0] and visitor_room_minspend[index][1]!=visitor_room_minspend2[index2][1]):
			index2+=1
		
	avgminstay=totalminstay/numvisitors
	finallistline.append(visitor_room_minspend[index][1])
	finallistline.append(avgminstay)
	finallistline.append(numvisitors)
	finallist.append(finallistline)
	index+=1
finallist.sort()

for indexnum in range(len(finallist)):
	print ("Room "+finallist[indexnum][0]+", "+str(finallist[indexnum][1])+" minute average visit, "+str(finallist[indexnum][2])+" visitor(s) total")
