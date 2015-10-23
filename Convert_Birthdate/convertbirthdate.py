import datetime
age=input("enter your age in number: ")
birthdate=input("enter your birthdate as YYYY-MM-DD : ")
def age_to_time(age):
	months=float(age)*12
	days=float(age)*365
	hours=days*24
	minutes=hours*60
	print ("months : "+str(months))
	print ("days : "+str(days))
	print ("hours : "+str(hours))
	print ("minutes : "+str(minutes))
age_to_time(age)

def birthday_to_time(birthdate):
	mylist=birthdate.split('-')
	t=datetime.datetime(int(mylist[0]), int(mylist[1]), int(mylist[2]))
	today=datetime.datetime.now()
	diff=today-t
	months=float(diff.days)/365
	days=diff.days
	hours=float(diff.days)*24
	minutes=hours*60
	print ("months : "+str(months))
	print ("days : " + str(days))
	print ("hours : " + str(hours))
	print ("minutes : " + str(minutes))