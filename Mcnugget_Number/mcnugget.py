def mcnugget_1980():
	mynumberlist=[]
	for m in range(1,50):
		mynumberlist.append(m)	
	for i in range(10):
		for x in range(6):
			for y in range(3):
				for number in mynumberlist:
					if (i*6+x*9+y*20==number):
						mynumberlist.remove(number)
	print ("The following list contains non-mcnugget numbers for 1980 : ")
	print (mynumberlist)

def mcnugget_2015():
	mynumberlist=[]
	for m in range(1,200):
		mynumberlist.append(m)
		for i in range(20):
			for x in range(15):
				for y in range(10):
					for n in range(8):
						for p in range(3):
							for number in mynumberlist:
								if (i*4+x*6+y*10+n*20+p*40==number):
									mynumberlist.remove(number)
	print ("The following list contains non-mcnugget numbers for 2015 : ")
	print (mynumberlist)
mcnugget_1980()
mcnugget_2015()