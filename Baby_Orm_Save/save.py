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


	def save(self):
		class_name=self.__class__.__name__
		test_string="SELECT * FROM {} WHERE".format(class_name)
		index=0
		my_dict=self.__dict__
		for name in my_dict:
			if index==0:
				test_string+=" {}= '{}'".format(name,my_dict[name])
				index+=1
			else:
				test_string+=" AND {}='{}'".format(name,my_dict[name])
				index+=1

		self.c.execute(test_string)
		content=self.c.fetchall()
		field_names=[f[0] for f in self.c.description]
		fname_len=len(field_names)
		if content==[] or content==None:
			insert_str="INSERT INTO {} (".format(class_name)
			insert_str_2="VALUES("
			fname_index=1
			value_list=[]
			while fname_index<fname_len:
				if fname_index==fname_len-1:
					insert_str+=" {} )".format(field_names[fname_index])
					insert_str_2+=" ? )"
					has_value=hasattr(self, field_names[fname_index])
					if has_value==True:
						value=getattr(self, field_names[fname_index])
						value_list.append(value)
					else:
						value_list.append(None)
					fname_index+=1
				

				else:
					insert_str+=" {} ,".format(field_names[fname_index])
					insert_str_2+=" ? ,"
					
					has_value=hasattr(self, field_names[fname_index])
					if has_value==True:
						value=getattr(self, field_names[fname_index])
						value_list.append(value)
					else:
						value_list.append(None)
					fname_index+=1
	

			
			value_tuple=tuple(value_list)
			self.c.execute(insert_str+insert_str_2, value_tuple)
			self.conn.commit()
			self.conn.close()
			return True

		



###don't touch the code for these
class Users(Model):
	pass

user=Users(name='Greg',username='greg0133')
user.save()