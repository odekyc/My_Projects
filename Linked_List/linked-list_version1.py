
class Node:
	def __init__(self,value):
		self.value=value
		self.pointernode=None
		
class LinkedList:
	def __init__(self, head):
		self.head=head
		self.current=None
		self.previous=None
		self.tail=None
	def createlist(self, new_node):
		if (self.current==None):
			self.current=new_node
			self.previous=self.head
			self.previous.pointernode=new_node
			self.head.pointernode=new_node
			self.tail=new_node
			self.tail.pointernode=None
		elif (self.current!=None):
			self.previous=self.current
			self.previous.pointernode=new_node
			self.current=new_node
			self.tail=new_node
			self.tail.pointernode=None
		
	def itersearch(self, value_to_look):
		self.current=self.head
		self.previous=None
		index=1
		while (self.current!=None):
			if (self.current.value!=value_to_look):
				index+=1
				self.previous=self.current
				self.current=self.current.pointernode
			elif (self.current.value==value_to_look):
				return "the node you are trying to look for is node number "+str(index)
				break
		if (self.current==None):
			return "the node you are looking for is not in the LinkedList"

	def recursearch(self, value_to_look, turn, current_node):
		
		if (turn>self.length()):
			return "the node you are looking for is not in the LinkedList"

		elif (turn>=1 and turn <=self.length()):
			
			
			if (current_node.value==value_to_look):
				return "the node you are looking for is node number "+str(turn)
			elif (current_node.value!=value_to_look):
				
				turn+=1
				
				return self.recursearch(value_to_look,turn, current_node.pointernode )
		
		

	def insert(self, new_node, insert_pos):
		
		if (insert_pos==1):
			self.current=self.head
			self.previous=None
			self.head=new_node
			self.head.pointernode=self.current
		elif (insert_pos>self.length()+1):
			print ("you are trying to insert beyound the current length of LinkedList")
		elif (insert_pos>1 and insert_pos<=self.length()):
			
			self.current=self.head
			self.previous=None
			count=1
			while (count<insert_pos):
				self.previous=self.current
				self.current=self.current.pointernode
				count+=1

			new_node.pointernode=self.current
		
			self.previous.pointernode=new_node
			self.current=new_node
		elif (insert_pos==self.length()+1):
			self.current=self.head
			self.previous=None
			count=1
			while (count<insert_pos-1):
				self.previous=self.current
				self.current=self.current.pointernode
				count+=1
			self.tail=new_node
			self.tail.pointernode=None
			self.current.pointernode=new_node
			self.current=self.tail
	
		
		
	

	def length(self):
		
		self.current=self.head
		len=0
		while(self.current!=None):

			self.current=self.current.pointernode
			len+=1
		return len
	def delete(self, del_pos):
		
		if (del_pos==1):
			self.current=self.head.pointernode
			self.head=self.current
			self.previous=None
		elif (del_pos>self.length()):
			print ("the position you are trying to delete is outside of current length of LinkedList")

		elif (del_pos>1 and del_pos!=self.length()):
			count=1

			self.current=self.head
			while (count<del_pos):
				self.previous=self.current
				self.current=self.current.pointernode
				count+=1
			self.current=self.current.pointernode
			self.previous.pointernode=self.current
		elif (del_pos>1 and del_pos==self.length()):
			count=1

			self.current=self.head
			while (count<del_pos-1):
				self.previous=self.current
				self.current=self.current.pointernode
				count+=1
			self.tail=self.current
			self.current.pointernode=None
	def print_backwards(self, next_node):

		if (next_node==self.head):
			return "finished printing all the nodes"
		else :
		
			self.current=self.head
			self.previous=None
			
			
			while (self.current!=None):
				if (self.current.pointernode.value==next_node.value):
					print (self.current.value)
					return self.print_backwards(self.current)
					break
				else :
					self.previous=self.current
					self.current=self.current.pointernode







		

		







node1=Node(27)
node2=Node(32)
node3=Node(44)
node4=Node(51)
newnode=Node(66)
newnode2=Node(38)
mylist=LinkedList(node1)
mylist.createlist(node2)
mylist.createlist(node3)
mylist.createlist(node4)
print (mylist.length())
print (mylist.itersearch(27))
print (mylist.itersearch(32))
print (mylist.itersearch(66))
print (mylist.itersearch(44))
print (mylist.itersearch(51))
print (mylist.itersearch(38))

mylist.insert(newnode, 1)
print (mylist.tail.value)
print (mylist.tail.value)
print (mylist.itersearch(27))
print (mylist.itersearch(32))
print (mylist.itersearch(66))
print (mylist.itersearch(44))
print (mylist.itersearch(51))
print (mylist.itersearch(38))
print (mylist.tail.value)
mylist.delete(5)
print (mylist.length())
print (mylist.itersearch(27))
print (mylist.itersearch(32))
print (mylist.itersearch(66))
print (mylist.itersearch(44))
print (mylist.itersearch(51))
print (mylist.itersearch(38))

mylist.delete(8)
print (mylist.length())
print (mylist.itersearch(27))
print (mylist.itersearch(32))
print (mylist.itersearch(66))
print (mylist.itersearch(44))
print (mylist.itersearch(51))
print (mylist.itersearch(38))

mylist.insert(newnode2,5)
print (mylist.itersearch(27))
print (mylist.itersearch(32))
print (mylist.itersearch(66))
print (mylist.itersearch(44))
print (mylist.itersearch(51))
print (mylist.itersearch(38))
print (mylist.current.value)

print (mylist.recursearch(66, 1, mylist.head))

print (mylist.itersearch(27))
print (mylist.itersearch(32))
print (mylist.itersearch(66))
print (mylist.itersearch(44))
print (mylist.itersearch(51))
print (mylist.itersearch(38))
print (mylist.print_backwards(mylist.tail))