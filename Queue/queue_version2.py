class Node:
	def __init__(self, value):
		self.value=value
		self.next=None

class Queue:
    def __init__(self):
    	self.head=None


    def enqueue(self,next_node):
    	if (self.is_empty()==True):
    		self.head=next_node
    	else:
    		end_node=self.get_end()
    		end_node.next=next_node


    def dequeue(self):
    	if (self.is_empty()==True):
    		return None

    	else: 
    		front_node=self.head
    		self.head=self.head.next
    		front_node.next=None
    		return front_node




    def get_end(self):
    	if (self.is_empty()==True):
    		return None
    	else:
    		cur_node=self.head
    		while (cur_node.next!=None):
    			cur_node=cur_node.next

    		return cur_node




    def is_empty(self):
    	if (self.head==None):
    		return True

    	else:
    		return False


    def get_front(self):
    	return self.head

my_queue=Queue()
print (my_queue.is_empty())
node_1=Node(6)
my_queue.enqueue(node_1)
my_queue.enqueue(Node(9))
my_queue.enqueue(Node(3))
my_queue.enqueue(Node(8))
print (my_queue.get_end().value)
print (my_queue.get_front().value)
my_queue.dequeue()
print (my_queue.get_end().value)
print (my_queue.get_front().value)
    	
