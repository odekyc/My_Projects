import sqlite3

class Model:
	conn = sqlite3.connect('babyorm.db')
	c = conn.cursor()
	def __init__(self,**kwargs):
		for name, value in kwargs.items():
	
			setattr(self, name, value)
		

		

	@classmethod
	def all(cls):
		class_name=cls.__name__
		
		test_string="SELECT * FROM {}".format(class_name)
		cls.c.execute(test_string)
		content=cls.c.fetchall()
		#or result=c.execute(test_string)
		#content=cls.c.fetchall()
		# or content=result.fetchall()
		#print (c.description) prints the fieldnames or column title of the table, works if you use fetchone() instead of fetchall() too
		#for f in c.description:
		#	print (f[0])

		instance_list=[]
		names=[f[0] for f in cls.c.description]
		for row in content:
			
			zipped=zip(names,row)

			row_instance=cls(**dict(zipped))
			instance_list.append(row_instance)

		return instance_list

	

		




	@classmethod
	def get(cls, **kwargs):
		class_name=cls.__name__
		dic_len=len(kwargs)
		index=0
		print (kwargs)
		test_string="SELECT * FROM {} WHERE".format(class_name)
		for name, value in kwargs.items():
			if index==0:
				test_string+=" {}= '{}'".format(name,value)
				index+=1
			elif index==dic_len-1:
				test_string+=" AND {}='{}' LIMIT 1".format(name,value)
			else:
				test_string+=" AND {}='{}'".format(name,value)
				index+=1
		
		print (test_string)
		cls.c.execute(test_string)
		content=cls.c.fetchone()

		if content==None:
			return None
		else:
			names=[f[0] for f in cls.c.description]
	
			zipped=zip(names,content)
			row_instance=cls(**dict(zipped))
			
			return row_instance




		
	@classmethod
	def filter(cls, **kwargs):
		class_name=cls.__name__
		dic_len=len(kwargs)
		index=0
		test_string="SELECT * FROM {} WHERE".format(class_name)
		for name, value in kwargs.items():
			if index==0:
				test_string+=" {}= '{}'".format(name,value)
				index+=1
			else:
				test_string+=" AND {}='{}'".format(name,value)
				index+=1

		print (test_string)	
		cls.c.execute(test_string)
		content=cls.c.fetchall()
	

		if (content):
			instance_list=[]
			names=[f[0] for f in cls.c.description]
			for row in content:
			
				zipped=zip(names,row)

				row_instance=cls(**dict(zipped))
				instance_list.append(row_instance)

			return instance_list



		elif content==None or content==[]: 
			return None




		



###don't touch the code for these
class Users(Model):
	pass

class Stocks(Model):
	pass


print (Users.all())
print (Stocks.all()[0].symbol)
user=Users(name='Dr.')
print (user.get(name='Dr.').balance)
print (user.get(name='Dr.', balance=39994.0).address)
print (user.get(name='Dr.'))
print (user.filter(name='Dr.', balance=35969.0)[0].address)
print (user.filter(name='Dr.', balance=35969.0))